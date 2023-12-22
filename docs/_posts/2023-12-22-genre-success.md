---
layout: post
title: Genres and Directors
subtitle: To what extent does director's experience with movie genres affect the success of the movie?
categories: Genres
banner:
  image: https://i.postimg.cc/L8ZnDTVR/image-2023-12-11-214623541.png
sidebar: []
---

## Introduction

...


## Is it less or more likely for a movie to succeed when the director tries a new genre?

To answer this question, we can compare the success score of the movies in which the director has tried at least one new genre, with the ones in which the directors has had previous experiences with all the genres in the movie. However, simply spliting the movies into these two categories might lead to wrong inferences. There are many cofounders that could directly or indirectly impact the success of a movie. Runtime of the movie, release year, languages, production countries, genres, director, and cast could be the principal ones, among many other factors. For the purpose of this study, it is not possible to take into account all these factors, but we try to balance the dataset on the cofounders that we have data about before drawing any conclusion.

For this purpose, we match the movies exactly on the categorical features: directors of the movie, production countries of the movie, languages of the movie, and genres of the move; and calculate propensity scores for continuous features: runtime of the movie, release year of the movie, and number of years from the first appearance of the movie director in our dataset. The last feature could be a very important one because we know that even the brightest directors always need some years before finding their style. The propensity score is calculated by the coefficient of the logistic regression predictor of the probability that the director employs a new genre in the movie. The matching is then done by maximizing the sum of weights (similarity of movies based on the difference of the propensity scores) in a graph of movies with edges between movies that match exactly on the categorical features. The following figure shows the distribution of the matched variables. Although the matching is not optimal, the distributions are more or less balanced in the control and the treatment groups. Note that the normalization of the features is done before the matching, thus mean values are slightly different than zero.

