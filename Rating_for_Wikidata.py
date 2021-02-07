#!/usr/bin/env python
# -*- coding: utf-8 -*-
   
import os
import codecs
import operator
import numpy as np


# read from from folder ./data
filename = os.path.join(os.path.dirname(__file__), 'data', 'table.csv')

#f1 = codecs.open( filename1, "r", "utf-8" )

arr = [[1,1,0,0,0,0,2], [3,2,0,1,0,0,1], [5,0,0,0,0,0,5], [5,5,0,1,1,3,8], [5,1,0,1,2,0,6], [1,1,0,0,0,1,2], [1,2,0,0,0,0,5], [5,3,3,1,0,0,46], [13,1,9,3,1,6,142], [11,1,20,4,0,1,166] ]#arr = [[1,1,0,0,0,0,2], [3,2,0,1,0,0,1], [5,0,0,0,0,0,5], [5,5,0,1,1,3,8], [5,1,0,1,2,0,6], [1,1,0,0,0,1,2], [1,2,0,0,0,0,5], [5,3,3,1,0,0,46], [13,1,9,3,1,6,142], [11,1,20,4,0,1,166] ]

for index in np.arange(0, 10, 1):
    y = (0.3*arr[index][0]) + (0.3*arr[index][1])+(0.15*arr[index][2])+(0.17*arr[index][3])+(0.2*arr[index][4])+(0.29*arr[index][5])+(0.0095*arr[index][6])
    print("{:.2f}".format(y))









        
        
