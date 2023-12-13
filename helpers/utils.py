import pandas as pd
import ast

def batched(it, sz: int):
    """Generator for retrieving batches from an iterator."""

    start = 0
    while start + sz < len(it):
        yield it[start:start+sz]
        start += sz
    yield it[start:]

def convert_and_downcast(df: pd.DataFrame) -> pd.DataFrame:
    """Convert object columns to string and downcast numeric columns to save memory."""
    for col in df.columns:
        if df[col].dtype == 'category':
            continue
        if df[col].dtype == object:
            df[col] = df[col].astype('string')
        elif df[col].dtype == float:
            df[col] = pd.to_numeric(df[col], downcast='float')
        else:
            df[col] = pd.to_numeric(df[col], downcast='integer')
    return df

def preprocess_cmu_movies(cmu_movies: pd.DataFrame) -> pd.DataFrame:
    cmu_movies.loc[46808, 'Movie countries'] = '{"/m/03rk0": "India"}'
    cmu_movies.loc[67202, 'Movie countries'] = '{"/m/03rk0": "India"}'
    cmu_movies.loc[67202, 'Movie languages'] = '{"/m/0999q": "Malayalam Language"}'
    cmu_movies.loc[72685, 'Movie countries'] = '{"/m/084n_": "Weimar Republic", "/m/0345h": "Germany"}'
    print("Preprocess logs:")
    if len(cmu_movies[cmu_movies['Movie countries'].str.contains('Language')]) == 0:
        print("✅ Fixed Movie Languages inside Movie Countries")
    else:
        print("❌ Failed to fix Movie Languages inside Movie Countries")

    cmu_movies.loc[1825, "Movie languages"] = '{"/m/04306rv": "German Language"}'
    cmu_movies.loc[7855, "Movie languages"] = '{"/m/02bjrlw": "Italian Language", "/m/06nm1": "Spanish Language", "/m/064_8sq": "French Language", "/m/04h9h": "Latin Language", "/m/02h40lc": "English Language", "/m/05qqm": "Polish Language", "/m/04306rv": "German Language"}'
    cmu_movies.loc[20807, "Movie languages"] = '{"/m/0k0sv": "Croatian language", "/m/02bjrlw": "Italian Language", "/m/06b_j": "Russian Language", "/m/06nm1": "Spanish Language", "/m/064_8sq": "French Language", "/m/05zjd": "Portuguese Language", "/m/02h40lc": "English Language", "/m/06zvd": "Slovenian language", "/m/04306rv": "German Language", "/m/02hwhyv": "Korean Language"}'
    cmu_movies.loc[25679, "Movie languages"] = '{"/m/05qqm": "Polish Language", "/m/0cjk9": "Ukrainian Language", "/m/0880p": "Yiddish Language", "/m/04306rv": "German Language"}'
    cmu_movies.loc[30562, "Movie languages"] = '{"/m/02h40lc": "English Language", "/m/06b_j": "Russian Language", "/m/04306rv": "German Language"}'
    cmu_movies.loc[68137, "Movie languages"] = '{"/m/02hwyss": "Turkish Language", "/m/04306rv": "German Language"}'
    if len(cmu_movies[cmu_movies["Movie languages"].str.contains("\\\\ud")]) == 0:
        print("✅ Removed Deseret characters")
    else:
        print("❌ Failed to remove Deseret characters")

    try: 
        cmu_movies['Movie release Year'] = cmu_movies['Movie release date'].str.split('-').str[0].astype('Int64')
        cmu_movies['Movie release Month'] = cmu_movies['Movie release date'].str.split('-').str[1].astype('Int64')
        cmu_movies['Movie release Day'] = cmu_movies['Movie release date'].str.split('-').str[2].astype('Int64')
        cmu_movies.drop(columns=['Movie release date'], inplace=True)
        print("✅ Movie release date splitted to three columns: Movie release Year, Movie release Month, Movie release Day")

        # https://en.wikipedia.org/wiki/Hunting_Season_(2010_film)
        # https://en.wikipedia.org/?curid=29666067
        cmu_movies.loc[cmu_movies["Movie release Year"] == 1010, "Movie release Year"] = 2010
        print("✅ Fixed 'Hunting Season' release year 1010 => 2010")
    except:
        print("❌ Failed to split Movie release date")
        print("❌ Failed to fix 'Hunting Season' release year 1010 => 2010")

    try:
        cmu_movies['parsed languages'] = cmu_movies['Movie languages'].apply(ast.literal_eval)
        cmu_movies['language codes'] = cmu_movies['parsed languages'].apply(lambda x: ','.join(list(x.keys())))
        cmu_movies['languages'] = cmu_movies['parsed languages'].apply(lambda x: ','.join([val.replace(' Language', '') for val in list(x.values())]))
        cmu_movies.drop(columns=['Movie languages', 'parsed languages'], inplace=True)

        cmu_movies['parsed countries'] = cmu_movies['Movie countries'].apply(ast.literal_eval)
        cmu_movies['countries codes'] = cmu_movies['parsed countries'].apply(lambda x: ','.join(list(x.keys())))
        cmu_movies['countries'] = cmu_movies['parsed countries'].apply(lambda x: ','.join(list(x.values())))
        cmu_movies.drop(columns=['Movie countries', 'parsed countries'], inplace=True)

        cmu_movies['parsed genres'] = cmu_movies['Movie genres'].apply(ast.literal_eval)
        cmu_movies['genres codes'] = cmu_movies['parsed genres'].apply(lambda x: ','.join(list(x.keys())))
        cmu_movies['genres'] = cmu_movies['parsed genres'].apply(lambda x: ','.join(list(x.values())))
        cmu_movies.drop(columns=['Movie genres', 'parsed genres'], inplace=True)

        cmu_movies.drop(columns=['language codes', 'countries codes', 'genres codes'], inplace=True)
        cmu_movies.rename(columns={
            'languages': 'Movie languages',
            'countries': 'Movie countries',
            'genres': 'Movie genres'
        }, inplace=True)

        print("✅ Seperated freebase identifiers from Movie Languages, Movie Countries and Movie Genres")

        cmu_movies.loc[cmu_movies['Movie languages'] == 'Hariyani', 'Movie languages'] = 'Haryanvi'
        cmu_movies['Movie languages'] = cmu_movies['Movie languages'].str.replace('Hariyani,', '')
        print("✅ Replaced Hariyani with Haryanvi")

        cmu_movies.loc[cmu_movies['Wikipedia movie ID'] == 16301022, 'Movie languages'] = cmu_movies.loc[cmu_movies['Wikipedia movie ID'] == 16301022, 'Movie languages'].str.replace('Saami, ', '')
        cmu_movies.loc[cmu_movies['Movie languages'].str.contains('Saami'), 'Movie languages'] = cmu_movies['Movie languages'].str.replace('Saami', 'Sami')
        print("✅ Replaced Saami with Sami")


    except:
        print("❌ Failed to seperate freebase identifiers from Movie Languages, Movie Countries and Movie Genres")
        print("❌ Failed to replace Hariyani with Haryanvi")
        print("❌ Failed to replace Saami with Sami")

    # could also drop Freebase Movie ID if not needed

    return cmu_movies

