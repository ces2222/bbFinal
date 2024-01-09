import spacy
import pandas as pd
import os

def basic_sentence_function(sentence):
    """
    sentence: string of text"""
    
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)

    my_dictionary_name = {}    
    for token in doc:
        if token.pos_ == 'PUNCT':
            pass
        else:
            my_dictionary_name[token.text] = token.pos_


    my_ner_dictionary = {}
    for ent in doc.ents:
        my_ner_dictionary[ent.text] = ent.label_


    return my_dictionary_name, my_ner_dictionary