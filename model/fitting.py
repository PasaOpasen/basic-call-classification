# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:53:51 2020

@author: qtckp
"""

import sys, os, io
sys.path.append(os.path.dirname('../'))

from detector import get_answer
from stemmer_rus import Get_dictionary_values, Stem_text, get_prop_set, grams_to_set
import numpy as np


from termcolor import colored
import colorama

dirname = os.path.dirname(__file__)

def TruePath(path):
    return os.path.join(dirname, path)

voc1 = None
voc2 = None

def update_graph():
    global voc1, voc2
    voc1 = get_prop_set(TruePath('model_data/objections_used.txt'))
    voc2 = get_prop_set(TruePath('model_data/objections_back_used.txt'))
    
    with open(TruePath('model_data/stopwords_used.txt'), 'r', encoding = 'utf-8') as file:
        stops = set((r.rstrip() for r in file))

    def bad_samples(filename):
        with open(filename, 'r', encoding = 'utf-8') as file:
            for line in file:
                words = line.rstrip().split()
                for word in words:
                    if word in stops:
                        print(f'{word}  -------  {line}')
    
    bad_samples(TruePath('model_data/objections_used.txt'))

    bad_samples(TruePath('model_data/objections_back_used.txt'))





with io.open("0.txt",'r', encoding = 'utf-8') as f:
    lines = f.readlines()
    

inds = np.arange(len(lines))
np.random.shuffle(inds)


i = 0
update_graph()

while i < inds.size:
    indx = inds[i]
    l1 = lines[indx]

    res = get_answer(l1, voc1, voc2)

    
    print(colored(f'key = {l1}', on_color = 'on_blue'))
    print(colored(f'skills = {res}', on_color = 'on_green'))
    print()
    
    
    tmp = input('press + for continue and something else for reload: ')
    print()
    if tmp == '+':
        i +=1
    else:
        update_graph()
        print()
