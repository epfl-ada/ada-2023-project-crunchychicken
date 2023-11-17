Dropping some comments while going through the notebook..

> No major issues in general. No problem if you ignore all my comments.

> I didn't touch the file to avoid merge conflicts.

1. I would add the title that we will choose to the beginning of the project instead of "Data wrangling ..."

2. Table of content great and beauitful to have it in markdown. Minor thing: clicking on the items doesn't work perfectly for me (maybe it's my editor). I've never done this before but maybe you know an easy fix.

3. Small bug in readers (line 124) caused import error.


# 1. The CMU Movie Corpus

## 1.1

#### The CMU Movie Plot Summaries dataset

4. It's hard to read the numbers. I would plot it horizontally (replace `violinplot` with `boxplot` if you don't like it):
```python
fig, ax = plt.subplots(figsize=(12, 2))
g = sns.violinplot(cmu_summaries['Plot Summary'].apply(len), orient='h', ax=ax, gridsize=1000)
ax.set(ylabel='Length', xlabel='Frequency');
ax.set_yticklabels('');
```

#### The CMU Movies & Characters dataset

5. We can add some words about the fact that we also treat specific columns in `readers`. The instructors might be too lazy to go and read our helper codes.

6. Okay, this kind of manual correction will be totally accepted I think! I was wrong earlier I didn't know what the issue was originally.

7. Forget it if it makes the rest of the notebook unusable but consider treating datetime like this:

```python
cmu_movies['Movie release date'] = pd.to_datetime(cmu_movies['Movie release date'], format='mixed', errors='coerce')
cmu_characters['Movie release date'] = pd.to_datetime(cmu_characters['Movie release date'], format='mixed', errors='coerce')
```

> Year, month, day would still be easily accessible: `cmu_movies['Movie release date'].dt.year`

8. Same for `"Actor DOB"`. The "T" character is part of an established datetime format but I don't know the name. I think `pd.to_datetime` will handle it automatically for us.

### 1.2 Insights on CMU's metadata state

####  Exploring the movies dataset

## 2. The IMDb data

9. Use this for reading the CSV files:

```python
imdb_people = read_dataframe(name='imdb/names')
imdb_info = read_dataframe(name='imdb/movies')
imdb_principals = read_dataframe(name='imdb/principals')
imdb_ratings = read_dataframe(name='imdb/ratings')
```

##### IMDb principals

10. Let's either use grids in both or not at all. Bob mentioned in one of the lectures to avoid unnecessary grids, so I would remove the grid. Maybe only horizontal grids but on the background?

## 3. Merging the CMU & IMDb metadata

### 3.1 Crawling Wikipedia and querying Wikidata to construct a mapping

11. We don't need to see all the extra columns in this table, or maybe not the whole table. Consider replacing the cell with this:

```python
duplicates_01 = pd.merge(left=duplicates_01, right=cmu_movies[['Wikipedia movie ID', 'Movie name']], left_on='wikipedia', right_on='Wikipedia movie ID',how='left').sort_values(by='imdb')
duplicates_01['url'] = duplicates_01.wikipedia.apply(lambda pageid: wikipedia.page(pageid=pageid).url)
display(duplicates_01, display_id=False)
```
