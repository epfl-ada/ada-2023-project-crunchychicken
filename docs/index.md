---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Home
heading: "Frames of Success: Diving into the minds of movie wizards"
subheading: "Chang Chun-Tzu, Arthur Lamour, Clémence Mayaux, Sepehr Mousavi, and Romain Rochepeau"
banner:
  image: /assets/img/banners/atriptothemoon.gif
  opacity: 0.50
  background: "#000"
  height: "100vh"
  min_height: "38vh"
  heading_style: "font-size: 4.25em; font-weight: bold"
  subheading_style: "color: gold"
---

## **Abstract**

Stanley Kubrick is known to have at least one great movie in every major movie genre. Conversely, when you see David Fincher's name as the director of a new movie, you are almost sure that there is going to be one or more serial killers involved. The directorial approach of the most successful directors can be so different and taking the right directorial approaches early can lead a director to achieve significant success in their career, and is believed to be the main factor determining the quality of the movie. In this data analysis project, we will utilize the CMU Movie Summary Corpus, along with supplementary datasets, to examine approaches of the brightest directors from three angles: the genre of their films, the team surrounding them, and the character personas in their movies. We aim to gain a clear insight on how their decisions impact the overall success of the movie.


## Datasets

The main datasets used for the project were:

- CMU movie corpus : Aligned plot summaries & Metadata from ~80 000 movies, including Movie genres, release dates, runtimes, languages, etc.

- Stanford CoreNLP-proccessed summaries : The aligned plot summaries run through the Stanford CoreNLP pipeline.

- IMDb Non-commercial datasets : Several datasets containing various information about the IMDb registered movies, people working in the industry and ratings, principally.

- "TheMovies" Dataset : Metadata of ~45 000 movies containing various metadata such as the budget, the ratings, the runtime, the revenue, etc.

## Conclusion

Throughout this entire data story, we have seen observed the complex relationships underlying directors and hence, movie success. Using our home-made success metric, and various analyses we have been able to emphasize the following points.

- The crew holds a particular role in the success of a movie. We found out that the impact of the entire crew was difficult to quantify, while some particular relationships seemed to have more impact on the success of directors. Mainly, the core collaborations the latter nurtured during their careers with specific individuals is common in many successful directors. It is most likely not a particular profession that will assess a director and movie success, such as staring a famous actor. Rather, it is the association of successful people with successful directors which seems to impact the most the success of the director's and, of course, the movies.


- The relationship between the genre of the movie and the movie's/director success was mixed. The diversity of directors with respect to their projects was not found to confidently impact their success, and there even seems to be a negative trend in terms of innovation for the latter, even if milder amongst the successful directors. On the other hand, we found that a movie was not necessarily less appreciated and successful if the director tried a new genre in one of his or her movies. However, some clusters amongst certain genre combinations,  were overall more present throughout the industry.

- We finally saw that character choices varied among successful directors and that most imporantly, the diversity score constructed was useful to assess the director's score, and thus success. A similar analysis can be made for the movies themselves, which tend to be directly impacted by how diverse they are in terms of personas and characters.


By looking through the prism of directors, we have found some insightful answers about the impact of the crews genres and personas on the movies success. While crew and personas yielded some strong information towards positive success of a movie, the genres analysis conducted was rather more difficult to assess. Another difficult thing to assess is the relationship the three different factors, not even counting all the underlying subfactors, but one thing is sure : they all impact the movies success at their own scale, and for various reasons as we saw during the data story.