import os
import codecs
import operator
import numpy as np
import csv

# read data
# filename1 = os.path.join(os.path.dirname(__file__),  'all_data.csv')
filename1 = os.path.join(os.path.dirname(__file__),  'all_data.csv')
#f1 = codecs.open( filename1, "r", "utf-8")
#filename2 = os.path.join(os.path.dirname(__file__),  'table_1.csv')
filename2 = os.path.join(os.path.dirname(__file__),  'TABLE_ALL_1.csv')
f2 = codecs.open( filename2, "r", "utf-8")

n = 2646

arr = np.empty((n, 2))
for line in f2:
    i = 0 
    line = line.split(',')

    f1 = codecs.open( filename1, "r", "utf-8")
    for arg in f1:
        arg = arg.split(',')

        if line[0] == arg[0]:
            arr[i][0] = int(line[1])
        if line[0] == arg[1]:
            arr[i][1] = int(line[1])
        i += 1
    f1.close

np.savetxt('input.csv', arr,fmt="%d", delimiter=' ')

#j=0
#while (j<n):
   # print(arr[j][0], ": ", arr[j][1])
   # j += 1
