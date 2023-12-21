import pandas as pd
import ast
import re
import seaborn as sns


# Discrete
PALETTE_D = sns.color_palette([sns.color_palette("colorblind")[i] for i in [4, 2, 0, 1, 3, 5, 7, 8, 6, 9]])
# Continuous
PALETTE_C = sns.color_palette("dark:#5A9_r", as_cmap=True)

####################### Utility function for external.py #######################
def batched(it, sz: int):
    """Generator for retrieving batches from an iterator."""

    start = 0
    while start + sz < len(it):
        yield it[start:start+sz]
        start += sz
    yield it[start:]

########## Utility function to ensure merge as Pandas requires int64  ##########

def cast_back_to_int64(df: pd.DataFrame, col_name: str) -> pd.DataFrame:
    df[col_name] = df[col_name].astype('int64')
    return df

def downcast_int64(df: pd.DataFrame, col_name: str) -> pd.DataFrame:
    df[col_name] = pd.to_numeric(df[col_name], downcast='integer')
    return df

######### Function to downcast the dtypes of dataframes to save space  #########

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

############################# Preprocess functions #############################

def preprocess_cmu_movies(cmu_movies: pd.DataFrame) -> pd.DataFrame:
    cmu_movies.loc[46808, 'Movie countries'] = '{"/m/03rk0": "India"}'
    cmu_movies.loc[67202, 'Movie countries'] = '{"/m/03rk0": "India"}'
    cmu_movies.loc[67202, 'Movie languages'] = '{"/m/0999q": "Malayalam Language"}'
    cmu_movies.loc[72685, 'Movie countries'] = '{"/m/084n_": "Weimar Republic", "/m/0345h": "Germany"}'
    print("Preprocess logs cmu_movies:")
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

        cmu_movies.loc[cmu_movies['Wikipedia movie ID'] == 27814939, 'Movie countries'] = 'United Kingdom'
        print("✅ The Flying Scotsman (1929 film) country fix")

        cmu_movies.loc[cmu_movies['Wikipedia movie ID'] == 15657123, 'Movie countries'] = 'Ukrainian SSR, Soviet Union'
        print("✅ Ukranian SSR fix")

        cmu_movies.loc[cmu_movies['Wikipedia movie ID'] == 35851069, 'Movie countries'] = 'France,Palestinian territories,Israel,Netherlands'
        print("✅ Palestinian territories fix")


    except:
        print("❌ Failed to seperate freebase identifiers from Movie Languages, Movie Countries and Movie Genres")
        print("❌ Failed to replace Hariyani with Haryanvi")
        print("❌ Failed to replace Saami with Sami")
        print("❌ Failed The Flying Scotsman (1929 film) country fix")
        print("❌ Failed Ukranian SSR fix")
        print("❌ Failed Palestinian territories fix")

    try:
        # https://en.wikipedia.org/?curid=10815585
        cmu_movies.loc[cmu_movies['Wikipedia movie ID'] == 10815585, 'Movie runtime'] = 94
        cmu_movies.loc[cmu_movies['Wikipedia movie ID'] == 21689271, 'Movie runtime'] = 85
        cmu_movies.loc[cmu_movies['Wikipedia movie ID'] == 21689271, 'Movie release Year'] = 1934
        cmu_movies.loc[cmu_movies['Wikipedia movie ID'] == 36136594, 'Movie runtime'] = 64
        cmu_movies.loc[cmu_movies['Wikipedia movie ID'] == 24873771, 'Movie runtime'] = 145
        cmu_movies.loc[cmu_movies['Wikipedia movie ID'] == 24873771, 'Movie release Year'] = 2012
        cmu_movies.loc[cmu_movies['Wikipedia movie ID'] == 2551150, 'Movie runtime'] = 86
        cmu_movies.loc[cmu_movies['Wikipedia movie ID'] == 11039905, 'Movie runtime'] = 153
        cmu_movies.loc[cmu_movies['Wikipedia movie ID'] == 11829180, 'Movie runtime'] = 1315
        cmu_movies.loc[cmu_movies['Wikipedia movie ID'] == 6012645, 'Movie runtime'] = float('nan')
        print("✅ Fixed huge runtimes")

        series_wiki_ids_to_remove = [18983351, 25930191, 33483307, 1348747] # series
        large_wiki_ids_to_remove = [14545195, 884506, 884435, 32441022, 884492, 11829180, 25345684] # over 1000 minutes movies
        wiki_ids_to_remove = series_wiki_ids_to_remove + large_wiki_ids_to_remove
        cmu_movies = cmu_movies[~cmu_movies['Wikipedia movie ID'].isin(wiki_ids_to_remove)]
        print("✅ Removed series")
    
    except:
        print("❌ Fixed huge runtimes")
        print("❌ Removed series")

    # could also drop Freebase Movie ID if not needed

    return cmu_movies

