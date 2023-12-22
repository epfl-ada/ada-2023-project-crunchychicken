---
layout: post
title: How impactful is the team surrounding the director on the film's success ?
subtitle: A study of the relationship of a director's entourage and success.
categories: Team
banner:
  image: https://i.postimg.cc/brX52r7r/Film-Crew-1.jpg
sidebar: []
---

Regardless of the epoch when it has been produced or its genre, a film is before anything the product of the complex and intertwined contributions of the crew members that worked on the latter. Directors can be seen as the central knot that ties the ensemble of the crew together : from helping in casting choices to artistic directions on set, the director's role is to guide the team towards the best outcome possible

In this first part, we will therefore try to assess the impact of different aspects of the crew surrounding a director his or her success and, by extension, trying to analyse underlying keys to movie success.


<div style="text-align:center; color:#5A9">
  <h3 style="font-weight:bold;">How does the number of people working impact the success of movies & directors?</h3>
</div>

In blockbusters or big productions of the last decade, credit lists can get rather long at the end of film. One can have the image that the biggest, most well funded movies, can lead more easily to success. Before diving into the closer relationships that may exist between directors and their crews, let us thus first investigate if this is the case and if the number of people working on films actually plays a role in their success.


Our datasets contains information about movies ranging from the very beginning of cinematography, to the middle of the 2010's. It does not only contains massive Hollywood productions but also very minimalist and intimist films, as well as everything in between. In fact, the distribution of the movie crew sizes actually follows a power law.

<div style="display:flex; justify-content:center;">
  <div style="flex:1; padding:10px 10px 10px 10px;">
    <img src="https://i.postimg.cc/W19mY7Gr/powerlaw.png)" alt="Plot 1" style="max-width:100%;">
  </div>
  <div style="flex:1; padding:10px 10px 10px 10px;">
    <img src="https://i.postimg.cc/YCQmczBj/crewmoviecorr.png" alt="Plot 2" style="max-width:100%;">
  </div>
</div>


The relationship between the movie scores & crew size is thus difficult to analyse. We can observe that movies with very large crews do not tend to behave better than movies with medium\-sized crews \(a hundred to a few hundred people\). On the one hand, it still that larger crew sizes have less very unsuccessful movies, but a lot of successful movies are limited in terms of crew sizes. Correlation analyzes do not yield any significance neither when taking the whole picture.
Even if we take the top 10 movies in terms of success score, we can observe that they differ with each other in terms of crew sizes. Movies such as Inception & the LOTR movies had more than 1000 people working on them, but as are successful as The Godfather or Schindler's list that are way less crowded in crew density.

