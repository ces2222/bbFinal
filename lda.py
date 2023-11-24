import pandas as pd
import spacy
import gensim
from spacy.lang.en import English
import json
from gensim import corpora
from gensim.models import LdaModel
from gensim.parsing.preprocessing import STOPWORDS
from json_setup import main

def run_lda(num_topics = 5, num_words = 10):
    jsondata = main()
    nlp = English()
    texts = text_setup(jsondata)
    corpus, dictionary = text_dictionary(texts)
    num_topics = num_topics
    lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15)
    topics = lda_model.print_topics(num_words=num_words)
    return topics


def preprocess(text):
    nlp = English()
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return tokens

def text_setup(jsondata):
    texts = [data['full_text'].lower().split() for data in jsondata.values()]
    texts = [[word for word in doc if word not in STOPWORDS] for doc in texts]
    return texts

def text_dictionary(texts):
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    return corpus, dictionary