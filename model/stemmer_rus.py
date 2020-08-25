# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 19:04:07 2020

@author: qtckp
"""

import Stemmer
import os, json, io

stemmer = Stemmer.Stemmer('russian')



def Get_dictionary_values():
    return list(set(dictionary.keys()))

def Stem_text(text):
    return set(stemmer.stemWords(text.lower().split()))

def get_stem_dictionary(filename = 'graph_skills.json'):
    """
    'graph_skills.json'
    'soft_skills.json'
    """
    dr = os.path.dirname(__file__)
    with io.open(os.path.join(dr, filename),'r', encoding = 'utf-8') as f:
        r = json.load(f)
    #print(r)
    return r

def grams_to_set(grams_sets):
    k = [' '.join(g) for g in grams_sets]
    return set(k)
    

def get_prop_set(filename = './model_data/objections_used.txt'):
    with io.open( filename,'r', encoding = 'utf-8') as f:
        sp = [Stem_text(line) for line in f if len(line)>1]
        s = grams_to_set(sp) #set()
        #for line in f:
        #    s = s.union(Stem_text(line))
        return s
    

#dictionary = get_stem_dictionary()



def update_dictionary():
    global dictionary
    dictionary = get_stem_dictionary()

