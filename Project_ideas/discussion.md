# Actor's Preference of Character and Corresponding Revenue ⭐
Question: What kind of characters do actors like to play? Same types of roles every time or experementing with different characters? Do the actors in some countries have more preference towards some type of characters? How do the character choices affect the movie revenue (does an actor's preference for a certain character type always lead to greater success, or are there cases where a particular character type doesn't quite click with an actor's style)? Are there actors that do well in various character types and how rare is it?

TA remark: How do you plan to categorize the characters played?

Discussion: first question (+ TA remark) is very close to the paper, we can inspire ourselves from their technics to find the characters types (agent actions, patient actions, attributes). Looks like we will use most of the training data:
- plot summaries and parquet dataframes for the character type identification
- movie and character metadata for the country and gender aspects. 
Note: the movie revenue has a lot of NA, need to see if we have enough data by only keeping the non NA rows. Worse case, we can use a scraper to complete the missing box office from wiki or IMDb.


## Feasibility of the idea : 
If we can not extract the personas of if we do not exactly know how to use them immediately, we should drop the idea.

## Research questions :
If we have the personas, we could try several things :

- Are the actors 'confined' in a certain type of role and /or character ? How different is depending on gender and ethnicity ? Is there biases or stereotypes reinforced on this basis ?

- How does the actor's choices relate to the movie success ? More generally, for the actor him/herself, how does this change throughout his/her career ? For some actors, is there a shift in roles played ? If it's the case, how long does it take an actor to 'find his/her way' ?

- Can we find some preferences that go well together ? Nothing as strong as a 'recipe' to success, but actor's preferences that match well ?

- What are the factor's that could lead to changes in actor's prefences ? Evolving under a new director ? Simply with age ? With the other actors that they work with ?









# Child stars 
Question: focus on young actors, how long do they stay in the "spotlight" and how much money they make throughout their carrer (at different periods)? What is age period is the peak time for a child star (early stage or later)? Are there children stars who are successful for a long period or is it hard for them to maintain popularity throughtout their carrer.

TA remark: Great question!! How would you characterize ‘being in the spotlight’ or the ‘peak time’?

Discussion: the data we have does not have actor salary, would have to use an external source for it (if there is one + compatible with the characters/actors in the dataset). We could use the movie revenue as a success criteria but there are a lot of nans, can possibly be an issue. Mostly using the movie and character metadata.


## Feasibility of the idea :
In my opinion very feasible if we have enough data to deal with. Could be problematic is if the number of child actors in the dataset is too low. For the CMU, without cleaning anything we have 4086 actors with age < 18 in the dataset which is already ok, but the number of child 'stars' among them will for sure drop.  Can only increase when adding IMDb data, but still.


## Research questions (to answer before P2 and after P2?) :

-   TA remarks : How do we characterize 'being in the spotlight' or 'peak time' ?

-   Who are child stars ?
    - Among the children actors, how many could be effectively counted as child stars? 
    - Is this a global phenomena or is it more pronounced in some countries ?
    - In which of their childhood years do they 'shine' the most ?
    - In what type of films do they tend to play ?
    This could help to familiarize with them and to start having a clue, maybe, about why they are famous

- We could guess that they must be very 'protected' : are they always surrounded by the same persons throughout their 'child-career' and how does this evolve with time ? (we could include relationships in the mix with that question)


- Do Child Stars reach their peak during childhood ? Are they destined to have a drop in popularity and in success as they grow up ?

- Intertwined with the previous question, in a way, is that for the ones for which the peak is reached during childhood : what do they become ? Do they stay in the movie industry and keep trying or just disappear after a while ?



# Decoding Movie Success: What Makes a Film a Hit?
Question: Why are some films popular? What kind of movie, characters, stories, actors are the most important for a movie's success? Are the keys to sucess different from country to country (show the regional trend and also global trend of movie)?

TA remark: A bit less creative and clear than the 2 first ideas. You don’t detail how you would proceed from a data analysis perspective whereas it is the goal of this project!

Discussion: revenue has a lot of nans could be an issue. "Hit"/"popular" can be very biased: cultural (bollywood), critical vs commercial success (Hollywood / Marvel movies making a lot of box office with shitty plots), marketing influence, demographic preferences

# Technological Advancements in film production
Question: how did technological advancements (synchronous sound, colour, green screens, digital lenses, CGI, internet) changed film production/ how did the film industry respond to these technological advancements? Is there a slump or a rise in certain movie genres following the invention or democratization of some techniques? Do films embrace this new type of cinematography receive different revenue and critical acclaim compared to traditional ones ? When new methods are invented, do films that embrace this new type of cinematography receive different revenue and critical acclaim compared to traditional ones? Did technological advancements modify the way films uses certain genres or themes using the plot summaries? In science fiction for instance, is there a shift towards space-related fictions after invention of green screens?

TA remark: great idea, really liked the idea of adding the methods used in each film

Discussion: the data we have is missing the technological advancements and methods used by films. For technological advancements with Google, we could possibly find the technological advancements and when they their created, but unsure if we can easily find info about the technology used for the movies in the dataset.

## Feasibility of the idea :
We most likely won't be able to retrieve all techniques used by a film (CGI etc. etc.) Some of them would be easy to find (no sound --> sound, black&white --> color) but for the most recent techniques, that's too complicated imo.

# How does the relationship of people shape the movie industry?
Question: how does the relationship of a team of directors, producers, writers, cinematographers influence the movie industry? By using a network graph and CMU IMDb DBpedia datasets, who are the most influential figures? s there any pattern in the success of a movie and the relationship of people among the production team? Is there any pattern in the emergence of a new star or the disappearance of a popular figure?

Discussion: where do we find data about the relationships? How do we characterize influence?

# Is she really acting or she is just being herself? ⭐
Certain actors and actresses are known to have performed diverse roles and different characters, while some are criticized for repeating themselves. By analyzing the characters and persona that have been portrayed by an actor or an actress, the importance of their role, their age at the time of the movie, potentially their personal state at the time, and a measure of their popularity or success, we can answer to the question whether there is a pattern in the career paths of actors and actresses in terms of the types of roles that they perform.

Discussion: actor popularity not directly available. Finding character types similar as the paper (use plot summaries and nlp data)

# How does the directorial style of directors evolve throughout their career?
Stanley Kubrick is known to have at least one great movie in every major movie genre. On the other hand, when you see David Fincher's name as the director of a new movie, you are almost sure that there is going to be one or more serial killers involved. But how is it for less-known directors? The directorial style of an average director evolves over time. Their experiences, their personal life, their emotional state, and many other factors might influence their style. It is not easy to put together all these factors, but we can analyze the types of movies that they have directed throughout their career and see if there are patterns in the career of a director. Several aspects such as the movie genre, the character types, the activity rate (e.g., movies per 5 years) of the director, the popularity of the movie cast, the budget of the movie, and the success of the movie can be analyzed.

## Feasibility of the idea : 
Now that we have the IMDb dataset, information about directors is available to use so data is not a problem anymore.
I would say that treating 'directorial style' might be a bit complicated : we have to really define that but it can be really interesting :

- We know that many directors have their favorite actors and that goes the other way around as well : how frequent is that ? Does that only concerns some specific type of films or some directors in particular industries (Bollwood,Hollwwood, etc.)

- How active are the directors in terms of movie production ? Does that correlate or is linked in some way with the success of the movies ?

- Are some directors 'opportunists' ? Can we find some directors that decided to cast, for their next film, only very popular actors at the time being ?

- Any others ?


# Gender equality in cinematography
Historically, cinema's portrayal of women was often confined within stereotypical boundaries. Females were restricted to roles that showcased them as housewives or love interests. However, as society progressed and the fight for gender equality gathered momentum and the cinematic universe began to reflect these shifts. Recent decades have witnessed an evident transformation in the roles assigned to women. No longer confined to the sidelines, females are now at the forefront, occupying central narratives, and frequently being portrayed as strong, independent, and intellectual characters. By analyzing the CMU corpus, we'll trace this evolution, marking gradual progression from peripheral roles to dominant narratives for women. We'll further evaluate the depth and diversity of these roles, ensuring that modern representations are not just quantitatively more but also qualitatively richer. Using external data sources like IMDb, we'll also assess the recognition of these roles in terms of awards, nominations, and critical acclaims. The goal is to highlight the cinematic journey of female characters from mere caricatures to comprehensive, multifaceted personalities that mirror the real-world evolution of women's roles in society.

TA remark: Great and complete idea, interesting to add the IMDb dataset! Minor comment: it could have been nice to be more precise on how you want to measure the depth and diversity of a role.

Discussion: similar to paper, would need to use the nlp data to find the types of female character (housewive, wonderwoman, ...)

## Feasibility of the idea : 

Same thing as for the very first idea, if we can not extract the personas then we can not do this idea


# Second idea: Influence of global events on movie plots
To gauge the impact of global happenings on cinema, we'll delve into the influences of wars, technological innovations, economic downturns, and even subtle governmental nudges. Historical events like the Cold War didn't just shape global politics but also cinematic narratives. Was there a spike in war-centric movies during such times or narratives where American protagonists found themselves fighting against foreign threats, suggesting possible governmental influence or propaganda? Moreover, with the advent of groundbreaking technology like CGI, did the film industry lean more towards alien invasions or space odysseys? And in times of economic crises, did cinema try to uplift spirits by churning out more comedies, offering a respite from real-world struggles? We could explore patterns in movie genres, plots, and even the nationalities of lead actors. Did certain global events lead to a particular nationality being more represented, or possibly even typecast, in specific roles? Were certain genres more predominant in specific decades due to overarching global sentiments?

TA remark: Good idea but you are not leveraging many of your ADA skills to answer this question. Try to be more creative on the data analysis part!

Discussion: no data on the timestamps for global events.

# Third idea: Globalization of movies
Explore the evolution of international film collaborations from their sparse existence at the dawn of the 20th century to the prolific global partnerships we witness today. By analyzing movies that have cross-border production teams or casts, is the democratization of these collaborations truly equitable? For instance, does the main cast predominantly hail from one nationality when a developed country collaborates with an emerging one? Do all nationalities get equal spotlight and access to awards? Are some nationalities stigmatized? Another intriguing facet is the global reach of cinema from various regions. While Hollywood films enjoy global viewership, other robust industries like Bollywood might not have the same global footprint. Why is there such a disparity, and how have these dynamics changed over time?

TA remark: Interesting question, especially the Hollywood/Bollywood comparison! Be careful although when comparing country-specific metrics such as awards that can be highly biased towards one country.

Discussion: dataset has a US country/English language bias.