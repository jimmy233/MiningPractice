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
def iterAST(cursor,a,ifcount,whileforcount,inputcount,outputcount,varcount,strcpycount,strcmpcount,opcount):
	for cur in cursor.get_children():
		if cur.kind == CursorKind.FUNCTION_DECL:
			#print(iter_cursor_content(cur))
			(red,ifcount,whileforcount,inputcount,outputcount,varcount,strcpycount,strcmpcount,opcount)=iter_cursor_content(cur,ifcount,whileforcount,inputcount,outputcount,varcount,strcpycount,strcmpcount,opcount)
			a=a+red
			for cur_sub in cur.get_children():
				print(cur_sub.spelling)
		elif cur.kind == CursorKind.FIELD_DECL:
			print(cur.kind)
		elif cur.type.kind == TypeKind.UCHAR:
			print(cur.kind)
		iterAST(cur,a,ifcount,whileforcount,inputcount,outputcount,varcount,strcpycount,strcmpcount,opcount)
	return a,ifcount,whileforcount,inputcount,outputcount,varcount,strcpycount,strcmpcount,opcount
def iter_cursor_content(cur,ifcount,whileforcount,inputcount,outputcount,varcount,strcpycount,strcmpcount,opcount):
        cursor_content=""
        for token in cur.get_tokens():
	    if token.spelling == 'int' or token.spelling == 'main' or token.spelling=='(' or token.spelling == ')' or token.spelling == '{' or token.spelling =='}' or token.spelling==';' or token.spelling==',' or token.spelling=='return' or token.spelling == '>>' or token.spelling == '<<' or token.spelling == '[' or token.spelling == ']' or token.spelling == 'char' or token.spelling == '=':
		continue
	    if token.spelling=='if':
		ifcount=ifcount+1
		continue
	    if token.spelling=='while':
		whileforcount=whileforcount+1
		continue
	    if token.spelling=='for':
		whileforcount=whileforcount+1
	    if token.spelling=='cin' or token.spelling =='scanf':
		inputcount=inputcount+1
		continue
	    if token.spelling=='cout' or token.spelling =='printf':
		outputcount=outputcount+1
		continue
	    if 'VAR' in token.spelling:
		varcount=varcount+1
		continue
	    if token.spelling=='strcpy':
		strcpycount=strcpycount+1
	    if token.spelling=='strcmp':
		strcmpcount=strcmpcount+1
	    if token.spelling == '+' or token.spelling == '-' or token.spelling=='*' or token.spelling=='/':
		opcount=opcount+1
		continue
            str_token = token.spelling+" "
            cursor_content = cursor_content+str_token
	cursor_content=re.sub('"','',cursor_content)
	cursor_content=re.sub('\'','',cursor_content)
        return cursor_content,ifcount,whileforcount,inputcount,outputcount,varcount,strcpycount,strcmpcount,opcount 
