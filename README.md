# ada-2023-project-crunchychicken

# TODO
- check how to use wiki and freebase id with wikidata
- check for a scrapper on wikidata + IMDb or other

# Dataset
**[Link to download the parsed XML datasets](https://drive.google.com/file/d/1-vKHQjKUtgpsMt1MzV3lcBp7WIcLA1YO/view?usp=sharing)**

- [Official page](https://www.cs.cmu.edu/~ark/personas/)
- [Official ReadMe](https://github.com/epfl-ada/ada-2023-project-crunchychicken/blob/main/cmu_readme.md)
- Main dataset: [CMU Movie Summary Corpus](https://www.cs.cmu.edu/~ark/personas/data/MovieSummaries.tar.gz) (46MB)
- Optional secondary dataset: [Stanford CoreNLP-processed summaries](https://www.cs.cmu.edu/~ark/personas/data/corenlp_plot_summaries.tar) (628MB)

## Data Placement Instructions
Put all the data files inside a subfolder named `Dataset/`, like this:
<pre>
project_root/
│
├── P2.ipynb
├── dependencies.parquet
├── parses.parquet
├── tokens.parquet
│
├── Dataset/
│   ├── character.metadata.tsv
│   ├── movie.metadata.tsv
│   ├── name.clusters.txt
│   ├── plot_summaries.txt
│   ├── README.txt
│   └── tvtropes.clusters.txt
│
└── XML_Dataset/
    ├── 330.xml.gz
    ├── 3271.xml.gz
    &nbsp;&nbsp;&nbsp;&nbsp;... (many more files) ...
    └── 37501922.xml.gz
</pre>

## Data size
### Main dataset
- character.metadata.tsv: 450,669 characters (40 MB) 
- movie.metadata.tsv: 81,741 movies (15 MB)
- name.clusters.txt: 970 unique character names, 2666 rows (64 KB)
- plot_summaries.txt: plot summaries of 42'306 movies, 42'303 rows (73MB)
- tvtropes.clusters.txt: 72 character types, 511 rows (57 KB)

### Secondary dataset
- dependencies.parquet: 34199068 rows (225 MB) 
- parses.parquet: 665586 rows (89 MB)
- tokens.parquet: 14905203 rows (177 MB)

# Authors
Group: CrunchyChicken
- [Sepehr Mousavi](mailto:sepehr.mousavi@epfl.ch) (SCIPER 338673)
- [Arthur Lamour](mailto:arthur.lamour@epfl.ch) (SCIPER 300443)
- [Romain Rochepeau](mailto:romain.rochepeau@epfl.ch) (SCIPER 300574)
- [Chang Chun-Tzu](mailto:chun-tzu.chang@epfl.ch) (SCIPER 351986)
- [Clémence Mayaux](mailto:clemence.mayaux@epfl.ch) (SCIPER 300278)
