# Deliverables: GitHub repository with the following (TO DELETE)
- Readme.md file containing the detailed project proposal (up to 1000 words). Your README.md should contain:
  - Title
  - Abstract: A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?
  - Research Questions: A list of research questions you would like to address during the project.
  - Proposed additional datasets (if any): List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.
  - Methods
  - Proposed timeline
  - Organization within the team: A list of internal milestones up until project Milestone P3.
  - Questions for TAs (optional): Add here any questions you have for us related to the proposed project.
- Notebook containing initial analyses and data handling pipelines. We will grade the correctness, quality of code, and quality of textual descriptions.

# TODO: Complete the final readme for P2
# [TITLE OF THE PROJECT]
- Director's choices on the destiny of a film
- The power of directing choices on film success

## Abstract
*A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?*

## Research Questions (*goal is to convince TA idea has value and is feasible*)
*A list of research questions you would like to address during the project.*

*SEPEHR: I think in this part we need to list fewer questions with more description on each of them. We can combine the questions below or only keep the most interesting ones.*


1) Do directors who work in multiple countries exhibit different styles in each context?
2) Is there a correlation between a director's critical success and the evolution of their style?
3) Are more successfull directors more often specialized in a particular genre, using particular characters, or there is a lot of diversity in their work.
4) Are directors successfull because they cast popular actors?
5) How to rate the directors?
6) How diverse the directors are in their character choices?
7) Can we find some directors that decided to cast, for their next film, only very popular actors at the time being ?
8) How active are the directors in terms of movie production ?
9) To what extent do directors experiment with their style over the course of their career, and are there periods of experimentation followed by periods of consistency?
10) Are the director always worked with same crew or not? Do it effect the success of movie(by ratings)?
11) Can we spot bright underrated directors who are in the early stages of their career? We will try to do that by analyzing the movie genre, the plot summary, the movie characters, the profile of the director (e.g., age, gender, country of origin) and the profile of the cast and crew of their movies.

## Proposed additional datasets
### Stanford CoreNLP-processed summaries
The dataset is available online [here](https://www.cs.cmu.edu/~ark/personas/data/corenlp_plot_summaries.tar).
*Explain what we can get from this dataset and why we are using it.*

### IMDb Non commercial datasets
The dataset is available online [here](https://developer.imdb.com/non-commercial-datasets/). Using this dataset, we can enrich the metadata about the movies in the CMU dataset, as well as the cast and crew of a movie. The major challenge for using this dataset is merging it with the CMU dataset. We have been able to merge them successfully by crawling Wikipedia and querying Wikidata to get the corresponding IMDb movie ID for each movie present in the CMU dataset. Next step is to also find such a mapping between the actors and actresses in the CMU dataset and their corresponding ID in the IMDb dataset, which is less critical.

## Methods

### NLP:
Following [*Learning Latent Personas of Film Characters* from David Bamman Brendan O’Connor Noah A. Smith](https://www.cs.cmu.edu/~dbamman/pubs/pdf/bamman+oconnor+smith.acl13.pdf), we first parsed all the XML files using *insert link to notebook* to obtain 4 dataframes: tokens, dependencies, coreference, parses. Using tokens and dependencies we can extract for characters present in movie plot summaries the agent actions, patient actions and their attributes, then we generated bags of words and used a [LDA](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) to find the typical personas *link notebook*. Since 2013, Stanford's coreNLP annotation pipeline has evolved, we decided to annoate the plots using the latest version of [Stanford coreNLP](https://stanfordnlp.github.io/CoreNLP/) to obtain better NER (Named Entity Recognition), allowing a more accurate identification of characters inside each movie plot. The coreNLP 4.5.5 pipeline code can be found here *insert link*. We use tokens, dependencies and an additional dataframe: Entity Mentions, that has the identified character per sentence of movie plot, this allows to have well defined characters and get more accurate typical personas using LDA.  

### Success and popularity of a movie
We measure the success of a movie by one or a combination of the IMDb ratings, the number of rates, the Box Office revenue, and possibly the awards and nominations of the movie. Will create a *success score* and a *popularity score* for each movie. We will decide on the exact definition of these scores based on their distribution and their representativeness of what we intend to measure.

### Success and popularity of a director
The most basic idea would be to calculate the average success and popularity scores of the movies of a director. A more elegant approach can be to count the number of successful or popular movies of the director, by applying a threshold on the scores. This way, we will take into account that for a director to be successful, only a couple of successful movies is enough. Taking Martin Scorcese for instance, movies like Casino, Goodfellas, and Taxi Driver are enough to make him a successful director, and for such directors, we should get a *success score* close to maximum, so why impinging his score with taking into account the success of movies like Made in Milan or The Family which nobody knows about?

### Similarity / representation of the plot summaries
*Maybe some words about how we plan to do that? Remove it otherwise.*


## Proposed timeline for P3
*List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.*

- Before xx.xx.2023: Fix the definition of success and popularity metrics.
- Before xx.xx.2023: ...


## Organization within the team
*A list of internal milestones up until project Milestone P3.*

*Sepehr: I think here they mean how we plan to split the work for P3, not what we did for P2. So we need to change this part.*

- Sepehr: IMDb
- Romain: IMDb
- Clemence: IMDb
- Arthur: NLP
- Chang: NLP

## Questions for TAs (optional)
*Add here any questions you have for us related to the proposed project.*


## Authors
Group: CrunchyChicken
- [Chang Chun-Tzu](mailto:chun-tzu.chang@epfl.ch) (SCIPER 351986)
- [Arthur Lamour](mailto:arthur.lamour@epfl.ch) (SCIPER 300443)
- [Clémence Mayaux](mailto:clemence.mayaux@epfl.ch) (SCIPER 300278)
- [Sepehr Mousavi](mailto:sepehr.mousavi@epfl.ch) (SCIPER 338673)
- [Romain Rochepeau](mailto:romain.rochepeau@epfl.ch) (SCIPER 300574)
