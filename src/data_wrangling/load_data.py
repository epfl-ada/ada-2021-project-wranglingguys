import pandas as pd
import ast
import numpy as np
from pathlib import Path
import os


def load_political_quotes(country=None, political_alignment=None, year=None, chunksize=1000):
    """
    Loads politician quotes matching the given filters.
    :param country: list of strings with countries used to filter where the
                    political parties of the politicians are from.
    :param political_alignment: list of strings with political alignments used
                                to filter the political parties of the politicians.
    :param year: years when the articles with the quotes were published.
    :param chunksize: defines the number of lines to read at a time from the quotebank datasets.
    :return: a generator with quotes matching the filters.
    """
    # TODO: Handle parties with more than one country and more than one
    # political alignment

    data_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
    politician_quotes_dir = os.path.join(data_dir, 'politician_quotes_dataset')
    parties_file_path = os.path.join(politician_quotes_dir, 'parties.csv.gz')

    parties = pd.read_csv(parties_file_path, compression='gzip', index_col=0)

    # Remove wrong political party ids
    parties.drop(parties.index[parties['country'].isnull()], inplace=True)
    parties.drop(parties.index[parties['political_alignment'].isnull()], inplace=True)

    # For now, when there are multiple countries and political alignmentS just choose first
    parties['country'] = parties['country'].apply(lambda x: ast.literal_eval(x)) \
                                           .apply(lambda x: x[0] if len(x) > 0 else None)
    parties['political_alignment'] = parties['political_alignment'].apply(lambda x: ast.literal_eval(x)) \
                                                                   .apply(lambda x: x[0] if len(x) > 0 else None)
    parties['politicians'] = parties['politicians'].apply(lambda x: ast.literal_eval(x))

    if political_alignment:
        parties.drop(parties.index[~parties['political_alignment'].isin(political_alignment)], inplace=True)
    if country:
        parties.drop(parties.index[~parties['country'].isin(country)], inplace=True)

    quote_years = np.arange(2015, 2021)
    if year:
        quote_years = year

    politicians = parties.explode('politicians').set_index('politicians')
    # Temprorarily, when there are politicians with more than a party
    # keep first
    politicians = politicians[~politicians.index.duplicated(keep='first')]

    for year in quote_years:
        quotes_path = os.path.join(politician_quotes_dir, 'temp_quotes-' + str(year) + '-politicians.csv.gz')
        with pd.read_csv(quotes_path, compression='gzip', chunksize=chunksize) as df_reader:
            for chunk in df_reader:
                chunk = chunk[chunk.qid.isin(politicians.index)] # Get politicians with those parties
                if chunk.empty:
                    continue
                # Make index match to copy column values
                chunk.set_index('qid', inplace=True)
                # Append country and political alignment information
                chunk['country'] = politicians['country']
                chunk['political_alignment'] = politicians['political_alignment']
                chunk['political_party'] = politicians['label']
                # Reset index to quoteID
                chunk = chunk.reset_index().set_index('quoteID')
                yield  chunk
