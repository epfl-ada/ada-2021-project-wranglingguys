# Applied Data Analysis project - Milestone 2

## Title
How much does the politics scenario in one topic change from one country to another?

## Abstract
Who is the italian Donald Trump? Is the Democratic Party similar to German CDU?
Going from one country to another it can be difficult to keep track of the parties' issues. How much easier would 
it be if you have a comparison between politicans and parties in different countries. 
In this project we want to adress these and other questions related to political topics. 
The main goal is to examine how much one politic scenario in one topic change from one country to another. 
Taking into account the quotes of politicians, the main issues are obtained. This will then be used for further
studies like getting the most dividing topic of politicans in one country. Besides the parties of each politican
are taken into account. This allows questions to be explored, such as how much do parties differ in their topics
to a politically similar party.

## Research questions 
1. Where do politicans differ the most in dividing topics in one country?
2. Considering a party, how much do their opinion differ compared to a party with similar political 
   orientation from another country?
2. How much does a politican differ from his party? Which party is most divided/similar?
3. Who is the most similar politican taken from one country compared to another country?
4. Given a sentence, which party could have said this?
5. How much does a party differ in their opinion between 2015 to 2019?
6. (How successfull were parties which changed the most during these years?) 
7. How much does the politics scenario in one topic change from one country to another?

## Proposed additional datasets
1. Wikidata


## Methods 
1. NLP
2. Word2Vec/ Doc2Vec?
3. Sentiment analysis 


## Proposed timeline
1. Adjusting the pipeline of Milestone 2 for all years or several countries
2. Going through the research questions 
3. Visualizing the results


## Organization within the team
1. Look for the most political citations in one country, take the country with the most ones. -Alexis
1. Filter the citations out.
2. Prepare data for NLP (remove stop words) - use word2vec with library or textblock gensim for topics -Giovanni
3. When we have the vectors of the words, do the clustering (into topics)   - Andi
4. Select a topic. Do sentiment analysis on some quotes in this topic	-Simon
5. Visualize the results

## Questions for TAs


