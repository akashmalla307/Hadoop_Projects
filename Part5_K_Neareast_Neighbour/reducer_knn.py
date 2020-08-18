#!/usr/bin/env python3
import sys
from operator import itemgetter
distances=[]
estimateval = 0
k=3

dict1={}
dict2={}
for line in sys.stdin:
	line = line.strip()
	row,dist,label = line.split('\t')
	if row in dict1:
		dict1[row].append([float(dist),float(label)])
	else:
		dict1[row] =[]
	dict2[row] = label
	

for row in dict1:
	res = dict(sorted(dict1[row], key = itemgetter(0), reverse = False)[:k])
	i=0
	votes={}
	for key , value in res.items():
		if value in votes:
			votes[value] = votes[value]+1
		else:
			votes[value] = 1
	max1 = max(votes.items(),key=itemgetter(1))[0]
	print(row,max1)

