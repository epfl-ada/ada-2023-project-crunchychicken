# NLP Pipelines Explained

The goal is to extract latent personas from the [CMU movie summaries](https://www.cs.cmu.edu/~ark/personas/#:~:text=Dataset%20%5B46%20M%5D%20and%20readme%3A%2042%2C306%20movie%20plot%20summaries) using a similar approach as described in [*Learning Latent Personas of Film Characters*](https://www.cs.cmu.edu/~dbamman/pubs/pdf/bamman+oconnor+smith.acl13.pdf) by David Bamman Brendan O’Connor Noah A. Smith. 


## 1st Approach: Stanford CoreNLP-processed summaries from CMU Movie Summary Corpus

The CMU Movie Summary Corpus dataset contained a supplement: [Stanford CoreNLP-processed summaries (628 MB)](https://www.cs.cmu.edu/~ark/personas/#:~:text=Supplement%3A%20Stanford%20CoreNLP%2Dprocessed%20summaries%20%5B628%20M%5D). This tar archive contains 42'306 `.xml.gz` files, each corresponding to a movie summary processed through the Stanford CoreNLP pipeline (including tagging, parsing, NER, and coreference resolution).

The files have the following XML structure:
```
root
│ document
│ │ sentences
│ │ │ sentence id
│ │ │ │ tokens
│ │ │ │ │ token id
│ │ │ │ │ │ word
│ │ │ │ │ │ lemma
│ │ │ │ │ │ char offset begin
│ │ │ │ │ │ char offset end
│ │ │ │ │ │ POS
│ │ │ │ │ │ NER
│ │ │ │ parse
│ │ │ │ basic-dependencies
│ │ │ │ │ dep
│ │ │ │ │ │ governor
│ │ │ │ │ │ dependent
│ │ │ │ collapsed-dependencies
│ │ │ │ │ dep
│ │ │ │ │ │ governor
│ │ │ │ │ │ dependent
│ │ │ │ collapsed-ccprocessed-dependencies
│ │ │ │ │ dep
│ │ │ │ │ │ governor
│ │ │ │ │ │ dependent
│ │ coreference
│ │ │ coreference
│ │ │ │ mention
│ │ │ │ │ sentence
│ │ │ │ │ start
│ │ │ │ │ end
│ │ │ │ │ head
```

[XML to Dataframes (2013).ipnyb](https://github.com/epfl-ada/ada-2023-project-crunchychicken/blob/main/pipelines/XML%20to%20Dataframes%20(2013).ipynb) parses the XML files and saves the NLP annotations to four dataframes: `tokens_df`, `dependencies_df`, `parses_df` and `coref_df`:

- `tokens_df`

| movie_id | sentence_id | token_id | word | lemma | COB | COE | POS | NER |
|----------|-------------|----------|------|-------|-----|-----|-----|-----|
| 10000053 | 1           | 1        | Fur  | Fur   | 0   | 3   | NNP | O   |

- `dependencies_df`

| movie_id | sentence_id | dependency_class | dependency_type | governor_id | governor_word | dependent_id | dependent_word |
|----------|-------------|------------------|-----------------|-------------|---------------|--------------|----------------|
| 10000053 | 1           | basic            | nn              | 6           | te            | 1            | Fur            |


- `parses_df`

| movie_id | sentence_id | parse                                         |
|----------|-------------|-----------------------------------------------|
| 10000053 | 1           | (ROOT (S (NP (NNP Fur) (NNP trapper) (NNP...  |


- `coref_df`

| movie_id | sentence_id | start | end | head | representative |
|----------|-------------|-------|-----|------|----------------|
| 10000053 | 1           | 3     | 6   | 5    | True           |

Then, [Annotations to Personas (2013).ipnyb](https://github.com/epfl-ada/ada-2023-project-crunchychicken/blob/main/pipelines/Annotations%20to%20Personas%20(2013).ipynb), using these dataframes, generates a bag-of-words matrix $(movie_{id}, character, r, w)$, where $r$ is of {agent verb, patient verb, attribute} and $w$ the lemma form the word associated to the character. We obtain the *characters dataframe*.

| movie_id | character | r | w | 
|----------|-----------|---|---|
| 11784534 | Ingrid Bergman | attribute | Ingrid |


![2013 Explanation Image](https://i.postimg.cc/5yZsSVFd/image-2023-12-12-213128256.png)

## 2nd Approach: Annotating with Stanford CoreNLP 4.5.5
The first approach used annotations generated in 2012 with an older and less accurate version of Stanford's CoreNLP Pipeline. We decided to annotate the movie summaries using the [latest CoreNLP Pipeline](https://stanfordnlp.github.io/CoreNLP/) (version 4.5.5). A notable enhancement is the use of the [neural system for coreference](https://github.com/clarkkev/deep-coref), the most accurate of the 3 systems:

| System        | Language | Preprocessing Time | Coref Time | Total Time | F1 Score |
|---------------|----------|--------------------|------------|------------|----------|
| Deterministic | English  | 3.87s              | 0.11s      | 3.98s      | 49.5     |
| Statistical   | English  | 0.48s              | 1.23s      | 1.71s      | 56.2     |
| Neural        | English  | 3.22s              | 4.96s      | 8.18s      | 60.0     |

Table from: https://stanfordnlp.github.io/CoreNLP/coref.html (accessed 13.12.2023)

[Create New Annotations (2023).ipnyb](https://github.com/epfl-ada/ada-2023-project-crunchychicken/blob/main/pipelines/Create%20New%20Annotations%20(2023).ipynb) implements the pipeline to annotate all the movie plot summaries using CoreNLP 4.5.5 and saving the annotations to individual text files: nlp_movie_330.txt, nlp_movie_333.txt, ...

[Text to Dataframes (2023).ipnyb](https://github.com/epfl-ada/ada-2023-project-crunchychicken/blob/main/pipelines/Text%20to%20Dataframes%20(2023).ipynb) parses the generated text files and saves the NLP annotations to Pandas dataframes: 

- df_sentences
- df_tokens
- df_constituency_parse
- df_binary_parse
- df_sentiment_tree
- df_dependencies
- df_entities
- df_coreference

[Annotations to Personas (2023).ipnyb](https://github.com/epfl-ada/ada-2023-project-crunchychicken/blob/main/pipelines/Annotations%20to%20Personas%20(2023).ipynb), similarly to the first approach, we obtain the *characters dataframe*.

![2023 Explanation Image](https://i.postimg.cc/1zfR9GNm/image-2023-12-13-163516199.png)
