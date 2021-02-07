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

filename2 = os.path.join(os.path.dirname(__file__), 'data', 'name_id.csv')

f = codecs.open( filename2, "r", "utf-8" )
for line in f:
    fio = getSurnameAndName(line)
    print(fio)
    #print(fio, an[j])
   # num[fio] = float(an[j])
    #j += 1
f.close() 
