# Applied Data Analysis project - Milestone 2

## Title
How much does the political scenario change from one country to another?

## Abstract
Who is the Italian Donald Trump? Is the Democratic Party similar to German CDU?

It can be difficult, moving from one country to another, keeping track of the parties' issues. It would be a huge help if you have a comparison between politicians and parties with respect to different countries. 
In this project we want to address these and other questions related to political topics. 

The main goal is to examine how much the political scenario in one topic changes from one country to another. 
Taking into account the quotes and the party of politicians, we will discover the hottest topics in each country and compare them to the ones of other countries.

Besides, we will investigate how politicians from different countries position themselves over the same topics, especially if they come from the same political background (i.e. right parties, left parties), by analyzing the similarities and the differences.

## Research questions 
1. How much does the political scenario in some hot topics (migration, climate change, EU, gender discrimination, drug legalization, russian politician) change from one country to another? Why is that?
2. Considering rigth-hand parties (AfD(Germany), Lega Nord(Italy), Front National(France), PiS(Poland), UKIP(UK)), how much do their opinions differ compared to a party with similar political orientation from another country?
3. How do the important politicans of these parties positioning themselves over topics (migration, climate change, EU, gender discrimination, drug legalization, russian politician)? 

## Proposed additional datasets
Wikidata: we use wikidata to extract political party related to the speakers and political orientation of parties. This data is necessary as we need to filter politicians, to associate politicians with parties and parties with political orientations. 


## Methods 
For research question 1:
Find a way to get the quotes of migration, climate change, EU, gender discrimination, drug legalization, russian politician of Germany, Italy, France, Poland and UK. 
Examine the distribution of these topics in the countries and over time.

For research question 2:
For each topic we do the plots of the sentiment analysis and highlight quotes from different parties with different colours. 
Then for each topic we can create a boxplot showing the sentiment analysis distribution per country.

For research question 3:
Compute for each politican and for each topic the average sentiment and compare them. Find the politicans who are more similar. 


In order to answer the research questions we plan to implement pipeline as follows:

1. Extract suitable subsets from the quote dataset
2. Embed the quotes as vectors
3. Extract the topics covered by the quotes
4. Use sentiment analysis on the quotes to get the „opinion direction“ expressed about the topic.

Embedding: we currently use Doc2Vec, which learns a joint embedding encoding both the semantic of the words as well as their order in the document. Although we might switch to another pretrained embedding model, like Word2Vec, that we already implemented. In particular, for Word2Vec, with *gensim* we load a pre-trained Word2Vec model. Then, we pre-process each quote and we average all the words with their TF-IDF score.

Topic Extraction: We follow the approach of Top2Vec. So we use UMAP for dimensionality reduction of the embedding vectors and HDBSCAN for the final clustering.

Sentiment Analysis: we use TextBlob to extract the polarity and subjectivity of quotes.


## Proposed timeline and organization within the team

### First week: finalize the working tools
During this week, we will improve and finalize our working tools.

In particular, we will improve the clustering results and the vector representation of quotes (Andreas and Giovanni).<br>
Also, we will improve the results of sentiment analysis (Simon).<br>
In addition, we will address some problems in the wikidata dataset, such as politicians with more associated parties (Alexis).

The aim of this week is to finalize all the working tools so that we can focus on the actual research questions during the second one.

### Second week: work on the research questions
During the second week, we will use the finalized working tools to answer our research questions.
We will work together on all the questions 


### Third week: finalize the results and prepare the presentation
During this week, we will put it all together and prepare the final presentation.

## Code organization 
Files:
```markdown
├── README.md: this file.
├── milestone2.ipynb: prototype of our project, with the preparation of the politicians dataset, the clustering and the sentiment analysis.
└── src
   ├── sentiment_analysis.py: helpers functions used to carry out sentiment anaylsis.
   ├── word2vec.py: helpers functions necessary to map the quotes in vector representation.
   └── data_wrangling
      ├── filter_politicians_quotes.py: script to filter only the quotes from the politicians.
      ├── generate_political_party_dataset.ipynb: notebook with the steps to generate the political party dataset.
      ├── load_data.py: helper functions that load the politician dataset given some filters.
      └── wikidata_fetch.py: functions to enrich the current dataset by pullin extra information about the speakers from the wikidata.
```
