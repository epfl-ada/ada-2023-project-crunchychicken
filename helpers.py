from typing import Union, Iterator
import wikipedia
from wikipedia import PageError, DisambiguationError
import requests
import pandas as pd
import tqdm
from time import sleep

def batched(it, sz: int):
    """Generator for retrieving batches from an iterator."""

    start = 0
    while start + sz < len(it):
        yield it[start:start+sz]
        start += sz
    yield it[start:]

def crawl_wikipedia(pageid: Union[int, str]) -> dict:
    """
    Extract data from the Wikipedia page of the movie.

    Args:
        pageid: Wikipedia page ID or the movie.
    """

    # Fetch the Wikipedia page
    try:
        wikipedia_page = wikipedia.page(pageid=pageid)
    except:
        return None

    # Check external URLs
    imdb = None
    for url in wikipedia_page.references[::-1]:
        # IMDb ID
        if imdb is None and 'imdb.com/title' in url:
            imdb = url.split('imdb.com/title/')[1].split('/')[0]
            if imdb[:2] != 'tt':
                imdb = None
        # Box Office Mojo ID (needs improvement)
        # if bomojo_id is None and 'boxofficemojo.com/movies' in url:
            # bomojo_id = [item.split('=')[1] for item in url.split('/')[-1].split('.')[0].split('?') if item.split('=')[0] == 'id'][0]

    # Put to gether all the info
    out = {
        'imdb': imdb,
    }

    return out

WIKIDATA_API_URL = 'https://query.wikidata.org/sparql'

Q_WIKIDATA_MATCH_ATTR = """
SELECT ?attr ?imdbid WHERE {
  ?item wdt:P345 ?imdbid .
  ?item %s ?attr
  FILTER(?attr IN (%s))
}
"""

WIKIDATA_ATTRIBUTES = {
    'freebase': 'wdt:P646',
    'imdb': 'wdt:P345',
}

def crawl_wikidata(values: list[str], by: str = 'freebase') -> list[list[str]]:
    """
    Queries Wikidata to get info about the movie by matching one attribute.

    Args:
        values: The values to match the movie with.
        by: The name of the attribute to match the values on.
    """

    # Build and send query
    query = Q_WIKIDATA_MATCH_ATTR % (WIKIDATA_ATTRIBUTES[by], ', '.join([f"'{val}'" for val in values]))
    for _ in range(10):
        r = requests.get(WIKIDATA_API_URL, params = {'format': 'json', 'query': query})
        if r.ok: break
        sleep(40)
    else:
        return []

    # Build the output
    out = [
        {
            by: binding['attr']['value'],
            'imdb': binding['imdbid']['value'],
        }
        for binding in r.json()['results']['bindings']
    ]

    return out

def extract_cmu_imdb_mapping():

    # Read the movies from the CMU dataset
    cmu_movies = pd.read_csv('data/MovieSummaries/movie.metadata.tsv', sep='\t', usecols=[0, 1], names=['wikipedia', 'freebase'])

    # Get mapping by crawling Wikipedia
    mapping_01 = []
    for wp_id in tqdm.tqdm(cmu_movies.wikipedia):
        try:
            res = crawl_wikipedia(pageid=wp_id)
        except Exception as e:
            res = None
        mapping_01.append({'wikipedia': wp_id, 'imdb': res['imdb'] if res else None})
    mapping_01 = pd.DataFrame(mapping_01).dropna()
    mapping_01.to_csv('generated/wp2imdb_01.csv', index=False)

    # Get mapping by querying Wikidata
    # mapping_02 = []
    # sz = 200
    # for batch in tqdm.tqdm(batched(cmu_movies.freebase, sz=sz), total=(len(cmu_movies.freebase)//sz + 1)):
    #     mapping_02.extend(crawl_wikidata(values=batch.to_list(), by='freebase'))
    # mapping_02 = pd.DataFrame(mapping_02).dropna()
    # mapping_02.to_csv('generated/wp2imdb_02.csv', index=False)
    mapping_02 = pd.read_csv('generated/wp2imdb_02.csv')  # TMP

    # Aggregate the two and store
    mapping = pd.merge(left=mapping_01, right=mapping_02, on='imdb', how='outer')
    mapping.to_csv('generated/wp2imdb.csv', index=False)

    print('Done!')
