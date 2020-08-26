# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 12:58:00 2020

@author: qtckp
"""


import pandas as pd
from shutil import copyfile
import os.path as op

model_data_path = './model/model_data'


data = pd.read_excel('train_data.xlsx', header = None)

with open('train.txt','w', encoding = 'utf8') as file:
    
    lines = [r.replace('\n',' ') +'\n' for r in data.iloc[:,3]]
    
    file.writelines(lines)




obj = pd.read_excel('objections.xlsx', header = None)

with open('objections_start.txt','w', encoding = 'utf8') as file:
    
    lines = [r.replace('\n',' ') +'\n' for r in obj.iloc[0,1:]]
    
    file.writelines(lines)


copyfile('objections_start.txt', op.join(model_data_path,'objections_used.txt'))





obj = pd.read_excel('objections_back.xlsx', header = None).dropna(axis='columns')

with open('objections_back_start.txt','w', encoding = 'utf8') as file:
    
    lines = [r.replace('\n',' ') +'\n' for r in obj.iloc[0,1:]]
    
    file.writelines(lines)


copyfile('objections_back_start.txt', op.join(model_data_path,'objections_back_used.txt'))










data = pd.read_excel('test_data.xlsx', header = None)

with open('test.txt','w', encoding = 'utf8') as file:
    
    lines = [r.replace('\n',' ') +'\n' for r in data.iloc[:,3]]
    
    file.writelines(lines)



