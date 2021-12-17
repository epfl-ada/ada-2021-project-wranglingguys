# Applied Data Analysis project - Milestone 3

## Title
How much does the political scenario change from one country to another?



## Data story
To read our data story, click <a href='https://simon01239.github.io/ada/'>here</a>.



## Abstract
Europe, 2019. It appears that right-wing populists are on the rise in many countries. However, is it possible to compare these parties between countries? What do they have in common? How do they differ? What is the general political orientation on controversial themes in different countries? What is the position of the leading politicians on these themes? Is ‘Alternative for Germany’ similar to ‘Lega Nord’? 

Therefore, we will take a short journey through the different political topics. For this purpose, we will focus on some of the largest countries in the European Union: France, Germany, Italy, Spain and Poland.

Taking into account the quotes and the party of politicians, we will examine and compare the hottest topics in each country.

Besides, we will investigate how politicians from different countries position themselves over the same topics, especially if they come from the same political background (i.e. right parties).



## Research questions 
1. How much does the political scenario in some hot topics (for example immigration, climate change, EU, discrimination, Israeli-Palestinian conflict, Russia, terrorism and Covid-19) change from one country to another? Why is that?
2. Considering the most important parties of these countries, how much do their opinions and interest differ over these topics?
3. How do the important politicians of the right-wing parties position themselves over the same topics? What can we observe if we compare them with the heads of government in the same countries?

## Proposed additional datasets
Wikidata: we use wikidata to extract political party related to the speakers and political orientation of parties. This data is necessary as we need to filter politicians, to associate politicians with parties and parties with political orientations. 



## Methods 

### General explanation

In order to answer the research questions we implemented the pipeline as follows:

1. With Wikidata, filter the quotes by politicians from the original Quotebank dataset.
2. Train a Top2Vec model based on the subset of quotes we use.
3. Create a new dataset of quotes per topic. 
4. Use sentiment analysis on the quotes to get the „opinion direction“ expressed about the topics.

The steps from 1. to 3. are performed in the preliminary data analysis and the first research question parts.
The fourth is performed for the other research questions respectively at the party-level and the politician-level.

### Techniques and libraries

Quotes embedding: we use <a href=''>Top2Vec</a>, which learns a joint embedding encoding both the semantic of the words as well as their order in the document. 

Topic Extraction: we follow the approach of Top2Vec. So we use UMAP for dimensionality reduction of the embedding vectors and HDBSCAN for the final clustering.

Sentiment Analysis: we use <a href='https://github.com/cjhutto/vaderSentiment'>VADER</a> to extract the polarity of quotes.



## Proposed timeline

### First week: finalize the working tools
During this week, we improve the project datails with the feedback from milestone 2 and finalize our working tools.

In particular, we will improve the clustering results and the vector representation of quotes (Andreas and Giovanni).<br>
Also, we will improve the results of sentiment analysis (Simon).<br>
In addition, we will address some problems in the wikidata dataset, such as politicians with more associated parties (Alexis).

The aim of this week is to finalize all the working tools so that we can focus on the actual research questions during the second one.

### Second week: work on the research questions
During the second week, we will use the finalized working tools to answer our research questions.
In particular, the first research question (Giovanni) has to be done first for the others to be started, as we need the topics datasets.
Then, the second research question (Alexis) and the third one (Andreas) will be answered in parallel.

### Third week: finalize the results and prepare the presentation
During this week, we will put it all together and prepare the data story and the final presentation (Simon).

## Organization within the team

- Alexis: data preprocessing, third research question.
- Andreas: finding a way to represent politicians by their sentiments over topics, second research question.
- Giovanni: finding a way to distinguish the topics, first research question.
- Simon: writing up the data story, preparing the final presentation.

## Code organization 
Files:
```markdown
├── README.md: this file.
├── milestone3.ipynb: notebook with the third milestone of the project.
└── src
   ├── sentiment_analysis.py: helpers functions used to carry out sentiment anaylsis.
   └── data_wrangling
      ├── filter_politicians_quotes.py: script to filter only the quotes from the politicians.
      ├── generate_political_party_dataset.ipynb: notebook with the steps to generate the political party dataset.
      ├── load_data.py: helper functions that load the politician dataset given some filters.
      └── wikidata_fetch.py: functions to enrich the current dataset by pulling extra information about the speakers from the wikidata.
└── scripts
   ├── research_question_1.py: helper functions used for the first research question
   └── research_question_3.py: helper functions used for the third research question
```
