# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 13:01:34 2020

@author: qtckp
"""


import sys, os, io
sys.path.append(os.path.dirname('../'))

from model.detector import get_answer



if __name__=='__main__':
    
    # with io.open("train.txt",'r', encoding = 'utf-8') as f:
    #     doclines = f.readlines()
    
    with io.open("test.txt",'r', encoding = 'utf-8') as f:
        doclines = f.readlines()

    result = [(i, a, b, c, d) for i, (a,b,c,d) in enumerate(map(lambda sample: get_answer(sample), doclines))]
    
    with io.open("results.txt",'w', encoding = 'utf-8') as f:
        f.writelines('\t'.join(map(str, r)) + '\n' for r in result)
  
    
    