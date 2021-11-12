from textblob import TextBlob

def get_subjectivity(citation):
    """
    Get the Subjectivity of a quote
    :param citation: String with the quote to be analyzed
    :return: Subjectivity of the quote
    """
    return TextBlob(citation).sentiment.subjectivity

def get_polarity(citation):
    """
    Get the polarity of a quote
    :param  citation: String with the quote to be analyzed
    :return: Float Polarity of the quote in range of [-1,1]
    """
    return TextBlob(citation).sentiment.polarity

def get_sentiment(score):
    """
    Get the sentiment by analyzing the score
    :param score: Float with the score
    :return: String either Positive, Negative or Neutral
    """
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'
