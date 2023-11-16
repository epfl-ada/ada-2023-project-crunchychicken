"""This module contains classes and methods for reading and treating raw data."""

import pandas as pd
from pathlib import Path
import json

DATA_PATH = Path(__file__).resolve().parent.parent / 'data'

FILES = {
    # CMU tables
    'cmu/movies': DATA_PATH / 'CMU/movie.metadata.tsv',
    'cmu/characters': DATA_PATH / 'CMU/character.metadata.tsv',
    'cmu/nameclusters': DATA_PATH / 'CMU/name.clusters.txt',
    'cmu/summaries': DATA_PATH / 'CMU/plot_summaries.txt',
    'cmu/tvtropes': DATA_PATH / 'CMU/tvtropes.clusters.txt',

    # IMDb tables
    'imdb/names': DATA_PATH / 'IMDb/name.basics.tsv',
    'imdb/movies': DATA_PATH / 'IMDb/title.basics.tsv',
    
    # NLP old annotations dataframes
    'cmu/tokens_2013' : DATA_PATH / 'CMU/annotations_2013/tokens.parquet',
    'cmu/dependencies_2013' : DATA_PATH / 'CMU/annotations_2013/dependencies.parquet',

    # NLP new annotations dataframes
    'cmu/tokens_2023': DATA_PATH / 'CMU/annotations_2023/tokens.parquet'
    'cmu/dependencies_2023': DATA_PATH / 'CMU/annotations_2023/dependencies.parquet'
    'cmu/entities_2023': DATA_PATH / 'CMU/annotations_2023/entities.parquet'
    
}

def read_dataframe(name: str, usecols: list[str] = None) -> pd.DataFrame:
    """Reads a dataframe with a suitable method and arguments and returns it."""

    filepath = FILES[name]

    if name == 'cmu/movies':
        movies = pd.read_csv(filepath,
            names=usecols,
            sep='\t',
        )
        #if 'release' in df:
        #    df.release = pd.to_datetime(df.release, format='mixed', errors='coerce')
        #if 'languages' in df:
        #    df.languages = df.languages.apply(eval)
        #if 'countries' in df:
        #    df.countries = df.countries.apply(eval)
        #if 'genres' in df:
        #    df.genres = df.genres.apply(eval)
        return movies  

    if name == 'cmu/characters':
        characters = pd.read_csv(filepath,
            names =usecols,
            sep='\t',
        )
        return characters
    
    if name == 'cmu/plot_summaries':
        plot_summaries = pd.read_csv(filepath,
                    usecols=usecols,
                    sep= '\t')
        return plot_summaries

    if name == 'cmu/nameclusters':
        names_clusters = pd.read_csv(filepath,
                    usecols=usecols,
                    sep= '\t')
        return names_clusters

    if name == 'cmu/tvtropes':
        rows = []
        with open(filepath, 'r') as file:
            for line in file:
                char_type, json_string = line.strip().split('\t', 1)
                char_info = json.loads(json_string)
                row = {
                    'Character type': char_type,
                    'Character name': char_info['char'],
                    'Movie name': char_info['movie'],
                    'Freebase character/actor map ID': char_info['id'],
                    'Actor name': char_info['actor']
                }
                rows.append(row)
        tvtropes_clusters = pd.DataFrame(rows, usecols=usecols)
        return tvtropes_clusters # to check

    if name == 'imdb/movies':
        movies = pd.read_csv(filepath,
            names=usecols,
            sep='\t',
            na_values=['\\N'],
            dtype={'runtimeMinutes': object},  # Has some strings
        )
        return movies

    if name == 'imdb/names': # to correct / modify (reused code from above imdb/movies)
        names = pd.read_csv(filepath,
            names=usecols,
            sep='\t',
            na_values=['\\N'], # probably wrong
            dtype={'runtimeMinutes': object},  # probably wrong
        )
        return names

    #if name == 'tokens_2013:

    