![top-10movies](https://i.postimg.cc/bvz03BSq/top10-movies.png)


Regarding the difference that can happen between large and small crew sizes, however, the interesting finding is not made at the scale of the movie but at the director's career scale. More precisely, the measure here is the average crew size that the director's crew choices during his entire career lead to. By observing the changes in success score with respect to the average crew sizes, we find significance differences between directors that had smaller crew sizes on average and directors with larger crew sizes. Those differences can be quantified by observing the success scores of directors with crew sizes either larger or smaller than a certain threshold, as on the two correlation plots below.

[![shift.png](https://i.postimg.cc/8zrLpfxf/shift.png)](https://postimg.cc/3kYk9N83)
[![help.png](https://i.postimg.cc/tTgJBYQ4/help.png)](https://postimg.cc/Ff2hRFHM)

For the majority of our thresholds, when conducting t-tests, the p-value is inferior to 0.05 and hence that the null hypothesis, i.e no difference between the populations of directors is not able to explain the observed differences in success score. This tends to indicate a significant difference between directors with differing crew sizes, which disappears starting from around 1200 members in the crew. Passed this point, the success scores of the directors with large average crew sizes are singificantly lower, thus draging the overall score of the director group to lower values and making the significance between groups vanish.

While the impact of a crew size on the success of the movie seems unsignificant, we still observe differences in success between directors that had very large crew sizes and directors with smaller crew sizes, on average. We must still temper the result with the nature of the data we have : we recall that we have an inherent skewness in our data with very few directors having very large crew sizes and thus even less directors that would have huge crew sizes on average in their career. However, even for the largest values considered on the graph, we have approximately two hundred directors to consider which is still reasonable.


<div style="text-align:center; color:#5A9">
  <h3 style="font-weight:bold;">Is the success of directors linked to the presence of certain individuals in their team ?</h3>
</div>

Now that we had a look at the crew in its entirety, let us dive into more specific members of the crew. Staying large at first, a first interesting measure to try and quantify the presence of certain individuals is to simply measure which persons stay in the director's crew from one movie to the other. To do so, we decide to use the overlap coefficient defined as  :

\[
\text{Overlap Coefficient} = \frac{|A \cap B|}{\min(|A|, |B|)}
\]

0 thus representing a very small overlap and 1 a large overlap, A & B being the two movie crews we want to compare. Here, we aim to know whether **certain** individuals are linked to the director's success and the choice of this particular metric over others, such as the Jaccard index, is mainly motivated by the fact that we do not want to penalize crews of different sizes. We therefore compute the average Overlap coefficient of directors over their different movies and the results obtained below for our directors are indicating that the vast majority of our directors tend to have low overlap coefficients, directors with a coefficent $>0.1$ are fairly rare. Moreover, it seems that the majority of our successful directors, are in this category and thus do not tend to overly work with the same people from one film to the other.

[![overlap.png](https://i.postimg.cc/TYf9YZSx/overlap.png)](https://postimg.cc/bdVbmFpV)


However, even if the value of the overlap is very small, it is non-zero in most cases, indicating that some people still work with directors from one movie to the other.
To assess the extent to which these persons presence is linked to the director's success, we identified the ones that starred in their most famous movies, that we will call the **core relationships** of a director. Our investigation showed that extremely few directors had collaborations going on during their entire career, we therefore decided to take all people, for our directors, that participated in at least 4 out of the 5 most famous movies of the latter, the top 7 shown below. Notice that we shift to the use of the 'avg-5' score here as we want to assess the success on these 5 movies.


[![firsttable.png](https://i.postimg.cc/dtPg82QB/firsttable.png)](https://postimg.cc/YjRX7mWG)

Some of our most successful directors indeed have core relationships such as Nolan, Tarantino or Spielberg. These close relationships can be purely professional, such as the famous composer John Williams & Spielberg, but we also find Emma Thomas & Jonathan Nolan, his wife and brother respectively. We have other examples, though not shown here, such as Peter Jackson which has a staggering 93 core collaborations, which are people that typically worked on all of the LOTR & Hobbits movies. Before studying the nature of these relationships, we wondered if, simply, more of these core relationships lead to more success for the directors. We took care to balance the dataset to avoid the potential cofounding effect of the number of movies directed on both these values, as an increase in both core relationships and success of a director could just be due to experience. For visualization, we set the threshold for successfulness of a director at an 'avg-5' score of 30. Same results were obtained when both increasing,to a certain extent, ~45 as a maximum score, and diminishing the threshold.


[![download.png](https://i.postimg.cc/05ZHJYwh/download.png)](https://postimg.cc/t7ZzKVDz)


The difference in the average core members count between the successful and unsuccessful groups graphically seems significant, and a t-test conducted using the latter resulted in a $10^{-5}$ p-value. We therefore have evidence against the null hypothesis, suggesting a significant difference in the average number of core members between directors that are successful and directors that are not. While it does not links causation, both successfulness and the ability of directors to maintain core relationship through their work are correlated !


We can now come back to the nature of core relationships. We saw with our seven most successful directors that they could be of various types, but what about the rest of our directors ?

[![0e4e7613-27d7-4908-a8ff-50b53deddc10.png](https://i.postimg.cc/gcDSCVcN/0e4e7613-27d7-4908-a8ff-50b53deddc10.png)](https://postimg.cc/rzDNWtrr)

Plenty of different jobs can be found here ! There is not one predominant type of relation between one director and one particular job, and many different technical crew jobs can be seen here, such as the cinematographers, the editors, people working in the sound department, or even in way smaller proportions stuntsmen/women, costume designers, etc. We can still observe that the three major core collaborations types of directors are producers, followed by writers and actors. It is also interesting and worth noting that, actresses are far less present $10\%$ vs. $2\%$ of the time, still a sign of a male-dominated industry. Considering only the professions majorely represented here,i.e everything but 'others', we performed multiple pairwise statistical tests to observe potential singificant differences between the professions with respect to the success of directors that had a core relationship with them.

[![40e0335e-40e0-4c0a-8aa8-813d15b7c28c.png](https://i.postimg.cc/jSFzVh10/40e0335e-40e0-4c0a-8aa8-813d15b7c28c.png)](https://postimg.cc/DS1WL1FB)

The results however show that the average score are close for all our professions, and that no significance in differences could be found. The chemistery and what makes success in this relationship is therefore not related to the exact professions of the persons part of these core relationships. Chemistry between a director and his core crew members is deeper than that !

Overall, the two main axes studied here showed different results. We observed that the amount of these core relationships was definitely linked to the director's success, while the profession or exact jobs of the latter did not seem to matter as much. Film success will therefore be directly impacted by the these kind of privileged relationships : if success of directors grows, the successes of its films as well. And as we saw, we are not here mentioning only the very few top Hollywood directors, but a few hundreds of directors that we considered to be successful throughout their careers !


<div style="text-align:center; color:#5A9">
  <h3 style="font-weight:bold;">Are some directors successful only because they cast popular actors ?</h3>
</div>

We saw that one of the most present professions in core relationships of directors where actors. Up-and-coming actors can of course be casted, but we know that successful directors, during their career, tend to associate most of time with very popular actors. We therefore focused on these popular actors and actresses as well to see how much they collaborated with our directors, and therefore impacted to their success : the idea is to only keep the actors and actresses that collaborated with our directors a few times.


[![secondtable.png](https://i.postimg.cc/Cx7qCpD4/secondtable.png)](https://postimg.cc/cvKCZjFK)

The success of an actor was computed in the same manner as the directors, to have a common measure on the movies, in order to evaluate confidently the relation between the scores of an actor and a director. Once again as as always, simple plots showed, once again, correlation between these two values, taken as the average of the actors scores for all collaborations of the director. But here let us rather, instead of looking at these scores directly, look how the network of collaborations looks like.

More precisely, we constructed a bipartite graph where each of our directors and most successful actors are represented by a node and each edge is weighted by the number of times each actor or actress collaborated with a certain director. To observe the result, we take the bipartite projection of this graph on the nodes of our directors. By doing so, the nodes of our directors are going to be related by the amount of actors/actresses collaborations they shared : the idea is thus to observe how much successful actors are shared within successful directors. First, we observe the result of such a projection on our 20 most successful directors :


[![successfulones.png](https://i.postimg.cc/PxRbWsg7/successfulones.png)](https://postimg.cc/cgf8Wj47)


Our most successful directors seem very connected in terms of their relationships, but how does it differ from less successful directors ?

[![Lessones.png](https://i.postimg.cc/DwPMq0BY/Lessones.png)](https://postimg.cc/zy37Nzmn)  [![evenless.png](https://i.postimg.cc/8CyX038R/evenless.png)](https:/postimg.cc/d7y975V3)


We see that the relationships in terms of actors/actresses collaboration sharing is way lower for directors that can be categorized as unsuccessful.
There is clearly a relation between the success of a directors and the kind of relations they hold with other successful directors in terms of actor casting. The actors that star in movies of very successful directors tend to star in the movies of other successful directors, while it is way less the case for unsuccessful directors. But does that mean that casting actors because they starred in famous movies is the key ? Let's look at the bigger picture. 

A similar graph formation & bipartite projection is formed, this time including every different collaborations that we have been able to find thanks to the IMDb data, whatever the roles or profession of people, the idea is to see if the behaviour we saw above is only specific to actors or if it is something general. A visualization of the evolution of the bipartite projection on the directors nodes is below. Once again, each node represents a director and the edge width assess how much they worked with the same people overall. 


{% include plotly_directors_connections_include.html %}


As you can see, by sliding the widget to the right, we go from successful directors to unsuccessful ones, taken randomly. We can indeed observe that the behaviour seen for actors just above is reproduced here : The most successful the directors are, the most relations they share in the industry. On the contrary, the less successful the directors, the less relationship they share with each other.

The closeness of directors is thus symptomatic of something bigger than just directors casting actors that other successful people, and thus successful actors, have worked with. The phenomenon is generalized to all professions : successful people tend to work with successful people, and the increase in collaborations between directors indicate their integration to the 'successful' network of directors.

It is therefore most likely that directors are not successful uniquely because they cast successful actors, but rather because their collaborations, in all professions of the movie crew, are populated with people that have already worked in 'successful' environments. Successfulness of a director, throughout his career, is thus definitely impacted by his or her ability to surround him.herself with the right persons : high chances that a successful crew will lead to a successful movie !

<div style="text-align:center; color:#5A9">
  <h3 style="font-weight:bold;">Conclusive thoughts</h3>
</div>

Through this first part, we have a good grasp on the different impacts that a movie crew can have on the success of a movie and on the director's careers. Crew size, core relationships and director's crew networks are all important factors to take into account when measuring the impact of various aspects of the crew's nature.
It is still important to mention that our analysis will be inherently biased towards the people that the IMDb, and more generally the websites and industries, decide to put in the spotlight. The exact and complete data about very specific members of the crews were present in less amount than for the actors, or directors. If we can not really measure the impact of the more obscure and technical roles, a sure thing is that movies would not be able to see day without them!
