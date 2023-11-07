# Hidden connections in the film production industry

?? where do we find data about the relationships? How do we characterize influence?

## Abstract
The production of a movie involves a collaboration between a variety of roles for a relatively long period of time, and they all influence the success of the movie. The quality of the plot and the acting are of course an important factor, but there are details that are often more difficult to discern. When a team of directors, producers, writers, cinematographers, etc. collaborate, the result is more than just one movie. They build a relationship, good or bad, and it will influence their future projects and decisions. By building a network graph of the relationship of the most important people in the movie industry (using the CMU, IMDb, and DBpedia datasets), we can analyze it to get more insights about how these relationships have influenced the industry.

## Research questions
- Who are the most influential figures? Are there names that appear more than the others in major projects?
- Are there hidden factors about the presence of people and the success of the movie?
- Is there any pattern in the success of a movie and the relationship of people among the production team?
- Are there such things as *winning teams*? I.e., are there some combinations that have always been successful?
- Is there any pattern in the emergence of a new star or the disappearance of a popular figure? Here, we are looking for the hidden influence of managers and investors in the lifetime of a star.
- *Potentially some other questions from Arthur's idea*

## Proposed additional datasets
Proposed additional datasets (if any): List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.

### IMDb non-commercial datasets

Available [here](https://developer.imdb.com/non-commercial-datasets/).
*... add stuff ...*


## Methods
- What defines a relationship: Could be # of collaborations (movies made together), could be weighted by the total duration of the project.
- A separate graph can be made for the managers of the actors, if we can find the data anywhere.
- *Graph-related stuff? add some*

## Proposed timeline
*... add ...*


## Organization within the team
- Check feasibility of the idea
- Clean both datasets
- Merge the datasets
- Define the relationship and edge weights
- Create the global graph and store it
- Explore the graph and find interesting insights from it
- Address the research questions asked in the proposal
- Prepare the content and graphs
- Write the stroy


## Questions for TAs
- Are we obliged to use the plot summaries and the NLP skills in the project? The plot summaries do not really fit into this idea.


# The related ideas (*to be removed*)

## How does the relationship of people shape the movie industry?
The production of a movie involves a collaboration between a variety of roles for a relatively long period of time, and they all influence the success of the movie. The quality of the plot and the acting are of course an important factor, but there are details that are often more difficult to discern. When a team of directors, producers, writers, cinematographers, etc. collaborate, the result is more than just one movie. They build a relationship, good or bad, and it will influence their future projects and decisions. By building a network graph of the relationship of the most important people in the movie industry (using the CMU, IMDb, and DBpedia datasets), we can analyze it to get more insights about how these relationships have influenced the industry. Who are the most influential figures? Is there any pattern in the success of a movie and the relationship of people among the production team? Is there any pattern in the emergence of a new star or the disappearance of a popular figure?

## Globalization of movies
Explore the evolution of international film collaborations from their sparse existence at the dawn of the 20th century to the prolific global partnerships we witness today. By analyzing movies that have cross-border production teams or casts, is the democratization of these collaborations truly equitable? For instance, does the main cast predominantly hail from one nationality when a developed country collaborates with an emerging one? Do all nationalities get equal spotlight and access to awards? Are some nationalities stigmatized? Another intriguing facet is the global reach of cinema from various regions. While Hollywood films enjoy global viewership, other robust industries like Bollywood might not have the same global footprint. Why is there such a disparity, and how have these dynamics changed over time?
