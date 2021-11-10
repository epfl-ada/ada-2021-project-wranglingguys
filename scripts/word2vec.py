import gensim.downloader as api
from gensim.parsing import *
import numpy as np


def get_word2vec_model(pretrained_model_name):
    """
    Get a trained Word2Vec model.
    :param pretrained_model_name: string containing the name of the pre trained model. Please, consult this website https://github.com/RaRe-Technologies/gensim-data#models to check the names of the pre trained models.
    :return: gensim word2vec model.
    """
    model = api.load(pretrained_model_name)

    return model


def get_sentence_vector(sentence, model):
    """
    Get the vector representation of a sentence.
    :param sentence: string containing a sentence.
    :param model: Word2Vec trained model to query.
    :return: vector representing the whole sentence.
    """
    preprocessed_words_strings = preprocess_string(sentence, filters=[strip_punctuation, strip_multiple_whitespaces,
                                                                      remove_stopwords, strip_short])
    preprocessed_words_vectors = [model.get_vector(string) for string in preprocessed_words_strings]
    average = np.mean(preprocessed_words_vectors, axis=0)
    average = average / np.std(average)

    return average
