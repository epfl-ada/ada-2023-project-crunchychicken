---
layout: post
title: Success Measures
subtitle: How we quantify measures for success of a movie or a director
categories: General
banner:
  image: https://i.postimg.cc/L8ZnDTVR/image-2023-12-11-214623541.png
sidebar: []
---

<!-- TODO: Let's refer to this post in the other postes -->

In order to conclude anything about the success of movies or directors in a data-centric approach, first, we need to have a definition about success, and it has to be such that we can measure it with the available data.

We follow a movie-based approach for defining the success of a director, which means that we first need to define a success score for the movies. Having those, we can define several scores to quantify the success of a director based on the scores of the movies that the director has portrayed.

## Success of a movie

Many different measures can determine the success of a movie. Briefly, what matters could be summarized into these four questions:
  - How many people watched the movie?
  - How was the quality of the movie?
  - How impactful was the movie?
  - How much money did the movie make?

For some, maybe the last question suffices to define the success of a movie. However, in this study, we focus more on the popularity and the quality of the movie. Measuring the impact of a movie is possible by for instance analyzing the blogs, posts, and tweets that mentioned the name of the movie. The authors believe that this is a tedious task and out of the scope of this study. The revenue of the movie is available in our datasets but only for 10% of the movies. We argue that the revenue of the movie is somehow reflected in the popularity and the quality of the movie, and we stick with the first two questions in this study in order to be able to analyze a larger dataset.

The answer to the first question is directly reflected in the number of IMDb votes that a movie receives. The more popular the movie, the more people watch it, and the more votes it receives. Similarly, the quality of the movie is reflected in the average rating of the movie, which is again available from the IMDb datasets. We therefore only need to find a suitable way to combine these two measures.

Another measure that we can look at is the number of awards and nominations of a movie, which reflects the answer to all the four questions stated above. However, we believe that relying on the number of awards and nominations of movies will limit us only to a set of award-winning movies and limits having a score for less-known movies. Even though the focus of this study is on successful directors, who have many award-winning movies, we still want to take into account the non-award-winning movies of these directors. However, we can use these data to validate any success metric by looking at the correlation of the metric with the number of awards won or nominated.

We define the success score of a movie as
$$
S_{movie} = {Rating}_{movie} \times \log({Votes}_{movie}),
$$
which reflects both the popularity and the quality of the movie.

### Assessment of the metric

In the following, we show that the suggested score represents the success of a movie well by validating it against the revenue and the awards of the movie.

[![corr-score-revenue.png](https://i.postimg.cc/vDRQXghk/corr-score-revenue.png)](https://postimg.cc/m1wfgr0y)

The above figure shows the distribution of the score with different revenue ranges of the movie. We can see that overall, there is a positive correlation between our score and the logarithm of the revenue of the movie, although this correlation is stronger for higher scores.

[![corr-score-awards-Won.png](https://i.postimg.cc/MTTKG8XP/corr-score-awards-Won.png)](https://postimg.cc/XZR02mfd)
[![corr-score-awards-Nominated.png](https://i.postimg.cc/gkwXD3zS/corr-score-awards-Nominated.png)](https://postimg.cc/Lnp84YZL)

The above figures show the distribution of the score with different ranges of number of awards won and nominated. The positive correlation shows that our metric is able to capture well the features which define the success of the movie in terms of its chances for winning awards.

However, we should bear in mind that this method for quantifying the success of a movie favors the movies with larger audiences to a large extent. For seeing this, we can take a look at the overall distribution of the number of IMDb votes and the IMDb rating and compare this for movies produced in different countries or in different decades. In the following figures, we can observe that movies produced in some countries such as Argentina clearly have lower votes than the whole dataset, which will damage their final score. Likewise, the movies produced in the 10s have been watched by less people in the technological era, which is again, reflected by lower number of IMDb votes. This could lead us to favor modern-life directors over the older ones simply because they have had larger audiences. To address this, we should always compare the scores of movies or directors that are produced in the same country and in the same temporal period.

{% include ratings_votes_by_country_include.html %}


The following figure shows the distribution of movie scores for several countries. Countries like Argentina have significantly lower average score, while countries like Turkey and Iran that have larger populations, have higher means than the United States.

[![dist-score-country.png](https://i.postimg.cc/Pq6vyyw7/dist-score-country.png)](https://postimg.cc/HJyLsQ30)

The following figure shows the distribution of movie scores for different time periods. Although the average score is more or less similar, we can see an increasing trend in the second and third quantiles, and many more outliers for more recent periods.

[![output.png](https://i.postimg.cc/6Q74HRf5/output.png)](https://postimg.cc/3yTwNkqP)

## Success of a director

The success of directors can simply be defined in the success of their movies. However, one can aggregate multiple movie scores differently. 
The most basic idea would be to calculate the average success score of the movies of a director. In this study, we follow the logic that only a few successful movies is enough to make a director successful. Taking Martin Scorsese for instance, movies like Casino, Goodfellas, and Taxi Driver are enough to make him a successful director, and for such directors, we should get a success score close to maximum, so why impinging his score with taking into account the success of movies like Made in Milan or The Family which nobody knows about?

We propose the following aggregate scores for measuring the success of a director:

- `avg-n`: Average score of the top `n` movies
- `hits-s`: Number of movies with scores higher than `s`
- `rate-r`: Number of movies with IMDb ratings higher than `r` with at least 1000 votes

TODO: ADD INTERACTIVE TABLE WITH DIFF SCORES (TOP 10)

Note that `avg-n` can therefore only be calculated for directors with at least `n` movies, which does not interfere with the purpose of this study sicne we are focused on successful directors.

Among the proposed scores, `avg-3` seems to be the most reliable one with the fewest missing values. Therefore, we pick this score as the main score along this study but we refer to the other scores as well. For instance, `hits-s` can be used to find very few legendary directors, and `rate-r` can be used to determine directors with at least a few highly rated movies, but not necessarily *"successful"*. The number of directors for whom the `avg-3` score can be calculated is 6500, about 20 percent of the total number of directors for whom we have data. The following figures show the correlation between the `avg-3` scores with `hits-40`, and the awards won or nominated by directors. The positive correlation confirms the validity of our chosen metric.

[![corr-dir-score-award-Nominated.png](https://i.postimg.cc/X7Lpgxd0/corr-dir-score-award-Nominated.png)](https://postimg.cc/qztJJs1m)

[![corr-dir-score-award-Won.png](https://i.postimg.cc/g2BjCJgS/corr-dir-score-award-Won.png)](https://postimg.cc/fVmMXwnm)

[![corr-dir-score-hits40.png](https://i.postimg.cc/k5045H3W/corr-dir-score-hits40.png)](https://postimg.cc/7CNDsmLL)

### Successful directors in different countries

TODO: MOVE THE TABLES HERE


## Final remark

In order to address the limitations of the proposed scores, in a more data-centric alternative approach, one could deploy a supervised machine learning algorithm in order to learn a representive score for the directors based on different features about the director or their movies. This way, the features could take into account the nationality or the birth year of the director, among many other features.
