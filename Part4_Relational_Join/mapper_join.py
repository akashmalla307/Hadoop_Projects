#!/usr/bin/python3

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split('\t')
    name = "-"
    id1 = ""
    code ="-"
    place = "-"
    salary = "-"
    
    if len(line) == 2:
       if line[0] != 'Employee':
             id1 = line[0]
             name = line[1]
    else:
        if line[0] != 'Employee':
              id1 = line[0]
              salary = line[1]
              place = line[2]
              code = line[3]
    if id1 != 'Employee ID':
        print('%s\t%s\t%s\t%s\t%s' % (id1,name,salary,place,code))

