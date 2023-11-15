"""This module contains classes and methods for reading and treating raw data."""

import pandas as pd
from pathlib import Path

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
    # ...
}

def read_dataframe(name: str, usecols: list[str] = None) -> pd.DataFrame:
    """Reads a dataframe with a suitable method and arguments and returns it."""

    filepath = FILES[name]

    if name == 'cmu/movies':
        df = pd.read_csv(filepath,
            usecols=usecols,
            sep='\t',
            names=['wikipedia', 'freebase', 'title', 'release', 'borevenue', 'runtime', 'languages', 'countries', 'genres'],
        )
        if 'release' in df:
            df.release = pd.to_datetime(df.release, format='mixed', errors='coerce')
        if 'languages' in df:
            df.languages = df.languages.apply(eval)
        if 'countries' in df:
            df.countries = df.countries.apply(eval)
        if 'genres' in df:
            df.genres = df.genres.apply(eval)

    if name == 'cmu/characters':
        ...

    if name == 'imdb/movies':
        df = pd.read_csv(filepath,
            usecols=usecols,
            sep='\t',
            na_values=['\\N'],
            dtype={'runtimeMinutes': object},  # Has some strings
        )

    return df