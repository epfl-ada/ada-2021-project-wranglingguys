import pandas as pd
import pywikibot
import os

if __name__ == "__main__":
    data_dir = '../../data/'
    # Get all the speakers that have a party in the parquet file
    parquet_dir = data_dir + 'speaker_attributes/speaker_attributes.parquet/'
    politicians = pd.DataFrame(columns=['id', 'label', 'party'])
    for file in os.listdir(parquet_dir):
        if file.endswith('.parquet'):
            df = pd.read_parquet(os.path.join(parquet_dir, file))
            df_politicians = df.loc[df.party.notnull(), ['id', 'label', 'party']] # Speakers with a political party
            politicians = politicians.append(df_politicians)

    politicians.set_index('id', inplace=True)

    quotes_dir = data_dir + 'quotebank/'
    out_dir = data_dir + 'politician_quotes_dataset/'

    # Loop through the 5 quotebank datasets
    for file in os.listdir(quotes_dir):
        file_out = out_dir + os.path.splitext(os.path.splitext(file)[0])[0] + '-politicians.csv'
        with pd.read_json(os.path.join(quotes_dir, file), lines=True, compression='bz2', chunksize=10000) as df_reader:
            # Loop through each of the chunks of the dataset
            for index, chunk in enumerate(df_reader):
                chunk['qid'] = chunk['qids'].apply(lambda x: x[0] if len(x) > 0 else None)
                # Remove the quotes not belonging to politicians
                idx_to_drop = chunk.index[~chunk.qid.isin(politicians.index)]
                chunk.drop(idx_to_drop, inplace=True)
                # Append to file
                chunk.to_csv(file_out, mode=('a' if index else 'w'),
                             index=False, compression="gzip", header=(index == 0))
