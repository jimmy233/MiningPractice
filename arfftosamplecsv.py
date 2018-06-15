#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 23:52:56 2018

@author: jimmy233
"""

import re
import sys
import csv

lines = []
csv_file=open('exex.csv','w')
writer = csv.writer(csv_file)
arff_file = open('edx.arff')#open('ex1_2feature_br.arff')
array =arff_file.readlines()
csv_reader = csv.reader(open('sample_submission.csv'))
num=1;
count=8
for row in csv_reader:
    num = num + 1
    if num == 2:
        writer.writerow(row)
        continue
    st=array[count].split(',',15)
    count=count+1
    if st[1]=='0':
        row[1]=0
    elif st[1]=='1':
        row[1]=1
    writer.writerow(row)

