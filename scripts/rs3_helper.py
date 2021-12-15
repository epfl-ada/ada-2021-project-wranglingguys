import pandas as pd
from top2vec import Top2Vec
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from src.data_wrangling.load_data import load_political_quotes

from textblob import TextBlob
from src.sentiment_analysis import get_subjectivity, get_polarity, get_sentiment

from math import pi
import matplotlib.gridspec as gridspec

def bins_equidistant(number, start, end):
    step_size = (end - start)
    steps = number
    
    bins = list()
    cur = start*number
    for i in range(number + 1):
        bins.append(cur)
        cur += step_size
    return [x/number for x in bins]


# Distribution of top speakers
def show_top_k_speakers_party(topic_name, df, country = None, k=10):
    sns.set_context('notebook')
    # Filtered top 10 speakers
    if country is None:
        series = df['speaker']
    else:
        series = df['speaker']

    series = series.groupby(series).count()
    visualized_df = pd.DataFrame({'speaker': series.index,
                        'counts': series.values
                       }, columns = ['speaker','counts'])
    visualized_df = visualized_df.sort_values('counts', ascending=False).head(k)
    fig, ax = plt.subplots(figsize = (14,6))
    palette = sns.color_palette("mako")
    sns.barplot(x="speaker", y="counts", data=visualized_df,
                      ci = None, ax=ax, palette=palette)
    ax.set_xticklabels(labels=visualized_df['speaker'], rotation=60, ha='right')
    plt.xlabel('Speaker / Party (Country)')
    plt.ylabel('Number of quotes')
    if country is None:
        plt.title('%s - Top speakers in this party' % topic_name)
    else:
        plt.title('%s - Top speakers in this party' % (topic_name, country))
    plt.show()
    
    return visualized_df


# Distribution of top speakers
def show_avg_polarity_of_speaker(speaker, df, topics):
    sns.set_context('notebook')


    series = df.query('speaker == @speaker')[[t + '_avg_polarity' for t in topics]].iloc[0]
    visualized_df = pd.DataFrame({'topic': topics,
                        'polarity': series.values
                       }, columns = ['topic','polarity'])
    
    fig, ax = plt.subplots(figsize = (14,6))
    palette = sns.color_palette("mako")
    sns.barplot(x="topic", y="polarity", data=visualized_df,
                      ci = None, ax=ax, palette=palette)
    ax.set_xticklabels(labels=visualized_df['topic'], rotation=60, ha='right')
    plt.xlabel('Speaker / Party (Country)')
    plt.ylabel('Number of quotes')
    
    plt.title('%s - Top speakers in this party' % speaker)
   
    plt.show()
    
    return visualized_df




def show_avg_polarity_of_speaker_radar1(speaker, df, topics, grid_int=None):
    
    if grid_int == None:
        i = 111
    else:
        i = grid_int[0]*100 + grid_int[1]*10 + 1 + grid_int[2]
        
    
    # number of variable
    categories=[x[:-13].title() for x in list(df)[2:]]
    N = len(categories)

    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    values=df.query('speaker == @speaker').iloc[0][2:].tolist()
    values += values[:1]
    values

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(i,  polar=True)

    # Draw one axe per variable + add labels
    plt.xticks(angles[:-1], categories,  size=38)#color='grey',
    
    #scale
    start = min(df[[x + '_avg_polarity' for x in topics]].values.flatten())
    end = max(df[[x + '_avg_polarity' for x in topics]].values.flatten())
    steps = 2 
    bins = bins_equidistant(start=start, end=end, number=steps)
    
    # Draw ylabels
    ax.set_rlabel_position(20)
    plt.yticks([start,0, end], [str(start),"0", str(end)],  size=40)#[start,0, end] [str(start),"0", str(end)] #[start,0, end], [str(start),"0", str(end)]
    plt.ylim(start,end)

    # Plot data
    ax.plot(angles, values, linewidth=10, linestyle='solid')

    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)
    
    ax.title.set_text(speaker)
    ax.title.set_fontsize(60)

    # Show the graph or return it
    if grid_int == None:
        plt.show()
    else:
        return ax
    
    
    
def show_all_polarity_radar(df, topics, grid = (2,3)):
    
    
    fig = plt.figure(figsize=(100, 50))
    
    
    fig.tight_layout()

    for i, politician in enumerate(df['speaker']):
        fig.add_subplot(show_avg_polarity_of_speaker_radar1(politician, df.fillna(0), topics, grid_int=(grid[0], grid[1], i)))
        
#distr_topics_politician
def show_distr_speaker_topic(df, topics, quotes_by_topic, bin_number = 8):
    fig, axes = plt.subplots(len(df),len(topics), figsize=(15,15), sharex=True, sharey=False)
    fig.tight_layout()

    bins = [x/10 for x in range(-10,11)]
   
    for i, speaker in enumerate(df['speaker']):
        for j, topic in enumerate(topics):
            
            axes[i][j].hist(quotes_by_topic[topic].query('speaker == @speaker')['polarity'], bins=bins_equidistant(bin_number,-1,1))

    for j in range(len(topics)):
        axes[0][j].set_title(topics[j])

    for i in range(len(df)):
        axes[i][0].set_ylabel(df['speaker'].iloc[i], rotation=90, size='large')