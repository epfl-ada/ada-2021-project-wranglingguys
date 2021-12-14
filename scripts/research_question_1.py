import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


### FUNCTIONS FOR TOPIC EXTRACTION

def filter_quotes_by_custom_topic(dataframe, top2vec_model, topic_keywords, similarity_threshold=0.22):
    """
    Given a dataframe and a top2vec model, filter the quotes by their similarity with a certain topic, represented as a set of key words.
    :param dataframe: pandas dataframe containing the quotes.
    :param top2vec_model: Top2Vec trained model.
    :param topic_keywords: keywords representing the topic.
    :param similarity_threshold: cosine-similarity threshold for a quote to be considered about the topic.
    :return:
    """
    doc_words, document_scores, document_ids = top2vec_model.search_documents_by_keywords(keywords=topic_keywords,
                                                                                          num_docs=len(dataframe))
    positions = np.argwhere(document_scores > similarity_threshold).flatten()
    print("There are %d quotes above the threshold %.2f for the topic with the following keywords: %s" % (
    len(positions), similarity_threshold, topic_keywords[0]), end='')
    for keyword in topic_keywords[1:]:
        print(", %s" % keyword, end='')
    print(".")
    return dataframe[dataframe.index.isin(document_ids[positions])]


### FUNCTIONS FOR VISUALIZATION

# Distribution over time
def show_time_distribution(topic_name, df):
    """
    Show the distribution over time of the topic in all the countries.

    :param topic_name: name of the topic.
    :param df: pandas dataframe containing the quotes.
    """
    sns.set_context('notebook')
    series = df["date"].dt.strftime('%Y-%b')
    series = series.groupby(series).count()
    date_range = pd.date_range('2015-01-01', '2020-04-01',
                               freq='MS').strftime("%Y-%b")
    series = series.reindex(date_range, fill_value=0)

    visualized_df = pd.DataFrame({'dates': series.index,
                                  'counts': series.values
                                  }, columns=['dates', 'counts'])

    fig, ax = plt.subplots(figsize=(20, 8))
    sns.barplot(x="dates", y="counts", data=visualized_df, color='cadetblue',
                ci=None, ax=ax)
    ax.set_xticklabels(labels=visualized_df['dates'], rotation=45, ha='right')
    # Add title and axis names

    plt.xlabel('Year - Month')
    plt.ylabel('Number of quotes')
    plt.title('%s - Distribution of quotes over time in all countries' % topic_name)
    plt.show()


def show_time_distribution_per_country(topic_name, df, countries_list):
    """
    Show the distribution over time of the topic per country.

    :param topic_name: name of the topic.
    :param df: pandas dataframe containing the quotes.
    :param countries_list: list of the countries.
    """
    sns.set_context('talk')
    df2 = df.copy(deep=True)
    df2["date"] = df["date"].dt.strftime('%Y-%b')
    date_range = pd.date_range('2015-01-01', '2020-04-01',
                               freq='MS').strftime("%Y-%b").tolist()

    sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0), 'axes.linewidth': 3})
    palette = sns.color_palette("mako")
    g = sns.FacetGrid(df2, palette=palette, row="country", row_order=countries_list, hue="country", aspect=10, height=2,
                      sharey=False)
    g.map_dataframe(sns.countplot, x="date", order=date_range, alpha=0.8)
    g.set(yticks=[], yticklabels=[], ylabel=None, xlabel="Date")
    for axes in g.axes.flat:
        _ = axes.set_xticklabels(axes.get_xticklabels(), rotation=45, ha='right')

    def label(x, color, label):
        ax = plt.gca()
        ax.text(-0.04, .2, label, color='black', fontsize=13,
                ha="left", va="center", transform=ax.transAxes)

    g.map(label, "country")
    g.fig.subplots_adjust(hspace=-.1)
    g.set_titles("")
    g.despine(left=True)
    plt.suptitle('%s - Number of quotes over time per country' % topic_name, y=0.98)
    plt.xlabel('Date')


# Distribution of political orientation
def show_political_orientation_distribution(topic_name, df):
    """
    Show the distribution of the quotes per political orientation in all the countries.

    :param topic_name: name of the topic.
    :param df: pandas dataframe containing the quotes.
    """
    sns.set_context('notebook')
    political_alignments = ['far-left', 'radical left', 'left-wing', 'centre-left',
                            'centrism', 'centre-right', 'right-wing', 'far-right',
                            'national conservatism', 'nationalism', 'liberalism', 'Third Way', 'syncretic politics',
                            None]

    series = df.groupby(['political_alignment'])['political_alignment'].count()
    series = series.reindex(political_alignments)
    series = series.dropna()
    visualized_df = pd.DataFrame({'political_alignment': series.index,
                                  'counts': series.values
                                  }, columns=['political_alignment', 'counts'])
    palette = sns.color_palette("mako")
    fig = sns.catplot(x='political_alignment', y='counts', kind="bar", palette=palette, data=visualized_df)
    plt.xlabel('Political alignment')
    plt.ylabel(None)
    plt.title('%s - Number of quotes over political alignments in all countries' % topic_name)
    fig.set_xticklabels(labels=visualized_df['political_alignment'], rotation=45, ha='right')
    fig.set_yticklabels([])
    sns.despine(left=True)
    plt.show()


