import pandas as pd
import os
from pathlib import Path

from helpers.readers import FILES, read_dataframe

# Script to convert .csv and .tsv of CMU/ IMDb/ MovieLens/ to parquet with brotli compression

cmu_movies_col_names = [
    "Wikipedia movie ID", 
    "Freebase movie ID", 
    "Movie name", 
    "Movie release date", 
    "Movie box office revenue", 
    "Movie runtime", 
    "Movie languages", 
    "Movie countries", 
    "Movie genres",
]

cmu_characters_col_names = [
    "Wikipedia movie ID",
    "Freebase movie ID",
    "Movie release date",
    "Character name",
    "Actor DOB",
    "Actor gender",
    "Actor height",
    "Actor ethnicity",
    "Actor name",
    "Actor age at movie release",
    "Freebase character/actor map ID",
    "Freebase character ID",
    "Freebase actor ID",
]

"""
cmu_summaries_col_names = [
    "Wikipedia movie ID", 
    "Plot Summary"
]
cmu_name_clusters_col_names = ['Character name', 'Freebase character/actor map ID']
"""

def check_folder(subdir, do_CMU, do_IMDb, do_MovieLens):
    if ("CMU" in subdir) and do_CMU:
        return True
    elif ("IMDb" in subdir) and do_IMDb:
        return True
    elif ("MovieLens" in subdir) and do_MovieLens:
        return True
    else:
        return False   
    
def get_key_for_file(file_name, files_dict):
    for key, value in files_dict.items():
        # Extract the file name part from the path
        if Path(value).name == file_name:
            return key
    return None

def convert_files_to_parquet(do_CMU=True, do_IMDb=True, do_MovieLens=True):
    
    script_dir = os.path.dirname(__file__) 
    data_dir = os.path.abspath(os.path.join(script_dir, 'data'))
    #data_dir = os.path.abspath(os.path.join(script_dir, '..', 'data'))
    print(f"Found data path: {data_dir}")

    for subdir, dirs, files in os.walk(data_dir):
        for file in files:
                if (file.endswith('.csv') or file.endswith('.tsv')) and (check_folder(subdir, do_CMU, do_IMDb, do_MovieLens)):    
                    #print(file, get_key_for_file(file, FILES))
                    print(f"Generating parquet for {file}")
                    key = get_key_for_file(file, FILES)
                    usecols = None
                    if key == "cmu/movies":
                        usecols = cmu_movies_col_names
                    elif key == "cmu/characters":
                        usecols = cmu_characters_col_names
                    #print(file, subdir)
                    file_base, _ = os.path.splitext(file)
                    parquet_path = os.path.join(subdir, file_base + '.parquet')
                    print(f"Saving to: {parquet_path}")
                    dataframe = read_dataframe(key, usecols=usecols, preprocess=True, convert_downcast=True)
                    dataframe.to_parquet(parquet_path, compression="brotli")           

    print("Conversion complete.")

if __name__ == "__main__":
    convert_files_to_parquet(do_CMU=True, do_IMDb=True, do_MovieLens=True)