def preprocess_cmu_characters(cmu_characters: pd.DataFrame) -> pd.DataFrame:
    print("Preprocess logs cmu_characters:")
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

# Utility function for preprocess_cmu_scraped
def parse_runtime(runtime):
    if pd.isna(runtime):
        return None
    
    # https://en.wikipedia.org/wiki/Reel
    if 'reels' in runtime:
        match = re.search(r'(\d+) reels', runtime)
        if match:
            return int(match.group(1)) * 10
        
    if 'reel' in runtime:
        match = re.search(r'(\d+) reel', runtime)
        if match:
            return int(match.group(1)) * 10

    if 'feet' in runtime:
        match = re.search(r'(\d+) feet', runtime)
        if match:
            return int(match.group(1)) / 1000 * 11

    if 'hour' in runtime or 'hr' in runtime:
        hours = re.search(r'(\d+) hour', runtime)
        hours = int(hours.group(1)) if hours else 0
        minutes = re.search(r'(\d+) min', runtime)
        minutes = int(minutes.group(1)) if minutes else 0
        return hours * 60 + minutes

    if 'Min' in runtime:
        match = re.search(r'(\d+) Min', runtime)
        if match:
            return int(match.group(1))
        
    if 'seconds' in runtime:
        match = re.search(r'(\d+) seconds', runtime)
        if match:
            return int(match.group(1)) / 60
        
    if 'secs' in runtime:
        match = re.search(r'(\d+) secs', runtime)
        if match:
            return int(match.group(1)) / 60
    
    if 'minute' in runtime or 'min' in runtime or "'" in runtime:
        minute_patterns = [r'(\d+)\s*min', r'(\d+)\s*minute', r"(\d+)'"]
        for pattern in minute_patterns:
            match = re.search(pattern, runtime)
            if match:
                return int(match.group(1))
            
    if ':' in runtime:
        try:
            minutes, seconds = runtime.split(':')
            return int(minutes) + int(seconds) / 60
        except ValueError:
            pass
        
    hour_minute_patterns = [r'(\d+)h\s*(\d+)m', r'(\d+)\.(\d+)']
    for pattern in hour_minute_patterns:
        match = re.search(pattern, runtime)
        if match:
            hours, minutes = match.groups()
            return int(hours) * 60 + int(minutes)

    if ':' in runtime and runtime.count(':') == 1:
        try:
            minutes, seconds = runtime.split(':')
            return int(minutes) + int(seconds) / 60
        except ValueError:
            pass  
        
    if ':' in runtime and runtime.count(':') == 2:
        try:
            hours, minutes, seconds = runtime.split(':')
            return int(hours) * 60 + int(minutes) + int(seconds) / 60
        except ValueError:
            pass

    return None

# Utility function for preprocess_cmu_scraped
def currency_symbol_to_code(text):
    currency_map = {
        '€': 'EUR', 'eur': 'EUR', 'euros': 'EUR',
        '$': 'USD', 'USD': 'USD', 'dollar': 'USD',
        '₹': 'INR', 'Rs': 'INR', 'Rp': 'INR', 'rupee': 'INR',
        '£': 'GBP', 'GPD': 'GBP',
        '¥': 'CNY', 'renminbi': 'CNY', 'yuan': 'CNY',
        '₽': 'RUB', 'RUR': 'RUB', 'rubles': 'RUB', 'RUB': 'RUB',
        'IRR': 'IRR', 'rial': 'IRR', 'Rial': 'IRR', 'rials': 'IRR',
        'real': 'BRL',
        'SEK' : 'SEK',
        '₱': 'PHP', 
        '₤': 'ITL', 'L.': 'ITL', 'Italian lire' : 'ITL',
        'yen': 'JPY', 'Yen' : 'JPY',
        'CZK' : 'CZK',
        'AUD' : 'AUD',
    }
    for key, value in currency_map.items():
        if key in text:
            return value
    return None

