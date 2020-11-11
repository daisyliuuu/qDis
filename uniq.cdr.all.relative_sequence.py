#!/usr/bin/python3
# -*- coding: utf-8 -*-

import gzip
import sys

'''
1. R1
2. R2
3. Out

'''

out1=open(sys.argv[3],'w')
def same_str(str1,str2):
	if len(str1) == len(str2):
		same_str_num=0
		for i in range(len(str1)):
			if str1[i] == str2[i]:
				same_str_num += 1
		return(same_str_num)

def DNA_reverse(sequence):
	return sequence[::-1]  # 求反向序列

def DNA_complement(sequence):
	# 构建互补字典
	comp_dict = {
		"A":"T",
		"T":"A",
		"G":"C",
		"C":"G",
		"a":"t",
		"t":"a",
		"g":"c",
		"c":"g",
		"N":"N",
		"n":"n"
	}
	#求互补序列
	sequence_list = list(sequence)
	sequence_list = [comp_dict[base] for base in sequence_list]
	string = ''.join(sequence_list)
	return string

dict1={}
#with gzip.open("/home/meng/shm_ana/x073/raw/LL12372_R1.fq.gz",'rt') as f:
with gzip.open(sys.argv[1],'rt') as f:
	line_num=0
	for line in f:
		line_num+=1
		seq=line.strip()
		start=0
		end=0
		if line_num % 4 == 1:
			header=seq.split(' ')[0]
			dict1[header]='1'
			#print(seq,file=out1)
		elif line_num % 4 == 2:
			cdr1_after = "TGGTATCGTC"
			cdr2_before = "AGAACGTGAG"
			for i in range(27,len(seq)-10):
				seq_1=seq[i:i+10]
				if same_str(seq_1,cdr1_after)>=8:
					end=i
					break

		#	cdr1=seq[end-27:end]
			
			for i in range(50,len(seq)-10):
				seq_2 = seq[i:i+10]
				if same_str(seq_2,cdr2_before) >= 9:
					start=i+10
					break
			if start != 0 and end != 0:
				cdr1=seq[end-27:end]
				cdr2=seq[start:start+39]
				dict1[header]=cdr1+'\t'+cdr2
			else:
				dict1[header]='0'
			#print(cdr1,file=out1)
			#print(cdr2,file=out1)

seq1="GGCCAAGGTA"
dict2={}
#with gzip.open("/home/meng/shm_ana/x073/raw/LL12372_R2.fq.gz",'rt') as f:
with gzip.open(sys.argv[2],'rt') as f:
	line_num=0
	for line in f:
		line_num+=1
		seq=line.strip()
		if line_num % 4 == 1:
			header=seq.split(' ')[0]
			#print(seq,file=out1)
		elif line_num % 4 == 2:
			seq=DNA_complement(DNA_reverse(seq))
			start=91
			end=0
			for i in range(95,len(seq)-10):
				seq2=seq[i:i+10]
				if same_str(seq1,seq2)>=8:
					end=i
					break
			if end != 0:
				cdr3=seq[91:end]
				if header in dict1.keys():
					#if dict1[header]+'\t'+cdr3 not in dict2.keys():
						#print(header+'\t'+dict1[header]+'\t'+cdr3,file=out1)
					if dict1[header]+'\t'+cdr3 in dict2.keys():
						dict2[dict1[header]+'\t'+cdr3] += 1
					else:
						dict2[dict1[header]+'\t'+cdr3] = 1
			#print(cdr3,file=out1)
	for k,v in dict2.items():
		print(k+'\t'+str(v),file=out1)
	out1.close()

