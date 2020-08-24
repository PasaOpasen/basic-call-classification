# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:09:37 2020

@author: qtckp
"""

import os.path as op
from shutil import copyfile

model_data_path = './model/model_data'


from stop_words import get_stop_words

stop_words = get_stop_words('ru')


with open(op.join(model_data_path, 'stopwords_base.txt'), 'w', encoding = 'utf-8') as file:
    file.writelines([s+'\n' for s in stop_words])

copyfile(op.join(model_data_path, 'stopwords_base.txt'), op.join(model_data_path, 'stopwords_used.txt'))
