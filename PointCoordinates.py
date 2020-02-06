#!/usr/bin/env python
# -*- coding: utf-8 -*-
   
import os
import codecs
import operator

# read from from folder ./data
filename = os.path.join(os.path.dirname(__file__), 'data', 'dates.csv')

f = codecs.open( filename, "r", "utf-8" )

# lifespan - average length of life, for each year (1669 - 1968)
lifespan1 = dict()
lifespan_max = dict()
lifespan_min = dict()
lifespan_mean = dict()
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
    min = 200
    max = 0
    index = 0
    m = 0
    sum = 0
    for cur in b:
        if cur == a:
            m += 1
            age = d[index] - cur
            if age > max: max = age
            if age < min: min = age
            sum += age
        index += 1  
    a += 1
    count_math[a] = m
    if m == 0:
       zero +=1
    elif m == 1:
        lifespan1[a] = sum
    else:
        
        result = round( (sum / m), 0)
        lifespan_mean[a] = result
        lifespan_max[a] = max
        lifespan_min[a] = min
    
     
f1 = open('lifespan_mean.txt', 'w')
f2 = open('lifespan_min.txt', 'w')
f3 = open('lifespan_max.txt', 'w')
f4 = open('lifespan1.txt', 'w')
f5 = open('x_one.txt', 'w')
f6 = open('x_many.txt', 'w')

for i in lifespan1:
    f4.write(str(lifespan1[i])+ '\n')
    f5.write(str(i-1)+ '\n')

for i in lifespan_mean:
    f1.write(str(lifespan_mean[i])+ '\n')
    f6.write(str(i-1)+ '\n')
    
for i in lifespan_max:
    f3.write(str(lifespan_max[i])+ '\n')
    
for i in lifespan_min:
    f2.write(str(lifespan_min[i])+ '\n')
    
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()

f.close() 
