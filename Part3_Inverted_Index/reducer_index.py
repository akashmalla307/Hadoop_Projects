#! /usr/bin/python3
 
from sys import stdin
import re
 
index = {}
         
for line in stdin:
	line=line.strip()
	word, doc_id = line.split('\t')
	index.setdefault(word, {})
	index[word].setdefault(doc_id) 
                 
                 
for word in index:
	doc_list =[doc_id for doc_id in index[word]]
	docs = ','.join(doc_list)
	print('%s\t%s' % (word, docs))
