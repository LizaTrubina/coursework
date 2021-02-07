#!/usr/bin/env python
# -*- coding: utf-8 -*-

def getSurnameAndName(string):
    first = string.index(',',0,len(string))
    end = len(string)
    name = string[first+1:end-1]
    return name

import os
import codecs
import operator
import numpy as np

# read from from folder ./data
filename1 = os.path.join(os.path.dirname(__file__), 'data', 'id_1.csv')
filename2 = os.path.join(os.path.dirname(__file__), 'data', 'id_2.csv')
filename3 = os.path.join(os.path.dirname(__file__), 'data', 'id_lang.csv')
filename4 = os.path.join(os.path.dirname(__file__), 'data', 'name_id.csv')

f1 = codecs.open( filename1, "r", "utf-8" )
f2 = codecs.open( filename2, "r", "utf-8" )

f4 = codecs.open( filename4, "r", "utf-8" )
num = dict()

m = 3
n = 10
arr = np.empty((n, m), dtype=object)
#for k in range(n):
#   arr[k][2] = 0
    
i = 0
for line in f1:
    line = line.split(',')
    arr[i][0] = int(line[1])
    i += 1
f1.close()

i = 0
for line in f2:
    line = line.split(',')
    arr[i][1] = int(line[1])
    i += 1
f2.close()

i = 0
for line in f4:
    line = line.split(',',maxsplit=1)
    f3 = codecs.open( filename3, "r", "utf-8" )
    for arg in f3:        
        arg = arg.split(',')
        if line[0] == arg[0]:
                arr[i][2] = int(arg[1])
                f3.close()
                break
        else: continue
    i +=1
f4.close()

j = 0
f = codecs.open( filename4, "r", "utf-8" )
for line in f:
    fio = getSurnameAndName(line)
    num[fio] = int(arr[j][2])
    j += 1
    
list_d = list(num.items())
list_d.srt(key=lambda i: i[1])
for i in list_d:
    print(i[0], ':', i[1])

f.close() 

# np.savetxt('file.txt', arr, delimiter=',')

for k in range(n):
    for j in range(m):
        print(arr[k][j], end=' ')
    print()
