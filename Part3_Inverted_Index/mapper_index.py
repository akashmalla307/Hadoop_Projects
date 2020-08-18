#! /usr/bin/python3
 
from sys import stdin
import re
import os
 
for line in stdin:
	doc_id=os.environ["map_input_file"]
	doc_id1 = re.findall(r'\w+' ,doc_id)[-1]
	doc_id2 = re.findall(r'\w+' ,doc_id)[-2]
	doc_id  =  "%s.%s " % (doc_id2,doc_id1)
	words = re.findall(r'\w+', line.strip())
                 
	for word in words:
		print("%s\t %s" % (word.lower(), doc_id))
