# KeyWord_Identification


## Description
Keyword identification (or keyphrase extraction) means automatically identifying the most important words or phrases in a text.
When you have tons of documents, articles, or messages, like for example : in research papers, it’s impossible to read everything.
Keyword extraction highlights what each text is about in seconds.
Search engines use keywords to index and rank content.
Keyword identification helps match queries with relevant documents, for example: When you Google “AI image generation,” it finds pages whose extracted keywords match those terms.





This project extracts, cleans, analyzes, and visualizes keywords from websites.
It uses web scraping, text cleaning, frequency analysis, and YAKE (Yet Another Keyword Extractor) to identify significant words from webpages.
It also stores the extracted keywords and their frequencies in an SQLite database, allowing comparisons across multiple websites with plots and word clouds.



## Yake
YAKE is a lightweight unsupervised automatic keyword extraction method that uses text statistical features to select the most important keywords from a document. 
It requires no training, external corpus, or dictionaries, and works across multiple languages and domains regardless of text size.


For each candidate word, YAKE calculates 5 key features:

  .Casing — is it capitalized unusually often?
  
  .Word position — early or late in text (earlier = more important).
  
  .Word frequency — rare words get higher importance.
  
  .Context diversity — if a word appears in many contexts, it’s less specific.
  
  .Sentence relatedness — words occurring close together might form a phrase.

  
  
Each candidate gets a combined score based on the above features. Lower score → more relevant keyword.
