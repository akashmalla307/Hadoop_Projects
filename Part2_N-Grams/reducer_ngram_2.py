#!/usr/bin/env python3
import sys
from operator import itemgetter 

wordcount = {}
ngram ={}
keywords=['science','sea','fire']

for line in sys.stdin:
	line = line.strip()
	tmpword,trigram, count = line.split('\t')
	#words = line.split()
	#length = len(words)
	try:
		ngram[trigram] = ngram[trigram]+int(count)
	except:
		ngram[trigram] = int(count)

N=10
res = dict(sorted(ngram.items(), key = itemgetter(1), reverse = True)[:N]) 
for x, y in res.items():
  print('%s\t%s' % (x,y))
