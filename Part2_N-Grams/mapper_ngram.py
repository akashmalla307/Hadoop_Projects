#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
	line = line.strip()
	s = re.sub(r'[^\w\s]','',line)
	words = s.split()
	length = len(words)
	if(length > 0):
		print('%s\t%s' % (s, length))

