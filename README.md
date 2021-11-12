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
2. Word2Vec: we 
3. Clustering
4. Sentiment analysis: We used *TextBlob* to extract the polarity of quotes. It is a library for Natural Language Processing (NLP) and can be used for complex analysis on textual data.


## Proposed timeline and organization within the team

### First week: finalize the working tools
During this week, we will improve and finalize our working tools.
During the Milestone 2, we tried to map the quotes in a Word2Vec representation by just averaging the words. 
We realized this did not work well with 

### Second week: work on the research questions
During the second week, we will use the finalized working tools to answer our research questions.

### Third week: finalize the results and prepare the presentation
During this week, we will put it all together and prepare the final presentation.

## Questions for TAs

## Code organization 
Files:
```markdown
├── README.md: this file.
├── milestone2.ipynb: prototype of our project, with the preparation of the politicians dataset, the clustering and the sentiment analysis.
└── src
   ├── sentiment_analysis.py: helpers functions used to carry out sentiment anaylsis.
   ├── word2vec.py: helpers functions necessary to map the quotes in vector representation.
   └── data_wrangling
      ├── filter_politicians_quotes.py: 
      ├── generate_political_party_dataset.ipynb
      ├── load_data.py:
      └── wikidata_fetch.py:
```
