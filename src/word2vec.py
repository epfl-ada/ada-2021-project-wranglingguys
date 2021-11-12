import gensim.downloader as api
import pandas as pd
from gensim.parsing import *
from gensim.models import TfidfModel
from gensim.corpora import Dictionary
from gensim.parsing.preprocessing import lower_to_unicode


def get_dct_and_tf_idf_model(quotes):
    """
    Given a list of quotes (iterable of iterable of strings), returns a dictionary, a bow_corpus and a TF-IDF model
    :param quotes: iterable of iterable of strings
    :return: dictionary, bow_corpus and TF-IDF model of the input dataset
    """
    # Fit dictionary
    dct = Dictionary(quotes)

    # Convert corpus to BoW format
    bow_corpus = [dct.doc2bow(quote) for quote in quotes]

    # Fit model
    tf_idf_model = TfidfModel(bow_corpus)

    return dct, bow_corpus, tf_idf_model

def get_word2vec_model(pretrained_model_name='glove-wiki-gigaword-50'):
    """
    Get a trained Word2Vec model.
    :param pretrained_model_name: string containing the name of the pre trained model. Please, consult this website https://github.com/RaRe-Technologies/gensim-data#models to check the names of the pre trained models.
    :return: gensim word2vec model.
    """
    print("### Loading Word2Vec %s pre trained model ###" % pretrained_model_name)
    model = api.load(pretrained_model_name)
    print("### Successfully loaded Word2Vec %s pre trained model ###" % pretrained_model_name)
    return model

def extend_dataframe(original_dataframe, quotes_feature_name, new_feature_name, word2vec_model=None):
    """
    Extend the dataframe adding a new feature with vector representations of quotes.
    :param original_dataframe: dataframe where to add the new feature and containing the quotes.
    :param quotes_feature_name: name of the feature containing the quotes.
    :param new_feature_name: name of the new feature to be added.
    :param word2vec_model: optionally, the word2vec model to use to form the vectors.
    """
    quotes_series = original_dataframe[quotes_feature_name]

    quotes_tokens_series = quotes_series.map(lambda sentence: preprocess_string(sentence, filters=[strip_punctuation, strip_multiple_whitespaces,
                                                                      remove_stopwords, strip_short, strip_numeric, lower_to_unicode]))

    if word2vec_model is None:
        word2vec_model = get_word2vec_model()

    # Get TF-IDF files
    dct, bow_corpus, tf_idf_model = get_dct_and_tf_idf_model(quotes_tokens_series)

    list = []

    # Transform the quotes into vectors by averaging with TF-IDF
    for index, quote in enumerate(quotes_tokens_series):
        scores_vector = tf_idf_model[bow_corpus[index]]
        list.append(get_sentence_vector(word2vec_model, scores_vector, dct))

    original_dataframe[new_feature_name] = pd.Series(list)


def get_sentence_vector(w2v_model, scores_vector, dct):
    """
    Get the vector representation of a sentence.
    If a word is not present in the vocabulary, it will be removed from the sentence.
    :param w2v_model: Word2Vec trained model to query.
    :param scores_vector: TF-IDF scores of the sentence.
    :param dct: dict containing all the words in the dataset.
    :return: vector representing the whole sentence.
    """

    total_weight = 0.
    average_vector = w2v_model['word'] * 0

    for word_index, word_score in scores_vector:
        word = dct[word_index]
        if word in w2v_model.key_to_index:
            word_vector = w2v_model[word]

            # Add score times word vector
            average_vector = average_vector + word_score * word_vector

            # Update the total weight
            total_weight = total_weight + word_score

    if total_weight == 0:
        return average_vector

    # Divide for the total weight
    average_vector = average_vector / total_weight

    return average_vector

