# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 19:59:01 2020

@author: qtckp
"""


with open('stopwords_used.txt', 'r', encoding = 'utf-8') as file:
    stops = set((r.rstrip() for r in file))



def bad_samples(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        for line in file:
            words = line.rstrip().split()
            for word in words:
                if word in stops:
                    print(f'{word}  -------  {line}')



bad_samples('objections_used.txt')

bad_samples('objections_back_used.txt')
