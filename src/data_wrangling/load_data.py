#!/usr/bin/python3

import pandas as pd
import ast
import numpy as np
def load_political_quotes(country=None, political_alignment=None, year=None, chunksize=1000):
    # TODO: Handle parties with more than one country and more than one
    # political alignment
    data_dir = '../../data/'
    politician_quotes_dir = data_dir + 'politician_quotes_dataset/'
    parties_file_path = politician_quotes_dir + 'parties.csv.gz'
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

    valid_politicians = parties['politicians'].explode().unique()

    for year in quote_years:
        quotes_path = politician_quotes_dir + 'quotes-' + str(year) + '-politicians.csv.gz'

        with pd.read_csv(quotes_path, compression='gzip', chunksize=chunksize) as df_reader:
            for chunk in df_reader:
                # Get politicians with those parties
                parties['politicians']
                test = chunk[chunk.qid.isin(valid_politicians)]
                yield test
