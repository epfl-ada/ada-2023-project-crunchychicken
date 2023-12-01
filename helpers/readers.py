"""This module contains classes and methods for reading and treating raw data."""

import pandas as pd
from pathlib import Path
import json
 # helpers. so notebook can resolve path 
from helpers.utils import convert_and_downcast, preprocess_cmu_movies, preprocess_cmu_characters, preprocess_imdb_movies, preprocess_movieLens_movies

DATA_PATH = Path(__file__).resolve().parent.parent / 'data'
GENERATED_PATH = Path(__file__).resolve().parent.parent / 'generated'

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
    'imdb/principals': DATA_PATH / 'IMDb/title.principals.tsv',
    'imdb/ratings': DATA_PATH / 'IMDb/title.ratings.tsv',
    'imdb/akas': DATA_PATH / 'IMDb/title.akas.tsv', # unused for now
    'imdb/crew': DATA_PATH / 'IMDb/title.crew.tsv', # unused for now
    'imdb/episode': DATA_PATH / 'IMDb/title.episode.tsv', # unused for now

    # Mappings
    'mapping_wikipedia_imdb_freebase': GENERATED_PATH / 'wp2imdb.csv',
    'mapping_wikipedia_imdb': GENERATED_PATH / 'wp2imdb_01.csv',
    'mapping_freebase_imdb': GENERATED_PATH / 'wp2imdb_02.csv',

    # MovieLens
    'movieLens/credits': DATA_PATH / 'MovieLens/credits.csv', # unused for now
    'movieLens/keywords': DATA_PATH / 'MovieLens/keywords.csv', # unused for now
    'movieLens/links': DATA_PATH / 'MovieLens/links.csv', # unused for now
    'movieLens/links_small': DATA_PATH / 'MovieLens/links_small.csv', # unused for now
    'movieLens/movies': DATA_PATH / 'MovieLens/movies_metadata.csv',
    'movieLens/ratings': DATA_PATH / 'MovieLens/ratings.csv', # unused for now
    'movieLens/ratings_small': DATA_PATH / 'MovieLens/ratings_small.csv', # unused for now
    
    # NLP old annotations dataframes
    'cmu/tokens_2013' : GENERATED_PATH / 'annotations_2013/tokens.parquet',
    'cmu/dependencies_2013' : GENERATED_PATH / 'annotations_2013/dependencies.parquet',
    'cmu/bags_2013': GENERATED_PATH / 'annotations_2013/bags.parquet',
    'cmu/characters_2013': GENERATED_PATH / 'annotations_2013/characters.parquet',
    'cmu/character_classification_2013': GENERATED_PATH / 'annotations_2013/character_classification.parquet',

    # NLP new annotations dataframes
    'cmu/tokens_2023': GENERATED_PATH / 'annotations_2023/tokens.parquet',
    'cmu/dependencies_2023': GENERATED_PATH / 'annotations_2023/dependencies.parquet',
    'cmu/entities_2023': GENERATED_PATH / 'annotations_2023/entities.parquet',
    'cmu/bags_2023': GENERATED_PATH / 'annotations_2023/bags.parquet',
    'cmu/characters_2023': GENERATED_PATH / 'annotations_2023/characters.parquet',
    'cmu/character_classification_2023': GENERATED_PATH / 'annotations_2023/character_classification.parquet',
    
}

