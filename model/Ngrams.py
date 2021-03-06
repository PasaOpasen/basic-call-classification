# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 16:11:56 2020

@author: qtckp
"""


import io
import sys, os
import re

from prepare_functions import *


my_dir = os.path.dirname(__file__)
def CorrectPath(filename):
    return os.path.join(my_dir, filename)

def CorrectPathData(filename):
    return os.path.join(my_dir,'model_data', filename)


def print_list(lst):
    for r in lst:
       print(r)
    
    print()
    print()
    print()



with io.open(CorrectPathData('stopwords_used.txt'), 'r', encoding = 'utf-8') as f:
    splitter = [w.rstrip() for w in f.readlines() if not w.startswith('#') and len(w)>1]




def txt_list_to_grams(sample, debug = 1, out_file = CorrectPath('report.txt')):
       
    if debug:
        beg = '------> '
        file = open(out_file,'w')
        sys.stdout = file
        
        print(beg+'BEGIN:')
        print(sample)

    
    lines = split_by_speakers(sample)
    if debug:
        print(beg+'SPLIT BY SPEAKERS')
        print_list(lines)
    
    
    # replace strange symbols with space
    convert = lambda s: s if s.isspace() or s.isalnum() else ' '
    
    lines = (
        (''.join((convert(s) for s in line)).strip(), number )
        for line, number in lines)
    
    if debug:
        lines=list(lines)
        print(beg+'DELETE STRANGE SYMBOLS')
        print_list(list(lines))
    
    # delete multiple spaces
    lines = [(' '.join(line.split()) , number) for line, number in lines]
    
    if debug:
        print(beg+'DELETE MULTIPLE SPACES')
        print_list(lines)
    
    
    
    # 3) remove stopwords
    
    dats = [(split_by_words2(line.lower(), splitter), number) for line, number in lines]
    
    if debug:
        print(beg+'SPLIT BY SENTENCES AND STOP WORDS')
        print_list(dats)
    
   
    # split by n-grams
    
    ngrams = []
    for sentences, number in dats:
        grams = list( 
            set().union(*[ 
                [' '.join(list(g)) for g in get_ngrams(txt.split(), 3)] for txt in sentences]).union(*[ 
                [' '.join(list(g)) for g in get_ngrams(txt.split(), 2)]
                    for txt in sentences]).union(*[ 
                [' '.join(list(g)) for g in get_ngrams(txt.split(), 1)] for txt in sentences])
            )
        grams = [g for g in grams if len(g)>0 and any((s.isalpha() for s in g))]                 
                            
        ngrams.append((grams, number))
        
    if debug:
        ngrams = list(ngrams)
        print(beg+'GET 1/2/3 NGRAMS')
        print_list(ngrams)
      
    
    if debug:
        print(beg+'RESULTS')
        print_list(ngrams)
        file.close()
    
    return ngrams, lines
    
    

if __name__=='__main__':
    
    # 1) read file
    
    with io.open(CorrectPath('0.txt'),'r', encoding = 'utf-8') as f:
        doclines = f.readlines()
    
    original_stdout = sys.stdout
    g = txt_list_to_grams(doclines[2],1)
    
        
    sys.stdout = original_stdout
    
    print_list(g)
        
