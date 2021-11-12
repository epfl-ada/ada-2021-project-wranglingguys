# Applied Data Analysis project - Milestone 2

## Title
How much does the politics scenario in one topic change from one country to another?

## Abstract
Who is the italian Donald Trump? Is the Democratic Party similar to German CDU?
It can be difficult, moving from one country to another, keeping track of the parties' issues. It would be a huge help if you have a comparison between politicans and parties w.r.t. different countries. 
In this project we want to adress these and other questions related to political topics. 
The main goal is to examine how much one politic scenario in one topic change from one country to another. 
Taking into account the quotes of politicians, the main topics are obtained. This will then be used for further
studies like getting the most dividing topic of politicans in one country. Besides the parties of each politican
are taken into account. This allows questions to be explored, such as how much do parties differ in their topics
to a political similar party.

## Research questions 
1. Where do politicans differ the most in dividing topics in one country?
2. Considering a party, how much do their opinion differ compared to a party with similar political 
   orientation from another country?
2. How much does a politican differ from his party? Which party is most divided/similar?
3. Who is the most similar politican taken from one country compared to another country?
4. Given a sentence, which party could have said this?
5. How much does a party differ in their opinion between 2015 to 2019?
6. (How successful were parties which changed the most during these years?) 
7. How much does the politics scenario in one topic change from one country to another?

## Proposed additional datasets
1. Wikidata: Extract political party related to the speakers, extract political orientation of parties


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