def read_dataframe(name: str, usecols: list[str] = None, preprocess=False) -> pd.DataFrame:
    """Reads a dataframe with a suitable method and arguments and returns it."""

    filepath = FILES[name]

    ### CMU
    if name == 'cmu/summaries':
        summaries = pd.read_csv(filepath,
                    names=usecols,
                    sep= '\t',
                    )
        if preprocess:
            print("Ignoring preprocess")
        return convert_and_downcast(summaries)
    
    if name == 'cmu/movies':
        movies = pd.read_csv(filepath,
            names=usecols,
            sep='\t',
        )
        if preprocess:
            movies = preprocess_cmu_movies(movies)
        return convert_and_downcast(movies)

    if name == 'cmu/characters':
        characters = pd.read_csv(filepath,
            names =usecols,
            sep='\t',
        )
        if preprocess:
            characters = preprocess_cmu_characters(characters)
        return convert_and_downcast(characters)

    if name == 'cmu/nameclusters':
        names_clusters = pd.read_csv(filepath,
                    names=usecols,
                    sep= '\t')
        if preprocess:
            print("Ignoring preprocess")
        return convert_and_downcast(names_clusters)

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
        if preprocess:
            print("Ignoring preprocess")
        tvtropes_clusters = pd.DataFrame(rows)

        return convert_and_downcast(tvtropes_clusters)

    ### IMDb

    if name == 'imdb/names':
        names = pd.read_csv(filepath,
            names=usecols,
            sep='\t',
            na_values=['\\N'],
        )
        names['birthYear'] = names['birthYear'].astype('Int64')
        names['deathYear'] = names['deathYear'].astype('Int64')

        if preprocess:
            print("Ignoring preprocess")

        return convert_and_downcast(names)
    
    if name == 'imdb/movies':
        movies = pd.read_csv(filepath,
            names=usecols,
            sep='\t',
            na_values=['\\N'],
            dtype={'runtimeMinutes': object},  # Has some strings
        )
        movies['titleType'] = movies['titleType'].astype('category')
        movies['isAdult'] = movies['isAdult'].astype('Int64')
        movies['startYear'] = movies['startYear'].astype('Int64')
        movies['endYear'] = movies['endYear'].astype('Int64')
        movies['runtimeMinutes'] = movies['runtimeMinutes'].astype('string')
        if preprocess: # fix runtimeMinutes and genres
            movies = preprocess_imdb_movies(movies)
        return convert_and_downcast(movies)

    if name == 'imdb/principals': # (reused code from imdb/movies)
        principals = pd.read_csv(filepath,
            names=usecols,
            sep='\t',
            na_values=['\\N'],
        )
        principals['category'] = principals['category'].astype('category')
        if preprocess:
            print("Ignoring preprocess")
        return convert_and_downcast(principals) 
    
    if name == 'imdb/ratings':
        ratings = pd.read_csv(filepath,
            names=usecols,
            sep='\t',
            na_values=['\\N'],
        )
        if preprocess:
            print("Ignoring preprocess")
        return convert_and_downcast(ratings)
    
    if name == 'imdb/akas':
        akas = pd.read_csv(filepath,
            names=usecols,
            sep='\t',
            na_values=['\\N'],
            dtype={'attributes': object},
        )
        akas['isOriginalTitle'] = akas['isOriginalTitle'].astype('Int64')
        if preprocess:
            print("Ignoring preprocess")
        return convert_and_downcast(akas)
    
    if name == 'imdb/crew':
        crew = pd.read_csv(filepath,
            names=usecols,
            sep='\t',
            na_values=['\\N'],
        )
        if preprocess:
            print("Ignoring preprocess")
        return convert_and_downcast(crew)
    
    if name == 'imdb/episode':
        episode = pd.read_csv(filepath,
            names=usecols,
            sep='\t',
            na_values=['\\N'],
        )
        episode['seasonNumber'] = episode['seasonNumber'].astype('Int64')
        episode['episodeNumber'] = episode['episodeNumber'].astype('Int64')
        if preprocess:
            print("Ignoring preprocess")
        return convert_and_downcast(episode)
    
    ### Mappings

    if name == 'mapping_wikipedia_imdb_freebase':
        mapping = pd.read_csv(filepath,
            names=usecols,
            sep=',',
        )
        mapping['wikipedia'] = mapping['wikipedia'].astype('Int64')
        if preprocess:
            print("Ignoring preprocess")
        return convert_and_downcast(mapping)
    
    if (name == 'mapping_wikipedia_imdb') or (name == 'mapping_freebase_imdb'):
        mapping = pd.read_csv(filepath,
            names=usecols,
            sep=',',
        )
        if preprocess:
            print("Ignoring preprocess")
        return convert_and_downcast(mapping)
    
    ### MovieLens

    if name == 'movieLens/movies':
        movies = pd.read_csv(filepath,
            names=usecols,
            sep=',',
            dtype=object,
        )
        if preprocess:
            # could add date split to YYYY, MM, DD
            movies = preprocess_movieLens_movies(movies)

        movies['adult'] = movies['adult'].astype('category')
        movies['budget'] = movies['budget'].astype('Int64')
        movies['id'] = movies['id'].astype('Int64')
        movies['popularity'] = movies['popularity'].astype('float')
        movies['revenue'] = movies['revenue'].astype('Int64')
        movies['runtime'] = movies['runtime'].astype('float').astype('Int64')
        movies['video'] = movies['video'].astype('category')
        movies['vote_average'] = movies['vote_average'].astype('float')
        movies['vote_count'] = movies['vote_count'].astype('Int64')
        return convert_and_downcast(movies)

    ### NLP

    if name == 'cmu/tokens_2013':
        return pd.read_parquet(filepath)
    if name == 'cmu/dependencies_2013':
        return pd.read_parquet(filepath)
    if name == 'cmu/bags_2013':
        return pd.read_parquet(filepath)
    if name == 'cmu/characters_2013':
        return pd.read_parquet(filepath)
    if name == 'cmu/character_classification_2013':
        return pd.read_parquet(filepath)
    
    if name == 'cmu/tokens_2023':
        return pd.read_parquet(filepath)
    if name == 'cmu/dependencies_2023':
        return pd.read_parquet(filepath)
    if name == 'cmu/entities_2023':
        return pd.read_parquet(filepath)
    if name == 'cmu/bags_2023':
        return pd.read_parquet(filepath)
    if name == 'cmu/characters_2023':
        return pd.read_parquet(filepath)
    if name == 'cmu/character_classification_2023':
        return pd.read_parquet(filepath)
