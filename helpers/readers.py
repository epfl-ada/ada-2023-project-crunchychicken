"""This module contains classes and methods for reading and treating raw data."""

import pandas as pd
from pathlib import Path
import json
import pickle
import numpy as np # unused?
from helpers.utils import preprocess_cmu_movies, preprocess_cmu_characters, preprocess_imdb_movies, preprocess_movieLens_movies, preprocess_cmu_movies_scraped
from helpers.utils import convert_and_downcast, cast_back_to_int64, downcast_int64
import time

DATA_PATH = Path(__file__).resolve().parent.parent / 'data'
GENERATED_PATH = Path(__file__).resolve().parent.parent / 'generated'

def save_dict_to_generated(filename:str, dic: dict):
    if not filename:
            raise ValueError("Filename cannot be empty")

    full_path = GENERATED_PATH / filename

    if not full_path.suffix:
        full_path = full_path.with_suffix('.pickle')

    with open(full_path, 'wb') as handle:
        pickle.dump(dic, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_dict_from_generated(filename: str):
    if not filename:
        raise ValueError("Filename cannot be empty")

    full_path = GENERATED_PATH / filename

    if not full_path.suffix:
        full_path = full_path.with_suffix('.pickle')

    with open(full_path, 'rb') as handle:
        return pickle.load(handle)

def save_parquet_to_generated(filename: str, df: pd.DataFrame):
    if not filename:
        raise ValueError("Filename cannot be empty")

    full_path = GENERATED_PATH / filename

    if not full_path.suffix:
        full_path = full_path.with_suffix('.parquet')

    df.to_parquet(full_path, compression='brotli')


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

FILES_PARQUET = {

    # CMU tables
    'cmu/movies': DATA_PATH / 'CMU/movie.metadata.parquet',
    'cmu/characters': DATA_PATH / 'CMU/character.metadata.parquet',
    # IMDb tables
    'imdb/names': DATA_PATH / 'IMDb/name.basics.parquet',
    'imdb/movies': DATA_PATH / 'IMDb/title.basics.parquet',
    'imdb/principals': DATA_PATH / 'IMDb/title.principals.parquet',
    'imdb/ratings': DATA_PATH / 'IMDb/title.ratings.parquet',
    'imdb/enhanced_movies': DATA_PATH / 'IMDb/enhanced_imdb.parquet', # external
    'imdb/awards' : DATA_PATH / 'IMDb/awards.parquet', # from Kaggle (https://www.kaggle.com/datasets/iwooloowi/film-awards-imdb)
    'imdb/akas': DATA_PATH / 'IMDb/title.akas.parquet', # unused for now
    'imdb/crew': DATA_PATH / 'IMDb/title.crew.parquet', # unused for now
    'imdb/episode': DATA_PATH / 'IMDb/title.episode.parquet', # unused for now

    # MovieLens (from Kaggle: https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)
    'movieLens/credits': DATA_PATH / 'MovieLens/credits.parquet', # unused for now
    'movieLens/keywords': DATA_PATH / 'MovieLens/keywords.parquet', # unused for now
    'movieLens/links': DATA_PATH / 'MovieLens/links.parquet', # unused for now
    'movieLens/links_small': DATA_PATH / 'MovieLens/links_small.parquet', # unused for now
    'movieLens/movies': DATA_PATH / 'MovieLens/movies_metadata.parquet',
    'movieLens/ratings': DATA_PATH / 'MovieLens/ratings.parquet', # unused for now
    'movieLens/ratings_small': DATA_PATH / 'MovieLens/ratings_small.parquet', # unused for now

    # add merged dataframes here so we don't merge each time
    'merged/movies': GENERATED_PATH / 'movies.parquet',
    'merged/directors': GENERATED_PATH / 'directors.parquet',
    'merged/awards': GENERATED_PATH / 'awards.parquet',

    'directors/metrics': GENERATED_PATH / 'director_metrics.parquet',
    "directors/scores": GENERATED_PATH / 'directors_with_score.parquet',
    "movie/scores": GENERATED_PATH / 'movie_with_score.parquet',

    "q1/matched_imdb_people": GENERATED_PATH / 'q1_matched_imdb_people.parquet',
    "q1/jobs_principal_people": GENERATED_PATH / 'q1_jobs_principal_people.parquet',
    "q1/mip_enhanced": GENERATED_PATH / 'q1_mip_enhanced.parquet',
    "q1/enhanced_directors": GENERATED_PATH / 'q1_enhanced_directors.parquet',
    "q1/movies_wcs": GENERATED_PATH / 'q1_movies_wcs.parquet',
    "q1/directors": GENERATED_PATH / 'q1_directors.parquet',
    "q1/movies": GENERATED_PATH / 'q1_movies.parquet',
    "q1/directors_core" : GENERATED_PATH / 'q1_directors_core.parquet',
    "q1/matched_test" : GENERATED_PATH / 'q1_matched_test.parquet',

}

def read_dataframe(name: str, usecols: list[str] = None, preprocess=False, convert_downcast=True) -> pd.DataFrame:
    """Reads a dataframe with a suitable method and arguments and returns it."""

    try: 
        filepath = FILES[name]
    except:
        print("Key Error: key does not exist in FILES")

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
            cmu_movies_scraped = preprocess_cmu_movies_scraped(pd.read_parquet(filepath))
            if convert_downcast:
                return convert_and_downcast(cmu_movies_scraped)
        elif convert_downcast:
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
            dtype={
                'year': object,
                'characterNames' : object,
            },
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
    
    if name == 'movieLens/links_small':
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
    
    if name == 'movieLens/ratings_small':
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
    
def read_dataframe_parquet(name: str) -> pd.DataFrame:
    """Reads a dataframe with a suitable method and arguments and returns it."""

    try: 
        filepath = FILES_PARQUET[name]
    except:
        print("Key Error: key does not exist in FILES_PARQUET")
    

    if not Path(filepath).exists():
        print(f"⚠️ File not found: {filepath} ⚠️")
        return None
    
    return pd.read_parquet(filepath)

# to get revenue, budget, profit for cmu movies
def get_cmu_movies_enhanced(use_parquet=True) -> pd.DataFrame:
    if use_parquet == False:
        cmu_movies = read_dataframe(
            name='cmu/movies',
            preprocess=True,
            usecols=[
                "Wikipedia movie ID", "Freebase movie ID", "Movie name",
                "Movie release date", "Movie box office revenue", "Movie runtime",
                "Movie languages", "Movie countries", "Movie genres",
            ]
        )
        
    else:
        cmu_movies = read_dataframe_parquet("cmu/movies")

    cmu_scraped_movies = read_dataframe(name='cmu/movies_scraped', preprocess=True)

    cmu_movies = cast_back_to_int64(cmu_movies, "Wikipedia movie ID")
    cmu_movies_enhanced = pd.merge(cmu_movies, cmu_scraped_movies, left_on="Wikipedia movie ID", right_on="Wikipedia movie ID", how="left")
    cmu_movies = downcast_int64(cmu_movies, "Wikipedia movie ID")
    cmu_movies_enhanced = downcast_int64(cmu_movies_enhanced, "Wikipedia movie ID")
    
    cmu_movies_enhanced['Movie release Year'] = cmu_movies_enhanced['Movie release Year'].fillna(cmu_movies_enhanced['release_year'])
    
    cmu_movies_enhanced = cmu_movies_enhanced.drop(columns=['release_year'])
    cmu_movies_enhanced = cmu_movies_enhanced.drop(columns=['Movie runtime'])
    cmu_movies_enhanced = cmu_movies_enhanced.drop(columns=['Movie box office revenue'])
    # can also drop month and day if not needed
    return cmu_movies_enhanced


# NOTE: Feel free to edit the following method as you wish
# The idea is to have primary, clean dataframes that contain everything that we need
# If you need a column but it's dropped, just add it and make sure the column is not repeated and is clean


def prepare_dataframes(use_parquet=False, save=True) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Prepares the primary movies dataframe by combining multiple raw dataframes."""
    function_start_time = time.perf_counter()
    # Read dataframs
    if use_parquet == False:
        start_time = time.perf_counter()
        cmu_movies = read_dataframe(
            name='cmu/movies',
            preprocess=True,
            usecols=[
                "Wikipedia movie ID", "Freebase movie ID", "Movie name",
                "Movie release date", "Movie box office revenue", "Movie runtime",
                "Movie languages", "Movie countries", "Movie genres",
            ]
        )
        print("Finished loading cmu_movies")
        imdb_info = read_dataframe(name='imdb/movies', preprocess=True)
        print("Finished loading imdb_info")
        imdb_ratings = read_dataframe(name='imdb/ratings')
        print("Finished loading imdb_ratings")
        #movieLens_movies = read_dataframe(name='movieLens/movies', preprocess=True)
        imdb_crew = read_dataframe(name='imdb/crew')
        print("Finished loading imdb_crew")
        imdb_people = read_dataframe(name='imdb/names')
        print("Finished loading imdb_people")
        imdb_awards = read_dataframe('imdb/awards')
        print("Finished loading imdb_awards")
        
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time    
        print(f"Total loading time: {elapsed_time} seconds")
    else:
        start_time = time.perf_counter()
        cmu_movies = read_dataframe_parquet("cmu/movies")
        print("Finished loading cmu_movies")
        imdb_info = read_dataframe_parquet("imdb/movies")
        print("Finished loading imdb_info")
        imdb_ratings = read_dataframe_parquet('imdb/ratings')
        print("Finished loading imdb_ratings")
        #movieLens_movies = read_dataframe_parquet('movieLens/movies')
        imdb_crew = read_dataframe_parquet('imdb/crew')
        print("Finished loading imdb_crew")
        imdb_people = read_dataframe_parquet('imdb/names')
        print("Finished loading imdb_people")
        imdb_awards = read_dataframe_parquet('imdb/awards')
        print("Finished loading imdb_awards")
        
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time    
        print(f"Total loading time: {elapsed_time} seconds")

    # Drop extra columns of imdb_awards
    imdb_awards.drop([
            'occurrence', 'winAnnouncementTime', 'name',
            'originalName', 'songNames', 'episodeNames',
            'characterNames', 'isSecondary', 'notes'
        ],
        axis=1,
        inplace=True,
    )

    # Separate movie awards from persons awards
    imdb_awards_movies = imdb_awards.query('isTitle == True')
    imdb_awards_persons = imdb_awards.query('isPerson == True')

    # Copy cmu_movies
    movies = cmu_movies.drop(['Movie release Day', 'Movie release Month'], axis=1).copy()

    # Rename the columns of movies
    # NOTE: Feel free to change the column names, we'll need to unify the names in the final notebook
    movies.rename(
        columns={
            'Wikipedia movie ID': 'wikipediaID',
            'Freebase movie ID': 'freebaseID',
            'Movie name': 'title',
            'Movie box office revenue': 'revenue',
            'Movie runtime': 'runtime',
            'Movie languages': 'languages',
            'Movie countries': 'countries',
            'Movie genres': 'genres',
            'Movie release Year': 'release',
        },
        inplace=True,
    )

    # Merge movies with imdb mapping (CMU IMDb movie merge)
    mapping_freebase_imdb = read_dataframe(name='mapping_freebase_imdb')
    movies = movies.merge(
        right=mapping_freebase_imdb.drop_duplicates(subset='freebase'),
        left_on='freebaseID', right_on='freebase', how='left'
    ).rename(columns={'imdb': 'tconst'}).drop('freebase', axis=1)
    print("Finished merge 1/6 : cmu imdb movies")

    # Remove duplicated movies
    movies.drop_duplicates(subset='tconst', inplace=True)

    # Merge movies with imdb_info
    movies = movies.merge(
        right=imdb_info.rename(columns={'genres': 'genres_imdb', 'runtimeMinutes': 'runtime_imdb'})[['tconst', 'isAdult', 'runtime_imdb', 'genres_imdb']],
        on='tconst', how='left',
    )
    print("Finished merge 2/6 : movies with imdb_info")

    # Merge movies with imdb_ratings
    movies = movies.merge(
        right=imdb_ratings.rename(columns={'averageRating': 'rating', 'numVotes': 'votes'}),
        on='tconst', how='left',
    )
    print("Finished merge 3/6 : movies with imdb_ratings")

    # # movies Merge with movieLens_movies  #  NOTE: Only adds ratings for 100 movies, not worth it
    # movies = movies.merge(
    #     right=movieLens_movies[['vote_average', 'vote_count', 'imdb_id']].rename(columns={'vote_average': 'rating_lens', 'vote_count': 'votes_lens', 'imdb_id': 'tconst'}),
    #     on='tconst', how='left',
    # )
    # movies.rating_lens.replace(to_replace=0, value=pd.NA)

    # Merge movies with imdb_crew
    movies = movies.merge(right=imdb_crew.drop('writers', axis=1), on='tconst', how='left')
    print("Finished merge 4/6 : movies with imdb_crew")

    # Add awards and nominations to movies
    #imdb_awards_movies_counts = imdb_awards_movies.groupby(by='const').apply(lambda df: pd.Series({'awardsNominated': len(df), 'awardsWon': len(df.query('isWinner == "True"'))})).reset_index()
    # testing an optimization:
    imdb_awards_movies_counts = imdb_awards_movies.groupby('const').agg(awardsNominated=('const', 'size'), awardsWon=('isWinner', lambda x: (x == "True").sum())).reset_index()
    movies = movies.merge(
        right=imdb_awards_movies_counts,
        left_on='tconst', right_on='const', how='left'
    ).drop('const', axis=1)
    print("Finished merge 5/6 : movies and nominations for tconst")
    movies.awardsNominated.fillna(0, inplace=True)
    movies.awardsWon.fillna(0, inplace=True)
    movies.awardsNominated = movies.awardsNominated.astype(int)
    movies.awardsWon = movies.awardsWon.astype(int)

    # Set the index of movies
    movies = movies.set_index('tconst')

    # Get a list of the existing directors from the movies dataframe
    nconsts = []
    for item in movies.dropna(subset='directors').directors.str.split(','):
        nconsts.extend(item)
    nconsts = set(nconsts)

    # Get the directors from imdb_people
    directors = imdb_people[imdb_people.nconst.isin(nconsts)].copy()

    # Add awards and nominations to directors
    #imdb_awards_persons_counts = imdb_awards_persons.groupby(by='const').apply(lambda df: pd.Series({'awardsNominated': len(df), 'awardsWon': len(df.query('isWinner == "True"'))})).reset_index()
    # testing an optimization:
    imdb_awards_persons_counts = imdb_awards_persons.groupby('const').agg(
        awardsNominated=('const', 'size'),
        awardsWon=('isWinner', lambda x: (x == "True").sum())
    ).reset_index()
    directors = directors.merge(
        right=imdb_awards_persons_counts,
        left_on='nconst', right_on='const', how='left'
    ).drop('const', axis=1)
    print("Finished merge 6/6 : movies and nominations for nconst")
    directors.awardsNominated.fillna(0, inplace=True)
    directors.awardsWon.fillna(0, inplace=True)
    directors.awardsNominated = directors.awardsNominated.astype(int)
    directors.awardsWon = directors.awardsWon.astype(int)

    # Set the index of directors
    directors = directors.set_index('nconst')

    if save:
        movies.to_parquet(GENERATED_PATH / 'movies.parquet', compression="brotli")
        directors.to_parquet(GENERATED_PATH / 'directors.parquet', compression="brotli")
        imdb_awards.to_parquet(GENERATED_PATH / 'awards.parquet', compression="brotli")
        print("Saved merged dataframes to generated folder")

    function_end_time = time.perf_counter()
    function_elapsed_time = function_end_time - function_start_time  
    print(f"Total merge time: {function_elapsed_time} seconds")

    return movies.copy(), directors.copy(), imdb_awards.copy()