def show_political_orientation_distribution_per_country(topic_name, df, countries_list):
    """
    Show the distribution of the quotes per political orientation per country.

    :param topic_name: name of the topic.
    :param df: pandas dataframe containing the quotes.
    :param countries_list: list of the countries.
    """
    sns.set_context('talk')
    dataset_political_alignments = df['political_alignment'].unique().tolist()
    political_alignments = ['far-left', 'radical left', 'left-wing', 'centre-left',
                            'centrism', 'centre-right', 'right-wing', 'far-right',
                            'national conservatism', 'nationalism', 'liberalism', 'Third Way', 'syncretic politics',
                            None]
    political_alignments = [entry for entry in political_alignments if entry in dataset_political_alignments]
    sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0), 'axes.linewidth': 3})
    palette = sns.color_palette("mako")
    g = sns.FacetGrid(df, palette=palette, row="country", row_order=countries_list, hue="country", aspect=10, height=1,
                      sharey=False)
    g.map_dataframe(sns.countplot, x="political_alignment", order=political_alignments, alpha=0.8)

    def label(x, color, label):
        ax = plt.gca()
        ax.text(-0.2, .2, label, color='black', fontsize=13,
                ha="left", va="center", transform=ax.transAxes)

    g.map(label, "country")
    g.set_titles("")
    g.fig.subplots_adjust(hspace=-.1)
    g.set(yticks=[], yticklabels=[], ylabel=None, xlabel="Political alignment")
    g.despine(left=True)
    for axes in g.axes.flat:
        _ = axes.set_xticklabels(axes.get_xticklabels(), rotation=45, ha='right')
    plt.suptitle('%s - Number of quotes over political alignments per country' % topic_name)


# Distribution of top speakers
def show_top_k_speakers(topic_name, df, k=10):
    """
    Show the top k speakers for a specified topic.

    :param topic_name: name of the topic.
    :param df: pandas dataframe containing the quotes.
    :param k: number of top speakers to show.
    """
    sns.set_context('notebook')
    # Filtered top 10 speakers
    series = df['speaker'] + ' / ' + df['political_party'] + ' (' + df['country'] + ')'

    series = series.groupby(series).count()
    visualized_df = pd.DataFrame({'speaker': series.index,
                                  'counts': series.values
                                  }, columns=['speaker', 'counts'])
    visualized_df = visualized_df.sort_values('counts', ascending=False).head(k)
    fig, ax = plt.subplots(figsize=(14, 6))
    palette = sns.color_palette("mako")
    sns.barplot(x="speaker", y="counts", data=visualized_df,
                ci=None, ax=ax, palette=palette)
    ax.set_xticklabels(labels=visualized_df['speaker'], rotation=60, ha='right')
    plt.xlabel('Speaker / Party (Country)')
    plt.ylabel('Number of quotes')
    plt.title('%s - Top speakers in all countries' % topic_name)
    plt.show()


def show_top_topics_per_country(df_list, df_titles, countries_list):
    """
    Show the most popular topics per country.

    :param df_list: list of different topics dataframes.
    :param df_titles: titles of the topics.
    :param countries_list: list of the countries.
    """
    i = 0
    for df, topic in zip(df_list, df_titles):
        df = df.copy(deep=True)
        df['Topic'] = topic.title()
        df_list[i] = df
        i += 1
    df = pd.concat(df_list)
    sns.set_context('talk')
    sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0), 'axes.linewidth': 3})
    palette = sns.color_palette("mako")
    g = sns.FacetGrid(df, palette=palette, row="country", row_order=countries_list, hue="country", aspect=8, height=2,
                      sharey=False)
    g.map_dataframe(sns.countplot, x="Topic", alpha=0.8)

    def label(x, color, label):
        ax = plt.gca()
        ax.text(-0.1, .2, label, color='black', fontsize=13,
                ha="left", va="center", transform=ax.transAxes)

    g.map(label, "country")
    g.set_titles("")
    g.fig.subplots_adjust(hspace=-.1)
    g.set(yticks=[], yticklabels=[], ylabel=None, xlabel="Topic")
    g.despine(left=True)
    for axes in g.axes.flat:
        _ = axes.set_xticklabels(axes.get_xticklabels(), rotation=45, ha='right')
    plt.suptitle('Distribution of quotes per topic and country')
