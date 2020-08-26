# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 11:31:43 2020

@author: qtckp
"""

import pandas as pd



data = pd.read_excel('test_data.xlsx', header = None)

with open('results.txt','r', encoding = 'utf8') as file:
    lines = [line.split('\t') for line in file]


s1 = pd.Series([a2 for _, a2, a3, a4, a5 in lines])
s2 = pd.Series([a3 for _, a2, a3, a4, a5 in lines])
s3 = pd.Series([a4 for _, a2, a3, a4, a5 in lines])
s4 = pd.Series([a5 for _, a2, a3, a4, a5 in lines])

data['obj'] = s1
data['obj_content'] = s2
data['obj_back'] = s3
data['obj_back_content'] = s4



data.to_excel('all_results.xlsx', header = False, index = False)

