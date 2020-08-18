#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
	line = line.strip()
	trigram,count = line.split('\t')
	print('%s\t%s\t%s' % ('ngram',trigram,count))

