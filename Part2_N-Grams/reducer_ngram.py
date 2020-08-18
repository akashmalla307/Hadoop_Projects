#!/usr/bin/env python3
import sys
from operator import itemgetter 

wordcount = {}
ngram ={}
keywords=['science','sea','fire']
n=0
tmp1='-'
tmp2='-'
for line in sys.stdin:
	line = line.strip()
	line, count = line.split('\t')
	words = line.split()
	length = len(words)
	i =0
	while(i+2<int(count)):
		first = words[i]
		second = words[i+1]
		third = words[i+2]
		i = i+1
			
		#if n > 0:	
		#	if first in keywords:
		#		word = tmp2+"_"+tmp1+"_$"
		#		try:
		#			ngram[word] = ngram[word]+1
		#		except:
		#			ngram[word] = 1

		if first in keywords:
			word="$_"+second+"_"+third
			try:
				ngram[word] = ngram[word]+1
			except:
				ngram[word] = 1
		elif second in keywords:
			word=first+"_$_"+third
			try:
        			ngram[word] = ngram[word]+1
			except:
				ngram[word] = 1
		elif third in keywords:
			word=first+"_"+second+"_$"
			try:
        			ngram[word] = ngram[word]+1
			except:
				ngram[word] = 1
	#tmp1 = words[length-2]
	#tmp2 = words[length-1]
	#n = n+1
N=10
res = dict(sorted(ngram.items(), key = itemgetter(1), reverse = True)[:N]) 
for x, y in res.items():
  print('%s\t%s' % (x,y))
