# Summary of "Learning Latent Personas of Film Characters" 
https://www.cs.cmu.edu/~dbamman/pubs/pdf/bamman+oconnor+smith.acl13.pdf
## Abstract
Paper presents two latent variable models for learning character types = *personas*. *Personas*: set of mixtures over latent lexical classes. Lexical classes capture attributes describing the character and the actions the character does ("agent") or is subject to ("patient"). 

**latent**: not directly observable or explicit, but is inferred or derived from the available data. Latent variables represent underlying, hidden factors that can explain observed patterns in the data. For instance, when analyzing film characters, their personalities or '*personas*' are not explicitly stated but can be inferred from their actions, dialogues, and interactions within the movie.

**lexical classes**: groups of words or phrases that share common characteristics, typically in terms of their meaning or usage. In the context of film characters, these could be groups of words that describe actions, emotions, attributes, etc.

**latent lexical classes**: These are groups of words or phrases that are not explicitly defined but are inferred from the data. They represent underlying themes or categories in the dialogue or descriptions of characters.

**set of mixtures**: This suggests a combination or blend of these inferred categories. In other words, a character's *persona* might be represented as a mix of different latent lexical classes. For example, a character might exhibit traits from a 'heroic' class (brave, courageous) and a 'comedic' class (funny, quirky).

**set of mixtures over latent lexical classes**: it means that each film character's personality is modeled as a combination of these inferred categories of words and phrases, which together represent their actions, attributes, and roles in the film. This approach allows for a more nuanced and complex understanding of characters beyond simple labels like "hero" or "villain."

## 1. Introduction
Debate: most important element of narrative is *plot* or *character*. Aristotle is for *plot*, Hollywood is for *character*. Paper will address the importance of *character* in defining a story: a character's latent internal nature drives the action we observe. 

**latent internal nature**: aspects of a character that are not immediately visible or explicit: motivations, desires, fears, beliefs, and personality traits.

**drives the action**:  latent (hidden or underlying) aspects are what motivate or cause the character to act in certain ways; character's behavior and decisions are a reflection of their internal state or nature.

**we observe**: audience or readers witness in the character's actions and story arc.

**character's latent internal nature drives the action we observe**: the actions and decisions of a character in a film or story are often driven by their internal characteristics and motivations, which may not be directly visible but can be understood through their behavior and the situations they encounter. This concept is crucial for creating depth and complexity in characters, making them more realistic and relatable to the audience.

Natural generative story: 
1. decide the kind of movie (e.g. romantic comedy), then 
2. decide on a set of character types or *personas*: `PROTAGONIST, LOVE INTEREST, BEST FRIEND`. 
3. Then, fill each of the roles with specific attributes: (female, 28 years old, clumsy). 
4. Then, sketch out the set of events by which they interact with the world and with each other: (runs but just misses the train, spills coffe on her boss), through which **characters reveal to the viewer the inherent qualities about themselves.**

Character-centric perspective leads to two questions:
1. can we learn what those standard personas (e.g. the hero, the villain, the mentor, the comic relief,...) are, by how individual characters are portrayed (examining individual characters—who are examples of these personas—and how they are depicted in films, one might be able to learn what the common traits and characteristics of each persona are. This includes looking at their actions, dialogues, roles in the story, and how they interact with other characters)?
2. can we learn the set of attributes and actions by which we recognize those common types? How do we, as viewers, recognize a `VILLIAN`?

Paper seeks a finegrained set that includes not only archetypes but also stereotypes (characters defined by a fixed set of actions widely known to be representative of class).

**Archetype**: universally recognized and recurring symbol, theme, or character type that appears across different cultures and time periods (Hero, the Trickster, the Mentor). Archetypes are not about specific characters but rather about the roles and symbolic meanings these character types represent. They are seen as universal, transcending specific cultural or temporal contexts.

**Stereotype**: simplified and fixed idea or image of a particular type of person or thing. Typically based on generalizations or assumptions about a group, class, or category of people. Can be based on cultural, social, or even prejudicial views. For example, the "nerdy scientist" or the "damsel in distress" are stereotypes that reflect simplified, widely recognized notions of these characters.

