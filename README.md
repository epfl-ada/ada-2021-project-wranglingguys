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
1. How much does the politics scenario in one topic change from one country to another?
2. Considering a party, how much do their opinions differ compared to a party with similar political 
   orientation from another country?
3. Who is the most similar politician taken from one country compared to another country?
4. Are the hottest topics of debate the same over different countries? If not, why is that?

## Proposed additional datasets
1. Wikidata: Extract political party related to the speakers, extract political orientation of parties.


## Methods 
1. NLP
2. Word2Vec
3. Clustering
4. Sentiment analysis: We used *TextBlob* to extract the polarity of quotes. It is a library for Natural Language Processing (NLP) and can be used for complex analysis on textual data.


## Proposed timeline
1. Filtering the data for political quotes
2. Merging Wikidata with Quotebank
3. Maybe doing a more in depth analysis of the quotes w.r.t. to different countries (length of quotes(number of words in quotes), distribution of number of quotes per day) ??
Also cleaning the data (e.g. Removing duplicates)
4. Vectorization of data (Word2Vec)
5. Answering the research questions in the order above by using the gained data of previous steps

## Organization within the team
1. Look for the most political citations in one country, take the country with the most ones. -Alexis
1. Filter the citations out.
2. Prepare data for NLP (remove stop words) - use word2vec with library or textblock gensim for topics -Giovanni
3. When we have the vectors of the words, do the clustering (into topics)   - Andi
4. Select a topic. Do sentiment analysis on some quotes in this topic	-Simon
5. Visualize the results

## Questions for TAs

## Code organization ?? 
Files:
* notebook.ipynb: notebook with in depth analysis of the data that we need
* 
