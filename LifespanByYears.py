#!/usr/bin/env python
# -*- coding: utf-8 -*-
   
import os
import codecs
import operator

# read from from folder ./data
filename = os.path.join(os.path.dirname(__file__), 'data', 'dates.csv')

f = codecs.open( filename, "r", "utf-8" )

# lifespan - average length of life, for each year (1669 - 1968)
lifespan = dict()
# count_math[i] = V means that V mathematicians lived in the year i
count_math = dict()
d = []
b = []
i = 0
count = 0
min_year = 2019
max_year = 0
for line in f:
    if line[0] == '"':
        line = line.split(',')
        if len(line) == 4 and line[2] !='' and line[3] != '\n':
            year = int(line[2])
            # print(year)
            if year < min_year:
                min_year = year
                
            if year > max_year:
                max_year = year
            
            b.insert(i, year)
            d.insert(i, int(line[3]))
            count += 1
            i += 1
        else: continue
        
    else:
        line = line.split(',')
        if len(line) == 3 and line[1] !='' and line[2] != '\n' :
            year = int(line[1])
            # print(year)
            if year < min_year:
                min_year = year
                
            if year > max_year:
                max_year = year
                
            b.insert(i, year)
            d.insert(i, int(line[2]))
            count += 1
            i += 1

a = min_year
cur = 0
sum = 0
m = 0
zero = 0
while a < (max_year + 1):
    index = 0
    m = 0
    sum = 0
    for cur in b:
        if cur == a:
            m += 1
            age = d[index] - cur
            sum += age
        index += 1  
    a += 1
    count_math[a] = m
    if m == 0:
       # lifespan[a] = 0
       zero +=1
    else:
            result = round( (sum / m), 0)
            lifespan[a] = result
            
f1 = open('y_lifespan.txt', 'w')
f2 = open('x_lifespan.txt', 'w')
f3 = open('count_lifespan.txt', 'w')
for i in lifespan:
    f1.write(str(lifespan[i])+ '\n')
    f2.write(str(i-1)+ '\n')
    f3.write(str(count_math[i])+ '\n')
f1.close()
f2.close()
f3.close()

for i in lifespan:
    print (i-1,":", lifespan[i], "", count_math[i])
print("0=" , zero)    
                           
f.close() 
