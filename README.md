# Frames of success :  Diving into the brains of movie wizards

## Abstract

Stanley Kubrick is known to have at least one great movie in every major movie genre. Conversely, when you see David Fincher's name as the director of a new movie, you are almost sure that there is going to be one or more serial killers involved. The directorial approach of the most successful directors can be so different and taking the right directorial approaches early can lead a director to achieve significant success in their career, and is believed to be the main factor determining the quality of the movie. In this data analysis project, we will utilize the CMU Movie Summary Corpus, along with supplementary datasets, to examine approaches of the brightest directors from three angles: the genre of their films, the team surrounding them, and the character personas in their movies. We aim to gain a clear insight on how their decisions impact the overall success of the movie.


## Research Questions 

1. How impactful is the team surrounding the director on the success of the movie?

    Are the directors who always work with the same technical crew more successful? Are some directors successful only because they cast popular actors? Can we find some directors that decided to cast, for their next project, only very popular actors by looking at details about their previous works? Successful directors built up their renown across the industry thanks to now very popular movies, but can it also be thanks to the presence of certain individuals in their team? If yes, how frequently have they been collaborating with each other?

2. To what extent does the director's choice of movie genre affect the success of the movie?

    Are more successful directors more often specialized in a certain combination of genres? Are directors who tend to work on more diverse projects less successful? Is there a correlation between a director's critical success and the evolution of their style, regarding the choices of movie genres? To what extent do directors experiment with new genres and thematics over the course of their career, and is there a pattern of periods of experimentation followed by periods of consistency?

3. What is the impact of the director's character choices on the sucess of the movie?

    What types of characters do successful directors choose? How diverse the directors are in their character choices? Can we find very successful directors that always use the same type of characters or others that vary a lot in their personas choices? In definitive, how does this impact the movie's success?

Additional question :
 
Can we spot bright underrated directors who are in the early stages of their career?

We will try to do that by analyzing the movie genre, the plot summary, the movie characters, the profile of the director (e.g., age, gender, country of origin) and the profile of the cast and crew of their movies.


## Proposed additional datasets

