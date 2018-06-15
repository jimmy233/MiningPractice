#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 10:35:00 2018

@author: jimmy233
"""

from __future__ import print_function
import sys
import os
import csv
import Levenshtein
sys.path.extend(['.', '..'])

from pycparser import c_parser, c_ast
f2 = open('doc_try.txt')
csv_reader = csv.reader(open('sample_submission.csv'))
num=1;
f3 = open('test_sp_new.txt','w')
def read_file_as_str(file_path):
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")
    all_the_text = open(file_path).read()
    return all_the_text

def read_one(txt):
    parser = c_parser.CParser()
    ast = parser.parse(txt, filename='<none>')
    s = len(ast.ext)
    summ = 0
    for i in range(0,s):
        if hasattr(ast.ext[i],'body') == True:
            function_body = ast.ext[i].body
            if function_body.block_items == None:
                summ = summ + 0 
            else:       
                summ = summ + len(function_body.block_items) 
    return summ
f4=open('traindecl_try.txt','w')
#csv_reader = csv.reader(open('sample_submission.csv'))
for line in f2.readlines():
    line = line.strip('\n')
    sd = line.split('#',2)
    str1=sd[0]
    str2=sd[1]
    s1=read_one(read_file_as_str(str1))
    s2=read_one(read_file_as_str(str2))
    resu = abs(s1-s2)
    print(str(resu))
    f4.writelines(str(resu)+'\n')
for row in csv_reader:
    line = row[0]
    num = num + 1
    if num == 2:
        continue
    sd = line.split('_',1)
    strr1='test/'+sd[0]+'.txt'
    strr2='test/'+sd[1]+'.txt'
    f11 = open(strr1)
    str1='scanf '
    str2='printf '
    f12 = open(strr2)
    for line in f11.readlines():
        if 'printf' in line:
            line=line.replace('printf','')
            line=line.replace(')','')
            line=line.replace(';','')
            line=line.replace('(','')
            str2=str2+line
        elif 'scanf' in line:
            line=line.replace('scanf','')
            line=line.replace(')','')
            line=line.replace(';','')
            line=line.replace('(','')
            str1 = str1+line
        elif 'cin' in line:
            line=line.replace('cin','')
            line=line.replace(')','')
            line=line.replace(';','')
            line=line.replace('(','')
            line=line.replace('>','')
            str1 = str1+line
        elif 'cout' in line:
            line=line.replace('cout','')
            line=line.replace(')','')
            line=line.replace(';','')
            line=line.replace('(','')
            line=line.replace('<','')
            line=line.replace('endl','\n')
            str2=str2+line
    str11='scanf '
    str22='printf '
    for line in f12.readlines():
        if 'printf' in line:
            line=line.replace('printf','')
            line=line.replace(')','')
            line=line.replace(';','')
            line=line.replace('(','')
            str22=str22+line
        elif 'scanf' in line:
            line=line.replace('scanf','')
            line=line.replace(')','')
            line=line.replace(';','')
            line=line.replace('(','')
            str11 = str11+line
        elif 'cin' in line:
            line=line.replace('cin','')
            line=line.replace(')','')
            line=line.replace(';','')
            line=line.replace('(','')
            line=line.replace('>','')
            str11 = str11+line
        elif 'cout' in line:
            line=line.replace('cout','')
            line=line.replace(')','')
            line=line.replace(';','')
            line=line.replace('(','')
            line=line.replace('<','')
            line=line.replace('endl','\n')
            str22=str22+line
    stf=str1+str2
    sts=str11+str22
    resu=Levenshtein.ratio(stf,sts)
    print(resu)
    f3.writelines(str(resu)+'\n')