# Utility function for preprocess_cmu_scraped
def convert_million(value):
    try:
        return float(value) * 1_000_000
    except ValueError:
        return None

# Utility function for preprocess_cmu_scraped
def convert_billion(value):
    try:
        return float(value) * 1_000_000_000
    except ValueError:
        return None

# Utility function for preprocess_cmu_scraped
def convert_crore(value):
    try:
        return float(value) * 10_000_000
    except ValueError:
        return None

# Utility function for preprocess_cmu_scraped
def parse_number(value):
    try:
        return float(value.replace(',', ''))
    except ValueError:
        try:
            return float(value.replace('.', '').replace(',', '.'))
        except ValueError:
            return None

# Utility function for preprocess_cmu_scraped
def parse_revenue(revenue):
    if pd.isna(revenue):
        return None, None

    revenue = re.sub(r'(est\.|c\.)\s*', '', revenue).replace(',', '')

    currency = currency_symbol_to_code(revenue)

    match = re.search(r'(\d+(?:\.\d+)?)\s*(billion|million|crore)?', revenue, re.IGNORECASE)
    if match:
        value, multiplier = match.groups()

        if multiplier:
            if 'million' in multiplier.lower():
                value = convert_million(value)
            elif 'billion' in multiplier.lower():
                value = convert_billion(value)
            elif 'crore' in multiplier.lower():
                value = convert_crore(value)
        else:
            value = parse_number(value)

        return currency, float(value)

    return None, None

# Utility function for preprocess_cmu_scraped
def compute_profit(row):
    if (
        pd.notna(row['budget_value']) and pd.notna(row['revenue_value']) and
        row['budget_currency'] == row['revenue_currency'] and
        row['budget_currency'] is not None
    ):
        profit = row['revenue_value'] - row['budget_value']
        return profit, row['budget_currency']
    else:
        return None, None

def preprocess_cmu_movies_scraped(cmu_scraped_movies: pd.DataFrame) -> pd.DataFrame:
    columns_to_drop = [
        'Directed by', 'Screenplay by', 'Story by', 
        'Based on', 'Produced by', 'Starring', 'Cinematography', 
        'Edited by', 'Music by', 'Production company', 'Distributed by'
    ]
    print("Preprocess logs cmu_movies_scraped:")
    try: 
        cmu_scraped_movies = cmu_scraped_movies.drop(columns=columns_to_drop)
        print("✅ Dropped initial screenplay related columns")
    except:
        print("❌ Failed to drop initial screenplay related columns")
    try:
        cmu_scraped_movies['runtime_minutes'] = cmu_scraped_movies['Running time'].apply(parse_runtime)
        print("✅ Parsed runtime")
    except:
        print("❌ Failed to parse runtime")
    try: 
        cmu_scraped_movies['revenue_currency'], cmu_scraped_movies['revenue_value'] = zip(*cmu_scraped_movies['Box office'].apply(parse_revenue))
        print("✅ Parsed revenue (box office)")
    except:
        print("❌ Failed to parse revenue (box office)")
    try:
        cmu_scraped_movies['budget_currency'], cmu_scraped_movies['budget_value'] = zip(*cmu_scraped_movies['Budget'].apply(parse_revenue))
        print("✅ Parsed budget")
    except:
        print("❌ Failed to parse budget")
    try:
        cmu_scraped_movies[['profit_value', 'profit_currency']] = cmu_scraped_movies.apply(compute_profit, axis=1, result_type='expand')
        print("✅ Generated movie profit")
    except:
        print("❌ Failed to generate movie profit")
    try:
        cmu_scraped_movies['release_year'] = cmu_scraped_movies['Release dates'].str.extract(r'(\d{4})')
        cmu_scraped_movies['release_year'] = pd.to_numeric(cmu_scraped_movies['release_year'], errors='coerce')
        cmu_scraped_movies['release_year'] = cmu_scraped_movies['release_year'].astype('Int64')
        print("✅ Extracted movie release year")
    except:
        print("❌ Failed to extract movie release year")

    columns_to_drop = [
        "Running time", "Budget", "Box office", "Release dates"
    ]

    try:
        cmu_scraped_movies = cmu_scraped_movies.drop(columns=columns_to_drop)
        print("✅ Dropped parsed columns")
    except:
        print("❌ Failed to drop parsed columns")
    return cmu_scraped_movies

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
    print("Preprocess logs imdb_movies:")
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
    
    print("Preprocess logs movieLens_movies:")
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
