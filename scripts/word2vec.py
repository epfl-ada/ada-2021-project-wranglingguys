import gensim.downloader as api
from gensim.parsing import *
import numpy as np


def extend_dataframe(original_dataframe, quotes_feature_name, new_feature_name, word2vec_model=None):
    """
    Extend the dataframe adding a new feature with vector representations of quotes.
    :param original_dataframe: dataframe where to add the new feature and containing the quotes.
    :param quotes_feature_name: name of the feature containing the quotes.
    :param new_feature_name: name of the new feature to be added.
    :param word2vec_model: optionally, the word2vec model to use to form the vectors.
    By default, it will use the pre-trained word2vec-google-news-300 model in gensim
    """
    quotes_series = original_dataframe[quotes_feature_name]

    if word2vec_model is None:
        word2vec_model = get_word2vec_model()

    quotes_vectors_series = quotes_series.map(lambda sentence: get_sentence_vector(sentence, word2vec_model))

    original_dataframe[new_feature_name] = quotes_vectors_series


def get_word2vec_model(pretrained_model_name='word2vec-google-news-300'):
    """
    Get a trained Word2Vec model.
    :param pretrained_model_name: string containing the name of the pre trained model. Please, consult this website https://github.com/RaRe-Technologies/gensim-data#models to check the names of the pre trained models. Default is google news dataset pre-trained model.
    :return: gensim word2vec model.
    """
    print("### Loading Word2Vec %s pre trained model ###" % pretrained_model_name)
    model = api.load(pretrained_model_name)
    print("### Successfully loaded Word2Vec %s pre trained model ###" % pretrained_model_name)
    return model


def get_sentence_vector(sentence, model):
    """
    Get the vector representation of a sentence.
    If a word is not present in the vocabulary, it will be removed from the sentence.
    :param sentence: string containing a sentence.
    :param model: Word2Vec trained model to query.
    :return: vector representing the whole sentence.
    """
    preprocessed_words_strings = preprocess_string(sentence, filters=[strip_punctuation, strip_multiple_whitespaces,
                                                                      remove_stopwords, strip_short])
    preprocessed_words_vectors = [model.get_vector(string) for string in preprocessed_words_strings if string in model.vocab]
    average = np.mean(preprocessed_words_vectors, axis=0)
    average = average / np.std(average)

    for string in preprocessed_words_strings:
        if string not in model.vocab:
            print("Word ", string, " not found!")

    return average
