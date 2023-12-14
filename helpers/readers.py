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
    'cmu/movies_scraped': GENERATED_PATH / 'scraped_cmu_movies_infobox.parquet',

    # IMDb tables
    'imdb/names': DATA_PATH / 'IMDb/name.basics.tsv',
    'imdb/movies': DATA_PATH / 'IMDb/title.basics.tsv',
    'imdb/principals': DATA_PATH / 'IMDb/title.principals.tsv',
    'imdb/ratings': DATA_PATH / 'IMDb/title.ratings.tsv',
    'imdb/enhanced_movies': DATA_PATH / 'IMDb/enhanced_imdb.csv', # external
    'imdb/awards' : DATA_PATH / 'IMDb/awards.csv', # from Kaggle (https://www.kaggle.com/datasets/iwooloowi/film-awards-imdb)
    'imdb/akas': DATA_PATH / 'IMDb/title.akas.tsv', # unused for now
    'imdb/crew': DATA_PATH / 'IMDb/title.crew.tsv', # unused for now
    'imdb/episode': DATA_PATH / 'IMDb/title.episode.tsv', # unused for now

    # Mappings
    'mapping_wikipedia_imdb_freebase': GENERATED_PATH / 'wp2imdb.csv',
    'mapping_wikipedia_imdb': GENERATED_PATH / 'wp2imdb_01.csv',
    'mapping_freebase_imdb': GENERATED_PATH / 'wp2imdb_02.csv',

    # MovieLens (from Kaggle: https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)
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

def read_dataframe(name: str, usecols: list[str] = None, preprocess=False, convert_downcast=True) -> pd.DataFrame:
    """Reads a dataframe with a suitable method and arguments and returns it."""

    filepath = FILES[name]

    if not Path(filepath).exists():
        print(f"⚠️ File not found: {filepath} ⚠️")
        return None

    ### CMU
    if name == 'cmu/summaries':
        summaries = pd.read_csv(filepath,
                    names=usecols,
                    sep= '\t',
                    )
        if preprocess:
            print("Ignoring preprocess")
        if convert_downcast:
            summaries = convert_and_downcast(summaries)
        return summaries
    
    if name == 'cmu/movies':
        movies = pd.read_csv(filepath,
            names=usecols,
            sep='\t',
        )
        if preprocess:
            movies = preprocess_cmu_movies(movies)
        if convert_downcast:
            movies = convert_and_downcast(movies)
        return movies

    if name == 'cmu/characters':
        characters = pd.read_csv(filepath,
            names =usecols,
            sep='\t',
        )
        if preprocess:
            characters = preprocess_cmu_characters(characters)
        if convert_downcast:
            characters = convert_and_downcast(characters)
        return characters

    if name == 'cmu/nameclusters':
        names_clusters = pd.read_csv(filepath,
                    names=usecols,
                    sep= '\t')
        if preprocess:
            print("Ignoring preprocess")
        if convert_downcast:
            names_clusters = convert_and_downcast(names_clusters)
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
        if preprocess:
            print("Ignoring preprocess")
        tvtropes_clusters = pd.DataFrame(rows)
        if convert_downcast:
            tvtropes_clusters = convert_and_downcast(tvtropes_clusters)
        return tvtropes_clusters
    
    if name == 'cmu/movies_scraped':
        if preprocess:
            print("Ignoring preprocess")
        if convert_downcast:
            return convert_and_downcast(pd.read_parquet(filepath))
        else:
            return pd.read_parquet(filepath)

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
        if convert_downcast:
            names = convert_and_downcast(names)
        return names
    
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
        if convert_downcast:
            movies = convert_and_downcast(movies)
        return movies

    if name == 'imdb/principals': # (reused code from imdb/movies)
        principals = pd.read_csv(filepath,
            names=usecols,
            sep='\t',
            na_values=['\\N'],
        )
        principals['category'] = principals['category'].astype('category')
        if preprocess:
            print("Ignoring preprocess")
        if convert_downcast:
            principals = convert_and_downcast(principals)
        return principals 
    
    if name == 'imdb/ratings':
        ratings = pd.read_csv(filepath,
            names=usecols,
            sep='\t',
            na_values=['\\N'],
        )
        if preprocess:
            print("Ignoring preprocess")
        if convert_downcast:
            ratings = convert_and_downcast(ratings)
        return ratings
    
    if name == 'imdb/enhanced_movies':
        movies = pd.read_csv(filepath,
            names=usecols,
            sep=',',
            dtype={'year': object},
        )
        movies.loc[movies["year"] == "TV Movie 2019", "year"] = "2019"
        movies['year'] = movies['year'].astype('Int64')
        if preprocess:
            print("Ignoring preprocess")
        if convert_downcast:
            movies = convert_and_downcast(movies)
        return movies
    
    if name == 'imdb/awards':
        awards = pd.read_csv(filepath,
            names=usecols,
            sep=',',
            dtype={'year': object,
                   'characterNames' : object},
        )
        awards['year'] = awards['year'].astype('Int64')
        if preprocess:
            print("Ignoring preprocess")
        if convert_downcast:
            awards = convert_and_downcast(awards)
        return awards
    
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
        if convert_downcast:
            akas = convert_and_downcast(akas)
        return akas
    
    if name == 'imdb/crew':
        crew = pd.read_csv(filepath,
            names=usecols,
            sep='\t',
            na_values=['\\N'],
        )
        if preprocess:
            print("Ignoring preprocess")
        if convert_downcast:
            crew = convert_and_downcast(crew)
        return crew
    
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
        if convert_downcast:
            episode = convert_and_downcast(episode)
        return episode
    
    ### Mappings

    if name == 'mapping_wikipedia_imdb_freebase':
        mapping = pd.read_csv(filepath,
            names=usecols,
            sep=',',
        )
        mapping['wikipedia'] = mapping['wikipedia'].astype('Int64')
        if preprocess:
            print("Ignoring preprocess")
        if convert_downcast:
            mapping = convert_and_downcast(mapping)
        return mapping
    
    if (name == 'mapping_wikipedia_imdb') or (name == 'mapping_freebase_imdb'):
        mapping = pd.read_csv(filepath,
            names=usecols,
            sep=',',
        )
        if preprocess:
            print("Ignoring preprocess")
        if convert_downcast:
            mapping = convert_and_downcast(mapping)
        return mapping
    
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

        if convert_downcast:
            movies = convert_and_downcast(movies)
        return movies
    
    if name == 'movieLens/credits':
        credits = pd.read_csv(filepath,
            names=usecols,
        )
        if preprocess:
            print("Ignoring preprocess")
        if convert_downcast:
            credits = convert_and_downcast(credits)
        return credits
    
    if name == 'movieLens/keywords':
        keywords = pd.read_csv(filepath,
            names=usecols,
        )
        if preprocess:
            print("Ignoring preprocess")
        if convert_downcast:
            keywords = convert_and_downcast(keywords)
        return keywords
    
    if name == 'movieLens/links':
        links = pd.read_csv(filepath,
            names=usecols,
        )
        if preprocess:
            links['imdbId'] = links['imdbId'].apply(lambda x: 'tt{:07d}'.format(x))

        links['tmdbId'] = links['tmdbId'].astype('Int64')

        if convert_downcast:
            links = convert_and_downcast(links)
        return links
    
    if name == 'movieLens/ratings':
        ratings = pd.read_csv(filepath,
            names=usecols,
        )
        if preprocess:
            print("Ignoring preprocess")
        if convert_downcast:
            ratings = convert_and_downcast(ratings)
        return ratings

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
