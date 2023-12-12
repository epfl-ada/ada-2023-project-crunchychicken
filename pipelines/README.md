# NLP Pipelines Explained

The goal is to extract latent personas from the [CMU movie summaries](https://www.cs.cmu.edu/~ark/personas/#:~:text=Dataset%20%5B46%20M%5D%20and%20readme%3A%2042%2C306%20movie%20plot%20summaries) using a similar approach as described in [*Learning Latent Personas of Film Characters*](https://www.cs.cmu.edu/~dbamman/pubs/pdf/bamman+oconnor+smith.acl13.pdf) by David Bamman Brendan O’Connor Noah A. Smith. 


## 1st Approach: Stanford CoreNLP-processed summaries from CMU Movie Summary Corpus

The CMU Movie Summary Corpus dataset contained a supplement: [Stanford CoreNLP-processed summaries (628 MB)](https://www.cs.cmu.edu/~ark/personas/#:~:text=Supplement%3A%20Stanford%20CoreNLP%2Dprocessed%20summaries%20%5B628%20M%5D). This tar archive contains 42'306 `.xml.gz` files, each corresponding to a movie summary processed through the Stanford CoreNLP pipeline (including tagging, parsing, NER, and coreference resolution).

The files have the following XML structure:
```
root
│ document
│ │ sentences
│ │ │ sentence id
│ │ │ │ tokens
│ │ │ │ │ token id
│ │ │ │ │ │ word
│ │ │ │ │ │ lemma
│ │ │ │ │ │ char offset begin
│ │ │ │ │ │ char offset end
│ │ │ │ │ │ POS
│ │ │ │ │ │ NER
│ │ │ │ parse
│ │ │ │ basic-dependencies
│ │ │ │ │ dep
│ │ │ │ │ │ governor
│ │ │ │ │ │ dependent
│ │ │ │ collapsed-dependencies
│ │ │ │ │ dep
│ │ │ │ │ │ governor
│ │ │ │ │ │ dependent
│ │ │ │ collapsed-ccprocessed-dependencies
│ │ │ │ │ dep
│ │ │ │ │ │ governor
│ │ │ │ │ │ dependent
│ │ coreference
│ │ │ coreference
│ │ │ │ mention
│ │ │ │ │ sentence
│ │ │ │ │ start
│ │ │ │ │ end
│ │ │ │ │ head
```

![2013 Explanation Image](https://i.postimg.cc/5yZsSVFd/image-2023-12-12-213128256.png)