index = Index.create()
#tu = index.parse('0ade50fef00347e7.txt',['-x','c++','-I','.'])
#a=''
#b=iterAST(tu.cursor,a)
#f=open('result.txt','a')
#f5=open('TestSim.txt','w')
'''fe=open('feature_.txt','w')
csv_reader = csv.reader(open('sample_submission.csv'))
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
	ifcount=0
	whileforcount=0
	inputcount=0
	outputcount=0
	varcount=0
	strcpycount=0
	strcmpcount=0
	opcount=0
	(b1,ifcount,whileforcount,inputcount,outputcount,varcount,strcpycount,strcmpcount,opcount)=iterAST(tu1.cursor,a,ifcount,whileforcount,inputcount,outputcount,varcount,strcpycount,strcmpcount,opcount)
	#print(ifcount)
	#print(whileforcount)
	ifcount1=0
	whileforcount1=0
	inputcount1=0
	outputcount1=0
	varcount1=0
	strcpycount1=0
	strcmpcount1=0
	opcount1=0
	(b2,ifcount1,whileforcount1,inputcount1,outputcount1,varcount1,strcpycount1,strcmpcount1,opcount1)=iterAST(tu2.cursor,e,ifcount1,whileforcount1,inputcount1,outputcount1,varcount1,strcpycount1,strcmpcount1,opcount1)
	if_re=abs(ifcount-ifcount1)
	whilefor_re=abs(whileforcount-whileforcount1)
	input_re=abs(inputcount-inputcount1)
	output_re=abs(outputcount-outputcount1)
	var_re=abs(varcount-varcount1)
	strcp_re='1'
	if (strcpycount == 0 and strcpycount1 > 0) or (strcpycount > 0 and strcpycount1==0):
		strcp_re='0'
	strcm_re='1'
	if (strcmpcount==0 and strcmpcount1>0) or (strcmpcount>0 and strcmpcount1==0):
		strcm_re='0'
	op_re=abs(opcount-opcount1)
	print(str(if_re)+'#'+str(whilefor_re)+'#'+str(input_re)+'#'+str(output_re)+'#'+str(var_re)+'#'+strcp_re+'#'+strcm_re+'\n')
	fe.writelines(str(if_re)+'#'+str(whilefor_re)+'#'+str(input_re)+'#'+str(output_re)+'#'+str(var_re)+'#'+strcp_re+'#'+strcm_re+'#'+str(op_re)+'\n')
'''	
f1=open('TrainSimi_9feature.txt','w')
f2=open('doc_try.txt')
ft=open('feature_train.txt','w')

for line in f2.readlines():
	line=line.strip('\n')
	st=line.split('#',2)
	tu1 = index.parse(st[0],['-x','c++','-I','.'])
	tu2 = index.parse(st[1],['-x','c++','-I','.'])
	a=''
	e=''
	ifcount=0
	whileforcount=0
	inputcount=0
	outputcount=0
	varcount=0
	strcpycount=0
	strcmpcount=0
	opcount=0
	(b1,ifcount,whileforcount,inputcount,outputcount,varcount,strcpycount,strcmpcount,opcount)=iterAST(tu1.cursor,a,ifcount,whileforcount,inputcount,outputcount,varcount,strcpycount,strcmpcount,opcount)
	#print(ifcount)
	#print(whileforcount)
	ifcount1=0
	whileforcount1=0
	inputcount1=0
	outputcount1=0
	varcount1=0
	strcpycount1=0
	strcmpcount1=0
	opcount1=0
	(b2,ifcount1,whileforcount1,inputcount1,outputcount1,varcount1,strcpycount1,strcmpcount1,opcount1)=iterAST(tu2.cursor,e,ifcount1,whileforcount1,inputcount1,outputcount1,varcount1,strcpycount1,strcmpcount1,opcount1)
	if_re=abs(ifcount-ifcount1)
	whilefor_re=abs(whileforcount-whileforcount1)
	input_re=abs(inputcount-inputcount1)
	output_re=abs(outputcount-outputcount1)
	var_re=abs(varcount-varcount1)
	strcp_re='1'
	if (strcpycount == 0 and strcpycount1 > 0) or (strcpycount > 0 and strcpycount1==0):
		strcp_re='0'
	strcm_re='1'
	if (strcmpcount==0 and strcmpcount1>0) or (strcmpcount>0 and strcmpcount1==0):
		strcm_re='0'
	op_re=abs(opcount-opcount1)
	sim = Levenshtein.ratio(b1,b2)
	#print(sim)
	#res=getNumofCommonSubstr(b1,b2)
	f1.writelines(str(sim)+'\n')
	print(str(if_re)+'#'+str(whilefor_re)+'#'+str(input_re)+'#'+str(output_re)+'#'+str(var_re)+'#'+strcp_re+'#'+strcm_re+'\n')
	ft.writelines(str(if_re)+'#'+str(whilefor_re)+'#'+str(input_re)+'#'+str(output_re)+'#'+str(var_re)+'#'+strcp_re+'#'+strcm_re+'#'+str(op_re)+'\n')
