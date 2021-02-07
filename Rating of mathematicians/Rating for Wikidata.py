#!/usr/bin/env python
# -*- coding: utf-8 -*-

def getSurnameAndName(string):
    first = string.index(',',0,len(string))
    end = len(string)
    if string.find('"') == -1:
        name1 = string[first+1:end-1]
        name1 = name1.split(' ')
        if len(name1) == 2:
            name = name1[1] + ", " + name1[0]
        elif len(name1) == 3:
            name = name1[2] + ', ' + name1[0]+ ' ' + name1[1]
        else: name = name1[0]
    else:
        name = string[first+2:end-2]        

    return name

import os
import codecs
import operator
import numpy as np
import csv

# read data
filename1 = os.path.join(os.path.dirname(__file__),  'table.csv')
filename2 = os.path.join(os.path.dirname(__file__),  'name.csv')
f1 = codecs.open( filename1, "r", "utf-8" )

num = dict()
m = 7
n = 2065
an = np.empty((n))
    
k = 0
for line in f1:
    line = line.split(',')
    an[k] = (int(line[0])*0.3) + (int(line[1])*0.17)+ (int(line[2])*0.15) + (int(line[3])*0.3) + (int(line[4])*0.29) + (int(line[5])*0.2) + (int(line[6])*0.0095)
    k += 1   
j = 0
f = codecs.open( filename2, "r", "utf-8" )
for line in f:
    fio = getSurnameAndName(line)

    x = round(an[j], 3)
    num[fio] = float(x)
    j += 1
f.close() 

list_d = list(num.items())
list_d.sort(reverse = True, key=lambda i: i[1])

f1 = open('rating.csv', mode='a', encoding = 'utf-8')
for i in list_d:
    a = str(i[0])
    b = str(i[1])
    #print(a, ": ",b) 
    f1.write(a + ': ' + b + '\n')
print(1)
