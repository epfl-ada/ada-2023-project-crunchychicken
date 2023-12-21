---
layout: post
title: What is the impact of the director’s character choices on the success of the movie ?
subtitle: SUBTITLE
categories: Genre
banner:
  image: https://i.postimg.cc/5th5pyzK/image-2023-12-11-214555044.png
sidebar: []
---
We're familiar with the notion that a director's success often hinges on their selection of characters in a movie. Yet, what types of characters do accomplished directors gravitate towards? How varied are directors in their choices of characters? Can we identify highly successful directors who consistently lean towards specific character types, and conversely, those who exhibit a broad spectrum in their character selections? Moreover, does the choice of characters significantly influence a movie's success? This section aims to delve into these questions and uncover the intricate connections between directors' character choices and the ultimate success of both the directors and their films.

## Exploring Character Choices of Successful Directors
To understand the character preferences of successful directors, we'll start by examining the top 10 directors in our dataset.

[![top10-directors.png](https://i.postimg.cc/qqDrQDsd/top10-directors.png)](https://postimg.cc/SY9Hxr1Z)

These directors are widely recognized in the industry. Moving on, we'll take a closer look at the score distribution of directors.

![distribution-score-directors.png](https://i.postimg.cc/cCnBzRdv/distribution-score-directors.png)

The director scores are centered around 20-30, indicating a distribution that follows the normal distribution pattern, with the highest frequency occurring around the average.

Now, let's delve into the distribution of character types chosen by all directors.
[![topic-distribution-of-top10-directors.png](https://i.postimg.cc/6pqdq8jj/topic-distribution-of-top10-directors.png)](https://postimg.cc/HrGJPkCX)

What are the choise for the top 10 directors?
[![director-chracter-choices-heatmap.png](https://i.postimg.cc/QMbJwYqB/director-chracter-choices-heatmap.png)](https://postimg.cc/kV2Stcz9)

It appears that they all make diverse character choices. Let's examine this more closely. The top 5 topics among the top 10 directors are 14, 31, 19, 30, and 15. Now, let's explore the words corresponding to each topic.

| Chracter types | Words                                            |
|-------|--------------------------------------------------|
| 14    | tell take find leave try give visit admit agree return |
| 31    | see ask tell find go refuse leave get give try   |
| 19    | officer hire general detective david major assign film artist pilot |
| 30    | wife girl plan befriend member martin wound ex expose minister |
| 15    | john professor perform rao consider guy intervene transform count dump |

And the distribution of all character types among the top 10 directors.

[![chracter-type-distribution-top10-directors.png](https://i.postimg.cc/zD0KNRWQ/chracter-type-distribution-top10-directors.png)](https://postimg.cc/QVKHkCfg)

Based on the information above, it is evident that character type 14 is the most commonly chosen among all top 10 directors. Nonetheless, the character choices vary significantly among these directors.

## How diverse the directors are in their character choices ? 

From above, seems like success directers have a diverse choice of chracters. But let us explore more about the diversity if the directors choices of chracters. First, let see the distrubutin of the directers by the number of unique chracters he/she workded with.
[![Distribution-of-Directors-by-Number-of-Unique-Characters.png](https://i.postimg.cc/J7ckRYDK/Distribution-of-Directors-by-Number-of-Unique-Characters.png)](https://postimg.cc/fkyLKKv0)

Let's have a close look of ten directors with the highest diversity.
[![top10-directer-highest-diversity.png](https://i.postimg.cc/05BqKPwN/top10-directer-highest-diversity.png)](https://postimg.cc/z3KQ9mpm)

From the above pie chart, we can observe that almost half of the directors only worked with one or two chractor type. However, using this method to define the diversity of directors' chatacter choices  might be subject to the influence of the total number of movies each director has undertaken. To achieve a more precise quantification of the diversity in directors' character choices, we need a more refined quantitative method.

For quantify diversity, we calculate the Shannon diversity index with normalization for each director based on the distribution of chracter types in their movies. Higher entropy values indicate grater diversity.
[![Distribution-of-Directors-by-diversity-score.png](https://i.postimg.cc/K8K7cryz/Distribution-of-Directors-by-diversity-score.png)](https://postimg.cc/MnSfdBH2)
[![top10-directer-highest-diversity-score.png](https://i.postimg.cc/Y9LT1mgq/top10-directer-highest-diversity-score.png)](https://postimg.cc/BLsh3bMd)

Based on the information presented in the pie chart, it is evident that 32.6% of directors exhibit a diversity score falling within the 1-2 range. Additionally, 31.6% of directors possess a diversity score of 0, indicating that their works predominantly feature a single character type. It's worth noting that this might be influenced by the limitations of the plot data available from CMU, as not all movies and characters have sufficient information to determine character types accurately. In the 0-1 range, 20.1% of directors fall into this category, while 13.8% fall within the 2-3 range. Notably, only 1.9% of directors attain a score of 3-4, indicating a higher diversity of character types in their works.

## Can we find very successful directors that always use the same type of characters or others that vary a lot in their personas choices ?
## In definitive, how does this impact the movie’s success ?

<!-- ![Temp Image](https://i.postimg.cc/sX52PNjZ/image-2023-12-11-214406269.png) -->
<!-- Example of manual size change, if you use both width and height the original aspect ratio of the image will not be preserved (deformation) -->
<!-- <img src="https://i.postimg.cc/sX52PNjZ/image-2023-12-11-214406269.png" alt="Temp Image" width="300"> height="50"> -->

