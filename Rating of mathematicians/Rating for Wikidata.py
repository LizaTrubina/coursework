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
num2 = dict()
m = 7
n = 2085
an1 = np.empty((n)) # min square
an2 = np.empty((n))

r = np.empty((n,2))   
k = 0
for line in f1:
    line = line.split(',')
    an1[k] = (int(line[0])*3.24) + (int(line[1])*(13.18))+ (int(line[2])*(4.92)) + (int(line[3])*(2.87)) + (int(line[4])*(3.8)) + (int(line[5])*0.26) + (int(line[6])*(0.42))
    an2[k] = (int(line[0])*0.33) + (int(line[1])*0.17)+ (int(line[2])*0.15) + (int(line[3])*0.3) + (int(line[4])*0.29) + (int(line[5])*0.25) + (int(line[6])*0.0095)
    k += 1   
j = 0
f = codecs.open( filename2, "r", "utf-8" )
for line in f:
    fio = getSurnameAndName(line)

    x = round(an1[j], 3)
    y = round(an2[j], 3)
    
    num[fio] = float(x)
    num2[fio] = float(y)
    j += 1
f.close() 

list_d = list(num.items())
list_d.sort(reverse = True, key=lambda i: i[1])

list_d2 = list(num2.items())
list_d2.sort(reverse = True, key=lambda i: i[1])

result1 = np.empty((1, 2085))
result2 = np.empty((1, 2085))
bufsize = 1

f = open('min_square.csv', 'a', buffering=bufsize,  encoding = 'utf-8')
j=0
for i in list_d:
    a = str(i[0])
    b = str(i[1])
    f.write(' ' + a + ': ' + b + '\n')
f.flush()

f2 = open('unscient.csv', 'a', buffering=bufsize,  encoding = 'utf-8')
for i in list_d2:
    a = str(i[0])
    b = str(i[1])
    f2.write(' ' + a + ': ' + b + '\n')
f2.flush()
print(1)
input("Press Enter to continue...")