### Stanford CoreNLP-processed summaries
The dataset is available online [here](https://www.cs.cmu.edu/~ark/personas/data/corenlp_plot_summaries.tar).
*Explain what we can get from this dataset and why we are using it.*

### IMDb Non commercial datasets
The dataset is available online [here](https://developer.imdb.com/non-commercial-datasets/). Using this dataset, we can enrich the metadata about the movies in the CMU dataset, as well as the cast and crew of a movie. The major challenge for using this dataset is merging it with the CMU dataset. We have been able to merge them successfully by crawling Wikipedia and querying Wikidata to get the corresponding IMDb movie ID for each movie present in the CMU dataset. Next step is to also find such a mapping between the actors and actresses in the CMU dataset and their corresponding ID in the IMDb dataset, which is less critical.

### 'TheMovies' Dataset

The dataset is available on [Kaggle](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=movies_metadata.csv). This dataset contains metadata for all 45,000 movies listed in the Full MovieLens Dataset. In it, we can retrieve some interesting information to cure as well as enrich our CMU concerning the movie runtimes, release years, production companies, as well as precious information regarding the movie's success, with some ratings and the revenue. In the dataset, 27 500~ movies are also part of our CMU Movie Corpus.

## Methods

### Success and popularity of a movie
We measure the success of a movie by one or a combination of the IMDb ratings, the number of rates, the Box Office revenue, and possibly the awards and nominations of the movie. Will create a *success score* and a *popularity score* for each movie. We will decide on the exact definition of these scores based on their distribution and their representativeness of what we intend to measure.

### Success and popularity of a director
The most basic idea would be to calculate the average success and popularity scores of the movies of a director. A more elegant approach can be to count the number of successful or popular movies of the director, by applying a threshold on the scores. This way, we will take into account that for a director to be successful, only a couple of successful movies is enough. Taking Martin Scorcese for instance, movies like Casino, Goodfellas, and Taxi Driver are enough to make him a successful director, and for such directors, we should get a *success score* close to maximum, so why impinging his score with taking into account the success of movies like Made in Milan or The Family which nobody knows about?


### Natural Language Processing
Following [*Learning Latent Personas of Film Characters* from David Bamman Brendan O’Connor Noah A. Smith](https://www.cs.cmu.edu/~dbamman/pubs/pdf/bamman+oconnor+smith.acl13.pdf), we first parsed all the XML files using *insert link to notebook* to obtain 4 dataframes: tokens, dependencies, coreference, parses. Using tokens and dependencies we can extract for characters present in movie plot summaries the agent actions, patient actions and their attributes, then we generated bags of words and used a [LDA](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) to find the typical personas *link notebook*. Since 2013, Stanford's coreNLP annotation pipeline has evolved, we decided to annoate the plots using the latest version of [Stanford coreNLP](https://stanfordnlp.github.io/CoreNLP/) to obtain better NER (Named Entity Recognition), allowing a more accurate identification of characters inside each movie plot. The coreNLP 4.5.5 pipeline code can be found here *insert link*. We use tokens, dependencies and an additional dataframe: Entity Mentions, that has the identified character per sentence of movie plot, this allows to have well defined characters and get more accurate typical personas using LDA.


## Proposed timeline for P3


| Deadline   | Question #1                                                                                                                           | Question #2                                                                              | Question #3                                                                              |
|------------|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| 3.12.2023  | 1. Finish cleaning the datasets ;<br>2. Clean & unify the codes <br> 3.Decide on success and popularity metrics.                    | Same as Q1                                                                               | Same as Q1                                                                               |
| 10.12.2023 | 1. Decide on the set of directors to study;<br>2. Decide on the definition of the "team" around the director;<br>3. Prepare the dataframes and preliminary visualizations. | 1. Prepare the Dataframes for vizsualizations <br> 2. Check the diversity of the genres per director | 1. Decide on how exactly to use the Persona's data with respect to directors<br> 2.  Prepare the dataframes and preliminary visualizations. |
| 17.12.2023 | 1. Try to address the raised research questions in detail;<br>2. Enhance the visualizations.                                            | 1. Assess the link the director's style to success<br>2. Enhance the visualizations       <br>3. Explore director's activity consistency regarding genres           | 1. Assess the director's personas choices<br>2. Link it to the success of the movies/directors                 |
| 22.12.2023 | 1. Finalize the visualizations;<br>2. Write the story and work on presentation (Github pages).                                          | Same as Q1                                                                               | Same as Q1                                                                               |


## Organization within the team

Until 3.12.2023, we will focus on Homework 2 but we will also start cleaning our datasets and trying retrieve more data, as explained in the notebook.

| Deadline   | Chang   | Arthur  | Clemence | Sepehr  | Romain  |
|------------|---------|---------|----------|---------|---------|
| 3.12.2023  | General | General | General  | General | General |
| 10.12.2023 | Q1      | Q3      | Q1       | Q2      | Q2      |
| 17.12.2023 | Q1      | Q3      | Q2-3       | Q1-2      | Q2-3      |
| 22.12.2023 | General      | General     | General       | General      | General      |

## Questions for TAs

- Our plan is to try to answer as many of the raised research questions as possible, but for the moment we are not sure which ones will give us more interesting results. Is this a good approach in your opinion? Should we focus on one of them instead?

- Are the methods clear enough ?  Or should we maybe define exact workflows for milestone P3 ?

## Authors

***CrunchyChicken* group - Advanced Data Science (CS-401) 2023**

- [Chang Chun-Tzu](mailto:chun-tzu.chang@epfl.ch) (SCIPER 351986)
- [Arthur Lamour](mailto:arthur.lamour@epfl.ch) (SCIPER 300443)
- [Clémence Mayaux](mailto:clemence.mayaux@epfl.ch) (SCIPER 300278)
- [Sepehr Mousavi](mailto:sepehr.mousavi@epfl.ch) (SCIPER 338673)
- [Romain Rochepeau](mailto:romain.rochepeau@epfl.ch) (SCIPER 300574)
