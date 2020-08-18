#!/usr/bin/env python3
import sys
import string

last_user_id = None
name_o="-"
cost_o ="-"
place_o ="-"
code_o ="-"
array = []

for line in sys.stdin:
    line = line.strip()
    id1,name,cost,place,code = line.split('\t')

    if not last_user_id or last_user_id != id1:
         last_user_id = id1
         if name == '-':
            cost_o = cost
            place_o = place
            code_o = code
         else:
            name_o = name 
    elif id1 == last_user_id:
         if name_o == '-':
            name = name
            cost = cost_o
            place = place_o
            code = code_o
         else:
            name = name_o
            cost = cost
            place = place
            code = code
         print(last_user_id,name,cost,place,code)
         name_o= '-'
         