[![movies-balanced-boxplots.png](https://i.postimg.cc/nrmQZwFP/movies-balanced-boxplots.png)](https://postimg.cc/m1bryjFY)

With the balanced dataset of 5250 movies, the treatment and control groups are splitted based on the exploration of a new genre by the director. We can run related t-tests on the distribution of different success metric of these two groups. The t-statistics and p-values of these tests are reported in the following table for the distribution of the movie score, the number of awards that the movie has been nominated to, and the number of awards won by the movie. For all three, the p-value is higher than `0.20` which suggests that the null-hypothesis that exploring a new genre by the director does not change the average success chances of the movie cannot be rejected.

| Metric           | t-statistic | p-value |
|------------------|-------------|---------|
| score            | -1.2254     | 0.22    |
| awards nominated | 0.7898      | 0.43    |
| awards won       | -0.6488     | 0.52    |

This can also be observed visually when comparing these distributions for both groups:

[![movies-balanced-scores.png](https://i.postimg.cc/bNJwQ5fc/movies-balanced-scores.png)](https://postimg.cc/nMyxx0L0)

To see this further, we have fitted linear regression models for predicting the aforementioned success metrics based on the treatment feature and got the results summarized in the following table. Both the features and the metrics are standardized before fitting the linear regression models. In all cases, the coefficients are insignificant when compared to the intercepts and the corresponding p-values are larger than `0.20` which implies that we cannot reject the null hypothesis that the coefficient in this model is zero with the 20% significance level. Note that the independent variable is a categorical variable and the coefficient should be interpreted as the increase in the expected normalized score when the director tries a new genre.

| Metric           | Intercept (p-value) | Coefficient (p-value) | R-squared |
|------------------|---------------------|-----------------------|-----------|
| score            | +0.0089 (0.648)     | +0.0334 (0.223)       | < 0.001   |
| awards nominated | -0.0571 (< 0.01)    | -0.0176 (0.427)       | < 0.001   |
| awards won       | -0.0600 (< 0.01)    | +0.0149 (0.515)       | < 0.001   |


## Are directors who tend to work on more diverse projects less or more successful?

Similar to the previous question, we can compare the success score of the directors and check the correlation with a measure of *tendency for more diverse projects*. We do this for two measures: 1. the average number of genres per move of the director; and 2. the total number of explored genres. The dependent variable here is, the `avg-3` score of the director and the number of awards of the director (note, director, not movie). The following table summarizes the results of linear regression models for predicting the dependent variable from each of the two dependent variables. Note that contrary to the previous question, here the features are not standardized. The first row shows that there is a small correlation between the average number of genres per movie and the success score. The second and the third rows show that although the positive correlations with the average number of genres per movie are insignificant with a significance level of 5%, there is a very small significant positive correlation with the total number of genres explored. The low R-squared in all the models shows that very little part of the distributions can be explained by the independent variables linearly.

| Metric           | Intercept (p-value) | genresPerMovie (p-value) | genresExplored (p-value) | R-squared |
|------------------|---------------------|--------------------------|--------------------------|-----------|
| `avg-3`          | +7.8017 (< 0.01)    | +5.4361 (< 0.01)         | 0.4017 (< 0.01)          | 0.198     |
| awards nominated | +8.7994 (< 0.01)    | +1.3527 (0.057)          | 0.3951 (< 0.01)          | 0.005     |
| awards won       | +5.4011 (< 0.01)    | +0.0568 (0.865)          | 0.1813 (< 0.01)          | 0.004     |

The figures below show the distribution of the `avg-3` score versus each of the independent variables. It is evident that there is not any significant linear correlation between the score and the independent variables.

[![avg-3-corr-genres.png](https://i.postimg.cc/Jz4s0hP8/avg-3-corr-genres.png)](https://postimg.cc/bsWyFp7V)

## To what extent do directors experiment with new genres and thematics over the course of their career?

To answer this question, we analyze the correlation between the career years of the director in the release year of the movie with a categorical variable which indicates whether a new genre has been explored by the director in the movie. It is natural to expect a decreasing trend of trying new genres as a director goes through his career. The following table shows the results of fitting a linear regression model between these two variables considering different datasets. Note that both features are standardized before fitting the model.

| Movies                | Intercept (p-value) | directorCareerYears (p-value) | R-squared |
|-----------------------|---------------------|-------------------------------|-----------|
| All                   | +0.6804 (< 0.01)    | -0.2148 (< 0.01)              | 0.212     |
| Successful director   | +0.6308 (< 0.01)    | -0.1555 (< 0.01)              | 0.159     |
| All (after 7.5 years) | +0.5380 (< 0.01)    | -0.1019 (< 0.01)              | 0.032     |

In the first two models, the intercept is quite high which means that with average years passed through the career of the director (around 7.5 years), the probability of trying a new genre is 0.6804 and 0.6308 among all directors and successful directors, respectively. Here, successful directors are those whose the `avg-3` score is higher than 40, which includes only 135 directors in our dataset. In both models, there is a significant negative correlation between our variables. The coefficient for each row means that for each standard deviation (around 9.3 years) passed through the career of a director, the probability of trying a new genre drops as the coefficient. We notice a smaller drop among the successful directors. The third row takes into account the fact that in the first years of their career, it is naturally more probable for directors to try new genres, and takes into account only movies after at least 7.5 years through their careers. Here, again, the negative correlation exists although it is a bit milder than the other two. These negative correlations are obvious in the followin figure. Here, the mean value of binary dependent variable is plotted agains the independent variable, with 95% confidence intervals.

[![careeryears-newgenre.png](https://i.postimg.cc/T1VKLLzd/careeryears-newgenre.png)](https://postimg.cc/T5PdBw2F)


## ...

TODO: Add temporal plot for director genres (interactive)

## Are more successful directors more often specialized in a certain combination of genres?

To answer this question, we need to study not only the existence of single genres in the movies of directors, but also the co-existenec of one or more genres in their movies. Take, for instance, three comedy-romance movies, one romance-drama movie, and three drama-crime movies in a portfolio. The presense of romance genre is the same as drama (4), and close to the presence of comedy (3) and crime (3), but these numbers alone do not represent the style of this portfolio. What is significant here, is the co-existence of comedy-romance and drama-crime movies.

In order to get the co-existence of genres, we define a undirected bipartite graph of the movies and their genres, and draw an edge between each movie and its genres. Projection of this bipartite graph on the movies will give us a multigraph of co-existence of genres in a group of movies. The multiplicity of each edge can then be reduced to a weight to get an ordinary undirected weight graph of the co-existence of genres in a group of movies.

{% include genre_coexistence_include.html %}

