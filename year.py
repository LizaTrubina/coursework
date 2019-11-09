#!/usr/bin/env python
# -*- coding: utf-8 -*-
   
import os
import codecs
import operator

# read from from folder ./data
filename = os.path.join(os.path.dirname(__file__), 'data', 'dates.csv')

f = codecs.open( filename, "r", "utf-8" )
year = input("Введите год:")
year= int(year)
count = 0
for line in f:
    if line[0] == '"':
        line = line.split(',')
        if len(line) == 4 and line[2] !='' and line[3] != '\n':
            date_b = line[2]
            date_d = line[3]
            if int(date_b) < year and year < int(date_d):
                count = count + 1
        else: continue
        
    else:
        line = line.split(',')
        if len(line) == 3 and line[1] !='' and line[2] != '\n' :
            date_b = line[1]
            date_d = line[2]
            if int(date_b) < year and year < int(date_d):
                count = count + 1

print('количество математиков на',year,'год:',count)
f.close() 