## 2. Data
### 2.1 Text (plot_summaries 2/11/2012 wiki dump and parquet files)
More popular movies have longuer plot summaries. With Stanford coreNLP: tag and syntactically parse the text, extract entities, and resolve coreference within the document.
**coreference**: relationship between words or phrases that refer to the same entity: "John went to the store. He bought milk.", "John" and "He" are in a coreference relationship: both words point to the same entity, John.

From the coreNLP results, extract linguistic features for each character:
- immediate verb governors: verbs that are directly associated with the character in the sentence structure. In syntactic parsing, a governor is a word that has dependents. "John kicked the ball," "kicked" is the verb governor for the subject "John."
- CCprocessed dependencies: specific syntactic relationships involving the character, each providing different insights:
    - Agent Verbs: These are verbs for which the entity (the character) is an agent argument. In syntactic terms like `nsubj` (nominal subject) or `agent`, these verbs indicate actions that the character actively performs. For example, in "Alice sings a song," "sings" is an agent verb for "Alice."
    - Patient Verbs: These verbs indicate where the entity is the patient, theme, or other argument. In terms like `dobj` (direct object), `nsubjpass` (passive nominal subject), `iobj` (indirect object), or `prep_*` (prepositional argument), these verbs show actions where the character is affected or involved in a more passive role. For example, in "The story fascinated Alice," "fascinated" is a patient verb for "Alice."
    - Attributes: These include adjectives and nouns that relate to the character, identifying their qualities or descriptions. They are linked to the character through syntactic roles like adjectival modifiers, noun-noun compounds, appositives, or copulas, involving dependencies like `nsubj`, `appos` governors or `nsubj`, `appos`, `amod`, or `nn` dependents of an entity. For instance, in "Brave Alice faced her fears," "Brave" is an attribute of "Alice."

These three roles capture three different ways in which character personas are revealed:
- actions they take on others
- actions done to them
- attributes by which they are described

For each character, paper extracts a bag of ($r$, $w$) tuples, $w$: word lemma, $r$: one of {agent verb, patient verb, attribute}.
### 2.2 Metadata (movie and character metadata 4/11/2012 freebase dump)
Across all 42'306 movies, entities average 3.4 agent events, 2.0 patient events and 2.1 attributes. Following experiments are restricted to events the are among the 1000 most frequent overall and characters with at least 3 events. Paper gets 120'345 characters, 33'559 from them can be matched to freebase actors with a specified gender and 29'802 to actors with a given date of birth. Average age at time of movie is 37.9 (standard deviation 14.1), 66.7% are males (note: this extreme 2:1 male/female ration reflects an inherent bias in film or a bias in attention on freebase). Age distribution is strongly bimodal when conditioning on gender: females: mean=33.0 s.d.=13.4, males: mean=40.5 s.d.=13.7.
## 3 Personas
One way to recognize a character's latent type is by observing the stereotypical:
- actions they do: VILLAINS *strangle*
- actions done to them: VILLAINS are *foiled* and *arrested*
- attributes that describe them: VILLAINS are *evil*

Paper defines a persona as a set of three typed distributions
- words for which character is *agent*
- words for which character is *patient*
- words by which charater is attributively modified

Each distribution ranges overa fixed set of latent word classes or *topics*. 

ZOMBIE persona example:
- agent: *eating* and *killing* actions
- patient of *killing* actions
- object of *dead* attributions
- topic labeled *eat* may include words like *eat*, *drink* and *devour*.

![Zombie example](https://i.postimg.cc/FHgCWwMT/image-2023-11-05-215720910.png)

## 4 Models
Both models have in common:
- soft clustering over words to tpoics (verb *strangle* is mostly a type of *Assault* word)
- soft clustering over topics to personars (VILLAINS perform a lot of *Assault* actions)
- hard clustering over characters to personas (Darth Vader is a VILLAIN)

First model: text only (plot summaries and XML files)

Second model: text + non textual information such as movie genre, age and gender.

### 4.1 Dirichlet Persona Model (text only model)
![first_model](https://i.postimg.cc/05DZQtqd/image-2023-11-06-183130800.png)

### 4.2 Persona Regression 
![second_model](https://i.postimg.cc/44WyzGZJ/image-2023-11-06-183420416.png)

![params](https://i.postimg.cc/2yRsWV6H/image-2023-11-06-183542540.png)

![results](https://i.postimg.cc/yYnG1fFp/image-2023-11-06-183707192.png)
