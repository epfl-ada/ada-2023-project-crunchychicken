# ada-2023-project-crunchychicken

# TODO
- read each others ideas and see how we can implement the chosen idea with the dataframes we have
- check how to use wiki and freebase id with wikidata
- Optional: check for a scrapper on wikidata + IMDb or other
- [ADA Instructions for P2](https://github.com/epfl-ada/ada-2023-project-crunchychicken/blob/main/instructions.md)

# Dataset: CMU Movie Summary Corpus
![dataframes visualization](https://i.postimg.cc/8zVnpKQS/image-2023-11-04-173843862.png)

- [CMU Movie Summary Corpus webpage](https://www.cs.cmu.edu/~ark/personas/)
- [Corrected version of the CMU Movie Summary Corpus ReadMe](https://github.com/epfl-ada/ada-2023-project-crunchychicken/blob/main/cmu_readme.md)
- [CMU Movie Summary Corpus paper: Learning Latent Personas of Film Characters by David Bamman, Brendan O'Connor, and Noah A. Smith](https://www.cs.cmu.edu/~dbamman/pubs/pdf/bamman+oconnor+smith.acl13.pdf) 
- Main dataset: [plot summaries and aligned metadata from Freebase](https://www.cs.cmu.edu/~ark/personas/data/MovieSummaries.tar.gz) (46MB)
- Secondary dataset: [Stanford CoreNLP-processed summaries](https://www.cs.cmu.edu/~ark/personas/data/corenlp_plot_summaries.tar) (628MB)

## Data Placement Instructions
⭐Download the data from **[here]([https://drive.google.com/file/d/1-vKHQjKUtgpsMt1MzV3lcBp7WIcLA1YO/view?usp=sharing](https://drive.google.com/drive/u/2/folders/1xeeJxvuIyu738Bd2ev_Ex49Af8lDv9pw))**⭐ <br> 
Put all the data files inside a subfolder named `Dataset/`, like this:
<pre>
project_root/
│
├── P2.ipynb
│
├── Dataset/
│   ├── coref.parquet
│   ├── dependencies.parquet
│   ├── parses.parquet
│   ├── tokens.parquet
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

### Secondary dataset after processing
- dependencies.parquet: 34199068 rows (225 MB) 
- parses.parquet: 665586 rows (89 MB)
- tokens.parquet: 14905203 rows (177 MB)

#### XML file format
<pre>
sentences
│ sentence id
│ │ tokens
│ │ │ token id
│ │ │ │ word
│ │ │ │ lemma
│ │ │ │ char offset begin
│ │ │ │ char offset end
│ │ │ │ POS
│ │ │ │ NER
│ │ parse
│ │ basic-dependencies
│ │ │ dep
│ │ │ │ governor
│ │ │ │ dependent
│ │ collapsed-dependencies
│ │ │ dep
│ │ │ │ governor
│ │ │ │ dependent
│ │ collapsed-ccprocessed-dependencies
│ │ │ dep
│ │ │ │ governor
│ │ │ │ dependent
</pre>

#### Stanford coreNLP
[website](https://stanfordnlp.github.io/CoreNLP/) <br>
[NER](https://stanfordnlp.github.io/CoreNLP/ner.html#description) <br>
[POS](https://stanfordnlp.github.io/CoreNLP/pos.html#description) <br>
[POS codes](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html) <br>
[PARSE](https://stanfordnlp.github.io/CoreNLP/parse.html#description) <br>
[Dependencies](https://stanfordnlp.github.io/CoreNLP/depparse.html#description) <br>
[Dependencies manual for dep class and dep types](https://downloads.cs.stanford.edu/nlp/software/dependencies_manual.pdf) <br>
[Dependencies literature](https://nlp.stanford.edu/software/stanford-dependencies.html)

# Authors
Group: CrunchyChicken
- [Sepehr Mousavi](mailto:sepehr.mousavi@epfl.ch) (SCIPER 338673)
- [Arthur Lamour](mailto:arthur.lamour@epfl.ch) (SCIPER 300443)
- [Romain Rochepeau](mailto:romain.rochepeau@epfl.ch) (SCIPER 300574)
- [Chang Chun-Tzu](mailto:chun-tzu.chang@epfl.ch) (SCIPER 351986)
- [Clémence Mayaux](mailto:clemence.mayaux@epfl.ch) (SCIPER 300278)
