#python3
import multiprocessing as mp
import csv
import sys

def same_base(seq1,seq2):
	result_num = 0
	if seq1 != "" and seq2 != "" and len(seq1)==len(seq2):
		for i in range(len(seq1)):
			if seq1[i]==seq2[i]:
				result_num += 1

	return(result_num)


dict_big={}
dict_little={}
#for line in open("uniq"):
for line in open(sys.argv[1]):
	l=line.strip().split('\t')[0:4]
	if "" not in l and len(line.strip().split('\t'))==4:
		read_num=line.strip().split('\t')[3]
		k="\t".join(line.strip().split('\t')[0:3])
		if int(read_num) > 10:
			dict_big[k] = read_num
		else:
			dict_little[k]=read_num

big_all=len(dict_big.keys())

#global dict_big

def result(k_little):
#for k_little in dict_little.keys():
	k_little1=k_little.split('\t')[0]
	k_little2=k_little.split('\t')[1]
	k_little3=k_little.split('\t')[2]
	big_num=0
	for k_big in dict_big.keys():
		big_num += 1
		k_big1=k_big.split('\t')[0]
		k_big2=k_big.split('\t')[1]
		k_big3=k_big.split('\t')[2]
		same_base_num1=same_base(k_little1,k_big1)
		same_base_num2=same_base(k_little2,k_big2)
		same_base_num3=same_base(k_little3,k_big3)
		if same_base_num1 >= 27-1 and same_base_num2 >= 39-1 and same_base_num3 >= 30-1:
			dict_big[k_big]=int(dict_big[k_big])+int(dict_little[k_little])
			return(k_big+'\ttest\t'+str(dict_big[k_big])+'\t'+str(int(dict_little[k_little]))+'\t'+k_little)
			break
		else:
			if big_num == big_all:
				return(k_little+'\t'+dict_little[k_little])

dict_new={}
p=mp.Pool(15)
#out=open("test.result",'a')
out=open(sys.argv[2],'w')
for res in p.imap(result,dict_little.keys()):
#	if res != None:
#		if len(res.split('\t')) >= 4:
	if "test" in res:
		k=res.split('\t')[0]+'\t'+res.split('\t')[1]+'\t'+res.split('\t')[2]
		if k in dict_new.keys():
			dict_new[k] =int(dict_new[k]) + int(res.split('\t')[5])
		else:
			dict_new[k] = int(res.split('\t')[5])
	else:
		print(res,file=out)

for k in dict_big.keys():
	if k in dict_new.keys():
		result1 = int(dict_big[k])+int(dict_new[k])
	else:
		result1 = int(dict_big[k])
	print(k+'\t'+str(result1),file=out)
