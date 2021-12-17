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
    """
    Calculates an array containing intervall borders for setting bins in histograms. Each bin has the same size.

    :param number: number of bins.
    :param start: smallest value.
    :param end: biggest value.
    :return: array containing bin borders.
    """
    
    step_size = (end - start)
    steps = number
    
    bins = list()
    cur = start*number
    for i in range(number + 1):
        bins.append(cur)
        cur += step_size
    return [x/number for x in bins]




def show_top_k_speakers_party(party_name, df, k=10): 
    """
    Show the top k speakers of a party

    :param topic_name: name of the party.
    :param df: pandas dataframe containing the quotes.
    :param k: number of top speakers to show.
    """
    
    sns.set_context('notebook')
    
    # Filtered top 10 speakers
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
    plt.xlabel('Speaker / Party')
    plt.ylabel('Number of quotes')
    
    plt.title('%s - Top speakers in this party' % party_name)
    
    plt.show()
    
    return visualized_df


def show_avg_polarity_of_speaker_radar(speaker, df, topics, grid_int=None):
    """
    Plots a radar plot with one axis per topic showing the average polarity of this speaker.

    :param speaker: name of the speaker.
    :param df: pandas dataframe containing politicians and polarity scores per topic.
    :param topics: list of topics in the dataframe. The dataframe must contain columns containing the topics polarity scores following the first two columns.
    :param grid_int: 3-tuple defining the grid in which the subplot appears.
                        0: number of rows of the grid
                        1: number of columns of the grid
                        2: this is ith subplot (left to right, top to bottom)
                        if None, single plot.
    :return: plot ax to be added to a matplotlib figure.
    """
    
    #caclulate the grid int passed to sublot()
    if grid_int == None:
        i = 111
    else:
        i = grid_int[0]*100 + grid_int[1]*10 + 1 + grid_int[2]
        
    
    # number of categories
    categories=[x[:-13].title() for x in list(df)[2:]]
    N = len(categories)

    #list of vlaues for each axis
    values=df.query('speaker == @speaker').iloc[0][2:].tolist()
    values += values[:1]
    values

    #calculate angles of axises
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    #the radar plot
    ax = plt.subplot(i,  polar=True)

    # one axis per category and angle
    plt.xticks(angles[:-1], categories,  size=38)
    
    # calc min and max of scale
    start = min(df[[x + '_avg_polarity' for x in topics]].values.flatten())
    end = max(df[[x + '_avg_polarity' for x in topics]].values.flatten())
    
    #set scale of axises
    ax.set_rlabel_position(20)
    plt.yticks([start,0, end], [str(start),"0", str(end)],  size=40)
    plt.ylim(start,end)

    #plot the data per catagory
    ax.plot(angles, values, linewidth=10, linestyle='solid')

    #fill the area
    ax.fill(angles, values, 'b', alpha=0.1)
    
    ax.title.set_text(speaker)
    ax.title.set_fontsize(60)

    if grid_int == None:
        plt.show()
    else:
        return ax
    
    
    
def show_all_polarity_radar(df, topics, grid = (2,3)):
    """
    Plots a grid of radar plot with one axis per topic showing the average polarity the speakers.
    All politicians contained in df are plotted.
    grid must be a tuple defining a big enough grid for the number of rows in df.
    
    :param df: pandas dataframe containing politicians and polarity scores per topic.
    :param topics: list of topics in the dataframe. The dataframe must contain columns containing the topics polarity scores following the first two columns.
    :param grid: tuple defining the grid in which the subplot appears.
                        0: number of rows of the grid
                        1: number of columns of the grid
                        Default: 2x3
    """
    
    fig = plt.figure(figsize=(100, 50))
    
    
    fig.tight_layout()

    for i, politician in enumerate(df['speaker']):
        fig.add_subplot(show_avg_polarity_of_speaker_radar(politician, df.fillna(0), topics, grid_int=(grid[0], grid[1], i)))
        

        
        
def show_distr_speaker_topic(df, topics, quotes_by_topic, bin_number = 8):
    """
    Plots a grid of histogram plots, showing the distribution of polarity scores of each politician and each topic.
    All politicians contained in df  and topics contained in topics are plotted.
    
    :param df: pandas dataframe containing politicians and polarity scores per topic.
    :param topics: list of topics in the dataframe. The dataframe must contain columns containing the topics polarity scores following the first two columns.
                    Also the quotes_by_topic dict must contain a dataframe with quotes for each of the listed topics.
    :param quotes_by_topic: dict of dataframes containing the quotes belonging to each topic. KEys are the topics.
    :param bin_number: number of bins of same size to be used in all of the histograms.
    """
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