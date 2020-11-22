#!/usr/bin/env python
# -*- coding: utf-8 -*-
   
import os
import codecs
import operator
import numpy as np

# read from from folder ./data
filename1 = os.path.join(os.path.dirname(__file__), 'data', '1.csv')
filename2 = os.path.join(os.path.dirname(__file__), 'data', '2.csv')
filename3 = os.path.join(os.path.dirname(__file__), 'data', 'count_lang.csv')
filename4 = os.path.join(os.path.dirname(__file__), 'data', 'name.csv')

f1 = codecs.open( filename1, "r", "utf-8" )
f2 = codecs.open( filename2, "r", "utf-8" )
f3 = codecs.open( filename3, "r", "utf-8" )
f4 = codecs.open( filename4, "r", "utf-8" )

m = 3
n = 6
arr = np.empty((n, m), dtype=object)
for k in range(n):
    arr[k][2] = 0
    
i = 0
for line in f1:
    if line[0] == '"':
        line = line.split(',')
        arr[i][0] = int(line[2])
        i += 1
                
    else:
        line = line.split(',')
        arr[i][0] = int(line[1])
        i += 1
i = 0
for line in f2:
    if line[0] == '"':
        line = line.split(',')
        arr[i][1] = int(line[2])
        i += 1
                
    else:
        line = line.split(',')
        arr[i][1] = int(line[1])
        i += 1

f1.close()
f2.close()
f1 = codecs.open( filename1, "r", "utf-8" )
i = 0
for line in f1:
    for arg in f3:
        if line[0] == '"' and arg[0] == '"':
            line = line.split(',')
            arg = arg.split(',')
            if line[0] == arg[0] and line[1] == arg[1]:
                arr[i][2] = int(arg[2])

        if line[0] != '"' and arg[0] != '"':
            line = line.split(',')
            arg = arg.split(',')
            if line[0] == arg[0]:
                arr[i][2] = int(arg[1])
    i +=1

    
for k in range(n):
    for j in range(m):
        print(arr[k][j], end=' ')
    print()
