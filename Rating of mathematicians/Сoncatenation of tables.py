#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
import operator
import numpy as np

# read data
filename1 = os.path.join(os.path.dirname(__file__), 'field_of_work.csv')
filename2 = os.path.join(os.path.dirname(__file__), 'languages.csv')
filename3 = os.path.join(os.path.dirname(__file__), 'notable_work.csv')
filename4 = os.path.join(os.path.dirname(__file__), 'academic_degree.csv')
filename5 = os.path.join(os.path.dirname(__file__), 'award.csv')
filename6 = os.path.join(os.path.dirname(__file__), 'professorship.csv')
filename7 = os.path.join(os.path.dirname(__file__), 'foreign_label.csv')

f1 = codecs.open( filename1, "r", "utf-8" )
f2 = codecs.open( filename2, "r", "utf-8" )
f3 = codecs.open( filename3, "r", "utf-8" )
f4 = codecs.open( filename4, "r", "utf-8" )
f5 = codecs.open( filename5, "r", "utf-8" )
f6 = codecs.open( filename6, "r", "utf-8" )

num = dict()
table = dict()
m = 7 # number of parameters
n = 2085 # number of mathematicians
arr = np.empty((n, m))

for k in range(n):
    arr[k][2] = 0
    
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
for line in f3:
    line = line.split(',')
    arr[i][2] = int(line[1])
    i += 1
f3.close()

i = 0
for line in f4:
    line = line.split(',')
    arr[i][3] = int(line[1])
    i += 1
f4.close()

i = 0
for line in f5:
    line = line.split(',')
    arr[i][4] = int(line[1])
    i += 1
f5.close()

i = 0
for line in f6:
    line = line.split(',')
    arr[i][5] = int(line[1])
    i += 1
f6.close()

i = 0
f8 = codecs.open(filename3, "r", "utf-8" )
for line in f8:
    line = line.split(',',maxsplit=1)
    f7 = codecs.open( filename7, "r", "utf-8" )
    for arg in f7:        
        arg = arg.split(',')
        if line[0] == arg[0]:
                arr[i][6] = int(arg[1])
                f7.close()
                break
        else: continue
    i +=1
f8.close()

np.savetxt('table.csv', arr,fmt="%d", delimiter=',')
print('1')

