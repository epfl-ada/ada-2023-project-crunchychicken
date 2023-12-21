---
layout: post
title: To what extent does the director’s choice of movie genre affect the success of the movie ?
subtitle: SUBTITLE
categories: Genre
banner:
  image: https://i.postimg.cc/5th5pyzK/image-2023-12-11-214555044.png
sidebar: []
---

**Are more successful directors more often specialized in a certain combination of genres?**

Some directors are known for consistently producing the same movie genre, while others explore a wide range of cinematic genres. Looking at the most successful directors, Joel Coen excels by producing films in a limited number of genres, while Steven Spielberg experiments with more than 60 different genres. Our aim is then to determine which combinations of genres lead to the highest level of success

![best-directors.png](https://i.postimg.cc/d1P1qdxF/best-directors.png)

To explore these combinations, we can project the bipartite graph onto the films, to highlight the relationships between the different genres.

![coexsistence-genre.png](https://i.postimg.cc/wv6CcjtJ/coexsistence-genre.png)

When we look at the coexistence of genres within a group of directors, we see that the drama genre is closely associated with romance, and that drama and comedy are also strongly linked. These combinations of genres can be a crucial factor in a film's success.

**Are directors who tend to work on more diverse projects less successful or more successful?**

There is a noticeable variation among directors regarding the diversity of their projects. Analyzing the relationship between the average scores of directors and the number of different movie genres they explore, reveals a robust correlation. The success of directors appears to increase with the diversity of their projects.

![genre-explored.png](https://i.postimg.cc/rmnmXbxd/genre-explored.png)

![score-directors-genre.png](https://i.postimg.cc/zXSfqVCZ/score-directors-genre.png)

**Correlation between a director’s critical success and evolution of their style regarding movie genres ?**

Performing an Ordinary Least Squares (OLS) analysis between movie score and runtime, director's new genre and directors' career years, we find a weak but significant correlation between film success and director's new genre. Moreover, we observe a strong and significant correlation between the runtime and the movie score.

**To what extent do directors experiment with new genres and thematics over the course of their career, and is there a pattern of periods of experimentation followed by periods of consistency?**

We note that, directors are less and less inclined to explore new genres as their careers progress.

![directors-success.png](https://i.postimg.cc/N0tvN4yW/directors-success.png)

**Is it less likely or more likely for a movie to succeed when the director tries a new genre?**



![Temp Image](https://i.postimg.cc/sX52PNjZ/image-2023-12-11-214406269.png)
<!-- Example of manual size change, if you use both width and height the original aspect ratio of the image will not be preserved (deformation) -->
<img src="https://i.postimg.cc/sX52PNjZ/image-2023-12-11-214406269.png" alt="Temp Image" width="300"> <!-- height="50"> -->

{% include plotly_demo_include.html %}

{% include plotly_top_directors_by_country_include.html %}