# Authors
Group: CrunchyChicken
- [Sepehr Mousavi](mailto:sepehr.mousavi@epfl.ch) (SCIPER 338673)
- [Arthur Lamour](mailto:arthur.lamour@epfl.ch) (SCIPER 300443)
- [Romain Rochepeau](mailto:romain.rochepeau@epfl.ch) (SCIPER 300574)
- [Chang Chun-Tzu](mailto:chun-tzu.chang@epfl.ch) (SCIPER 351986)
- [Clémence Mayaux](mailto:clemence.mayaux@epfl.ch) (SCIPER 300278)

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
## Title
Director's choices on the destiny of a film
The power of directing choices on film success

## Abstract

## Research Questions (*goal is to convince TA idea has value and is feasible*)
1) Do directors who work in multiple countries exhibit different styles in each context? 
2) Is there a correlation between a director's critical success and the evolution of their style?
3) Are more successfull directors more often specialized in a particular genre, using particular characters, or there is a lot of diversity in their work.
4) Are directors successfull because they cast popular actors?
5) How to rate the directors?
6) How diverse the directors are in their character choices?
7) Can we find some directors that decided to cast, for their next film, only very popular actors at the time being ?
8) How active are the directors in terms of movie production ?
9) To what extent do directors experiment with their style over the course of their career, and are there periods of experimentation followed by periods of consistency?

## Proposed additional datasets
- [IMDb Non commercial datasets](https://developer.imdb.com/non-commercial-datasets/)
- [Stanford CoreNLP-processed summaries](https://www.cs.cmu.edu/~ark/personas/data/corenlp_plot_summaries.tar)

## Methods
- IMDb methods: *explain merge and/or how mapping was obtained how does it work maybe*
  
- NLP: following [*Learning Latent Personas of Film Characters* from David Bamman Brendan O’Connor Noah A. Smith](https://www.cs.cmu.edu/~dbamman/pubs/pdf/bamman+oconnor+smith.acl13.pdf), we first parsed all the XML files using *insert link to notebook* to obtain 4 dataframes: tokens, dependencies, coreference, parses. Using tokens and dependencies we can extract for characters present in movie plot summaries the agent actions, patient actions and their attributes, then we generated bags of words and used a [LDA](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) to find the typical personas *link notebook*. Since 2013, Stanford's coreNLP annotation pipeline has evolved, we decided to annoate the plots using the latest version of [Stanford coreNLP](https://stanfordnlp.github.io/CoreNLP/) to obtain better NER (Named Entity Recognition), allowing a more accurate identification of characters inside each movie plot. The coreNLP 4.5.5 pipeline code can be found here *insert link*. We use tokens, dependencies and an additional dataframe: Entity Mentions, that has the identified character per sentence of movie plot, this allows to have well defined characters and get more accurate typical personas using LDA.  

## Proposed timeline for P3


## Organization within the team
- Sepehr: IMDb
- Romain: IMDb
- Clemence: IMDb
- Arthur: NLP
- Chang: NLP

## Questions for TAs (optional)
