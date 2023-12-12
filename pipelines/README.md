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

Then, using these dataframes, we want to generate a bag-of-words matrix $(movie_id, character, r, w)$, where $r$ is of $\{$agent verb, patient verb, attribute$\}$ and $w$ the lemma form the word associated to the character.

| movie_id | character | r | w | 
|----------|-----------|---|---|
| 11784534 | Ingrid Bergman | attribute | Ingrid |


![2013 Explanation Image](https://i.postimg.cc/5yZsSVFd/image-2023-12-12-213128256.png)

## 2nd Approach: 
