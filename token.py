from clang.cindex import Config
from clang.cindex import TypeKind
from clang.cindex import CursorKind
from clang.cindex import Index
import re
import os
import csv
import Levenshtein
libclangPath = '/usr/lib/llvm-3.8/lib/libclang.so.1'
if Config.loaded==True:
        pass
else:
        Config.set_library_file(libclangPath)
def iterAST(cursor,a):
	for cur in cursor.get_children():
		if cur.kind == CursorKind.FUNCTION_DECL:
			#print(iter_cursor_content(cur))
			a=a+iter_cursor_content(cur)
			for cur_sub in cur.get_children():
				print(cur_sub.spelling)
		elif cur.kind == CursorKind.FIELD_DECL:
			print(cur.kind)
		elif cur.type.kind == TypeKind.UCHAR:
			print(cur.kind)
		iterAST(cur,a)
	return a
def iter_cursor_content(cur):
        cursor_content=""
        for token in cur.get_tokens():
	    if token.spelling == 'int' or token.spelling == 'main' or token.spelling=='(' or token.spelling == ')' or token.spelling == '{' or token.spelling =='}' or ('VAR' in token.spelling) or token.spelling==';' or token.spelling==',' or token.spelling=='return' or token.spelling == 'cin' or token.spelling == 'cout' or token.spelling == 'scanf' or token.spelling=='printf' or token.spelling == '>>' or token.spelling == '<<' or token.spelling == 'if' or token.spelling == 'while' or token.spelling == '[' or token.spelling == ']' or token.spelling == 'char' or token.spelling == '+' or token.spelling =='-' or token.spelling == '=' or token.spelling == '*' or token.spelling=='/':
		continue
            str_token = token.spelling+" "
            cursor_content = cursor_content+str_token
	cursor_content=re.sub('"','',cursor_content)
	cursor_content=re.sub('\'','',cursor_content)
        return cursor_content 
index = Index.create()
#tu = index.parse('0ade50fef00347e7.txt',['-x','c++','-I','.'])
#a=''
#b=iterAST(tu.cursor,a)
f=open('result.txt','a')
#f5=open('TestSim.txt','w')
'''csv_reader = csv.reader(open('sample_submission.csv'))
num=1;
for row in csv_reader:
	num=num+1
	if num==2:
		continue
	st=row[0]
	sd=st.split('_',1)
        str1=sd[0]+'.txt'
        str2=sd[1]+'.txt'
	print(str1)
	print(str2)
        tu1 = index.parse(str1,['-x','c++','-I','.'])
	tu2 = index.parse(str2,['-x','c++','-I','.'])
	a=''
	e=''
	b1=iterAST(tu1.cursor,a)
	b2=iterAST(tu2.cursor,e)
	res=Levenshtein.ratio(b1,b2)
	if res>0.5075:
		f.writelines('1'+'\n')
	else:
		f.writelines('0'+'\n')
'''	
f1=open('TrainSimi.txt','w')
f2=open('docnew.txt')
'''def getNumofCommonSubstr(str1, str2):  
  
    lstr1 = len(str1)  
    lstr2 = len(str2)  
    record = [[0 for i in range(lstr2+1)] for j in range(lstr1+1)] 
    maxNum = 0           
    p = 0                 
  
    for i in range(lstr1):  
        for j in range(lstr2):  
            if str1[i] == str2[j]:  
                record[i+1][j+1] = record[i][j] + 1  
                if record[i+1][j+1] > maxNum:    
                    maxNum = record[i+1][j+1]    
                    p = i + 1  
    return str1[p-maxNum:p], maxNum  
'''
for line in f2.readlines():
	line=line.strip('\n')
	st=line.split('#',2)
	tu1 = index.parse(st[0],['-x','c++','-I','.'])
	tu2 = index.parse(st[1],['-x','c++','-I','.'])
	a=''
	e=''
	b1=iterAST(tu1.cursor,a)
	b2=iterAST(tu2.cursor,e)
	sim = Levenshtein.ratio(b1,b2)
	print(sim)
	#res=getNumofCommonSubstr(b1,b2)
	f1.writelines(str(sim)+'\n')
