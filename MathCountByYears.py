#!/usr/bin/env python
# -*- coding: utf-8 -*-
   
import os
import codecs
import operator

# read from from folder ./data
filename = os.path.join(os.path.dirname(__file__), 'data', 'dates.csv')

f = codecs.open( filename, "r", "utf-8" )
count = 0
b = []
d = []
count_year = dict()
min_year = 2019
max_year = 0
i = 0
for line in f:
    if line[0] == '"':
        line = line.split(',')
        if len(line) == 4 and line[2] !='' and line[3] != '\n':
            date_b = int(line[2])
            date_d = int(line[3])
            
            if date_b < min_year:
                min_year = date_b
                
            if date_d > max_year:
                max_year = date_d
            i += 1
            b.insert(i, date_b)
            d.insert(i, date_d)

        else: continue
        
        
    else:
        line = line.split(',')
        if len(line) == 3 and line[1] !='' and line[2] != '\n' :
            date_b = int(line[1])
            date_d = int(line[2])

            if date_b < min_year:
                min_year = date_b
                
            if date_d > max_year:
                max_year = date_d
            i += 1
            b.insert(i, date_b)
            d.insert(i, date_d)
            
            i += 1
print( min_year, max_year)

a = min_year
while a < (max_year + 1):
    index = 0
    count = 0
    for cur in b:
        if cur <= a and  a <= d[index]:
            count += 1
        index += 1  
    a += 1
    count_year[a] = count
    
f1 = open('y.txt', 'w')
f2 = open('x.txt', 'w')
for i in count_year:
    f1.write(str(count_year[i])+ '\n')
    f2.write(str(i-1)+ '\n')
   
f1.close()
f2.close()

for i in count_year:
    print (i-1,":", count_year[i])
                

f.close() 
