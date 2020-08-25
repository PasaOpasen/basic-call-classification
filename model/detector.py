# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:20:38 2020

@author: qtckp
"""

import sys, os, io
sys.path.append(os.path.dirname(__file__))

from Ngrams import txt_list_to_grams

from stemmer_rus import Get_dictionary_values, Stem_text, get_prop_set, grams_to_set

from prepare_functions import *

dirname = os.path.dirname(__file__)

def TruePath(path):
    return os.path.join(dirname, path)

def has_feature(grams, vocab):
    gr = [Stem_text(gram) for gram in grams]
    return any(v in grams_to_set(gr) for v in vocab)

def get_position_line(lines, index):
    if index != None:
       line, who = lines[index]
       return f'{who}) {line}'
        
    return None

def get_answer(sample, first_vocab = get_prop_set(TruePath('model_data/objections_used.txt')), second_vocab = get_prop_set(TruePath('./model_data/objections_back_used.txt'))):
    
    ngrams, lines  = txt_list_to_grams(sample, 0)
    
    first_flag, first_ind, second_flag, second_ind = False, None, None, None
    
    for i in range(len(lines)):
        g, number = ngrams[i]
        if number == 2 and has_feature(g, first_vocab):
            first_flag, first_ind, second_flag, second_ind = True, i, False, None
            
            for j in range(i+1, len(lines)):
                h, nb = ngrams[j]
                if nb == 1 and has_feature(h, second_vocab):
                    second_flag, second_ind = True, j
                    
                    break
            break
    
    if second_flag == False and len(lines)-first_ind > 8:
        second_flag = '50/50'
    
    return first_flag, get_position_line(lines, first_ind), second_flag, get_position_line(lines, second_ind)



if __name__=='__main__':
    
    
    with io.open("0.txt",'r', encoding = 'utf-8') as f:
        doclines = f.readlines()
        
    answer = get_answer(doclines[0],
                        get_prop_set('./model_data/objections_used.txt'),
                        get_prop_set('./model_data/objections_back_used.txt'))
    print(answer)
    
    

