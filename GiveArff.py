#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 18:19:56 2018

@author: jimmy233
"""

f=open('julei/relation_train_3features_cons.arff','w+')

f2=open('TestSim.txt')#TrainSimi_9feature.txt
f3=open('feature_test_try.txt')
f4=open('test_sp_new.txt')
#5=open('doc_try.txt')
f6=open('train_quatation_new.txt')
f7=open('traindecl_try.txt')

f.writelines("@relation CloneDectionTrain"+'\n')
f.writelines('\n')

f.writelines("@attribute Label {0,1}"+'\n')
f.writelines("@attribute Resemblance numeric"+'\n')
f.writelines("@attribute SpRes numeric"+'\n')
f.writelines("@attribute ConStantRes numeric"+'\n')
f.writelines("@attribute Decl numeric"+'\n')
f.writelines("@attribute if numeric"+'\n')
f.writelines("@attribute whilefor numeric"+'\n')
f.writelines("@attribute input numeric"+'\n')
f.writelines("@attribute output numeric"+'\n')
f.writelines("@attribute var numeric"+'\n')
f.writelines("@attribute op numeric"+'\n')
#f.writelines("@attribute strcpy {0,1}"+'\n')
#f.writelines("@attribute strcmp {0,1}"+'\n')
f.writelines('\n')

f.writelines("@data"+'\n')
array2=f2.readlines()
array3=f3.readlines()
array4=f4.readlines()
array5=f5.readlines()
array6=f6.readlines()
array7=f7.readlines()
for i in range(0,200000):
    array2[i] = array2[i].strip('\n')
    array4[i] = array4[i].strip('\n')
    array6[i] = array6[i].strip('\n')
    array3[i] = array3[i].strip('\n')
    array7[i] = array7[i].strip('\n')
    st=array3[i].split('#',7)
    #st = array3[i].split('#',2)
    s='?'+','+array2[i]+','+array4[i]+','+array6[i]
    f.writelines(s+'\n')
for i in range(0,144118):
    array5[i] = array5[i].strip('\n')
    array2[i] = array2[i].strip('\n')
    array4[i] = array4[i].strip('\n')
    array3[i] = array3[i].strip('\n')
    array6[i] = array6[i].strip('\n')
    array7[i] = array7[i].strip('\n')
    st=array3[i].split('#',7)
    sg=array5[i].split('#',2)
    s=sg[2]+','+array2[i]+','+array4[i]+','+array6[i]
    f.writelines(s+'\n')