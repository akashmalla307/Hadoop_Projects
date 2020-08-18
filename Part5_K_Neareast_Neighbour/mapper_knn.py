#!/usr/bin/env python3
import sys
import math
import csv
import numpy as np
import pandas as pd
train =[]

df= pd.read_csv(r'Test.csv')
arr1 = df.to_numpy()
len1 = len(arr1)
tmp=[]
word = 'TestRow'
for line in sys.stdin:	
	line = line.strip()
	train = np.fromstring(line,sep=',')
	trainwo = np.delete(train,-1)
	label = train[-1]
	i=-1
	while i < len1-1:
		i=i+1
		tmp = arr1[i]
		dist = math.sqrt(sum([(round(a,4) - round(b,4)) ** 2 for a, b in zip(arr1[i], trainwo)]))
		print('%s\t%s\t%s' % (word+str(i),dist,label))