def preprocess_cmu_characters(cmu_characters: pd.DataFrame) -> pd.DataFrame:
    print("Preprocess logs:")
    try:
        cmu_characters['Movie release Year'] = cmu_characters['Movie release date'].str.split('-').str[0].astype('Int64')
        cmu_characters['Movie release Month'] = cmu_characters['Movie release date'].str.split('-').str[1].astype('Int64')
        cmu_characters['Movie release Day'] = cmu_characters['Movie release date'].str.split('-').str[2].astype('Int64')
        cmu_characters.drop(columns=['Movie release date'], inplace=True)
        print("✅ Movie release date splitted to three columns: Movie release Year, Movie release Month, Movie release Day")
    except:
        print("❌ Failed to split Movie release date")

    try: 
        cmu_characters['Actor DOB'] = cmu_characters['Actor DOB'].str.split('T', expand=True)[0]
        cmu_characters['Actor DOB Year'] = cmu_characters['Actor DOB'].str.split('-').str[0].astype('Int64')
        cmu_characters['Actor DOB Month'] = cmu_characters['Actor DOB'].str.split('-').str[1].astype('Int64')
        cmu_characters['Actor DOB Day'] = cmu_characters['Actor DOB'].str.split('-').str[2].astype('Int64')
        cmu_characters.drop(columns=['Actor DOB'], inplace=True)
        print("✅ Actor DOB splitted to three columns: Actor DOB Year, Actor DOB Month, Actor DOB Day")
    except:
        print("❌ Failed to split Actor DOB date")

    try:
        cmu_characters.drop(columns=['Freebase actor ID', 'Freebase character ID'], inplace=True)
        print("✅ Dropped Freebase character/actor map ID and Freebase character ID")
    except:
        print("❌ Failed to drop Freebase character/actor map ID and Freebase character ID")

    # could also drop Freebase Movie ID and Freebase character/actor map ID if not needed

    return cmu_characters

def is_numeric(x):
    if str(x) != "<NA>":
        try:
            int(x)
            return True
        except (ValueError, TypeError):
            return False
    else:
        return True

def preprocess_imdb_movies(imdb_movies: pd.DataFrame) -> pd.DataFrame:
    print("Preprocess logs:")
    try:
        numeric_filter = imdb_movies['runtimeMinutes'].apply(is_numeric)
        non_numeric_rows = imdb_movies[~numeric_filter]

        imdb_movies.loc[~numeric_filter, 'genres'] = non_numeric_rows.apply(
            lambda row: row['genres'] + ',' + row['runtimeMinutes'] if pd.notna(row['genres']) else row['runtimeMinutes'], axis=1)

        imdb_movies.loc[~numeric_filter, 'runtimeMinutes'] = pd.NA

        imdb_movies['runtimeMinutes'] = pd.to_numeric(imdb_movies['runtimeMinutes']).astype('Int64')

        print("✅ Moved genres from runtimeMinutes to genres column")
    except:
        print("❌ Failed to move genres from runtimeMinutes to genres column")
    return imdb_movies

def preprocess_movieLens_movies(movieLens_movies: pd.DataFrame) -> pd.DataFrame:
    def is_misaligned(row):
        return row['adult'] not in ['False', 'True']
    
    print("Preprocess logs:")
    try: 
        misaligned_filter = movieLens_movies.apply(is_misaligned, axis=1)
        misaligned_rows = movieLens_movies[misaligned_filter]

        for index in misaligned_rows.index:
            first_col_value = movieLens_movies.loc[index, 'adult']
            movieLens_movies.loc[index, 'belongs_to_collection':'vote_count'] = movieLens_movies.loc[index, 'belongs_to_collection':'vote_count'].shift(9, axis=0)
            movieLens_movies.loc[index, 'overview'] = first_col_value
            columns_to_na = ['adult', 'belongs_to_collection', 'budget', 'genres', 'homepage', 'id', 'imdb_id', 'original_language', 'original_title']
            movieLens_movies.loc[index, columns_to_na] = pd.NA
        
        print("✅ Aligned bad rows")

    except:
        print("❌ Failed to align bad rows")

    return movieLens_movies