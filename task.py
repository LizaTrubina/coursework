#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
import operator

# read from from folder ./data
filename = os.path.join(os.path.dirname(__file__), 'data', 'query.csv')

f = codecs.open( filename, "r", "utf-8" )
# f = open( filename, 'r')
sum = 0
count = 0
for line in f:
 
    line = line.split(',')
    # print("len(line) = {0}".format(len(line)))
    if len(line) == 3 and line[1] and line[2]:
        
        count = count + 1
        date_b = line[1]
        date_d = line[2]       
        sum = sum +( int(date_d) - int(date_b))
       
    else: continue

age = round((sum/count), 0)
print(age)


f.close() 
