# Personas regression model

[Training code](https://github.com/dbamman/ACL2013_Personas/tree/master)

### Pre-request

1. java

    ** I use java 8

## Train


```

git clone https://github.com/dbamman/ACL2013_Personas/tree/master

cd ../java

gunzip input/movies.data.gz

./run.sh $OUTPUT_DIRECTORY $INPUT
# ex. ./run.sh output input/movies.data

```

Can modify run.sh to change number of iteration and also other hyperparameters.

** The original run.sh is using zsh so the first line is #!/bin/zsh, change to #!/bin/bash if you do not have zsh shell.

## Data

if you do 

```
gunzip input/movies.data.gz

./run.sh $OUTPUT_DIRECTORY input/movies.data

```
It will train with all data. In order to save some time, you can train with a smaller subset. I have create a 5k data by using their code (preprocess). You can directely download it from google drive 'Personas Regression Model/input/5k.data' and put inside ../java/input and run 
```
./run.sh $OUTPUT_DIRECTORY input/5k.data
```

## Output

Below are outputs I got now. You can find them in google drive 'Personas Regression Model'

1. for_test

    A short test training with all data and 1000 iteration, just to have a look of how output look like.

2. 5k_10000

    Training with 5k data with 10000 iteration.

3. all_10000
    
    Training with all data with 10000 iteration.

4. 5k_50000

    Training with 5k data with 50000 iteration