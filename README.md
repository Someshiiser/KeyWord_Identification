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

## Components of the project
Main file         -> Keyword_identification.ipynb
README.md         -> What theproject does.
keywords.db       -> DataBase created for without yake.
YAKE.db           -> DataBase created for with yake.
Testing.ipynb     -> Initial code testing.
testing_tan.ipynb -> Testing with the YAKE.


## Code Explanation

We start off by getting the html content from the urls the user enters using the $requests$ library . Next we parse the raw html data and getting only the string "text" part,
all of which is done using the $BeautifulSoup$ . After getting the text , we clean the text and make it more readable using the $re$ library.

The next step is to get the frequency of each word and store the data in a database. Once the data is stored in the database , we can use that to compare two or more 
websites. We define functions to find out what the top-20 words are according to the frequency, what are unique words are there in each site and wto hat are common words
in the sites we compare. One can add more functions for further analysis. We then visualize the data through bar graphs, word clouds and tree maps.


The program file  Keyword_identification.ipynb  has beautifully written comments , explaining each and every line and what it does. Refer to the comments ,if one ever
gets confues.

Here we use the frequencies of the words as a parameter for  Keyword Identification , implying the higher the frequency of a word the more relevant it becomes. But this
method is not reliable for getting meaningful keywords as frequencies of words like and , of , etc are very high , and using  these words as keywords does not make any sense.
So for the next step we change our approach and use $YAKE$ algorithm instead of relying just on the frequencies and analyze the data we get from that.

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
This score is used for further analysis and serves as a replacement for frequencies , providing more meaningful keywords than the previous method.


### Quick Installation
Yake is not included in the python module , so you have to manually install it first.




         pip install yake






### Citation

To know more about Yake check their  Documentation site: https://liaad.github.io/yake/docs/--home  and  github: https://github.com/LIAAD/yake.git 

         
