def getSurnameAndName(b_line):
    first = string.index(',',0,len(b_line))
    end = len(b_line)
    if b_line.find('"') == -1:
        name1 = b_line[first+1:end-1]
        name1 = name1.split(' ')
        if len(name1) == 2:
            name = name1[1] + ", " + name1[0]
        elif len(name1) == 3:
            name = name1[2] + ', ' + name1[0]+ ' ' + name1[1]
        else: name = name1[0]
    else:
        name = b_line[first+2:end-2]        

    return name

import os
import codecs
import operator
import numpy as np
import csv

# read data
filename1 = os.path.join(os.path.dirname(__file__),  'maths.csv')
f1 = codecs.open( filename1, "r", "utf-8" )
filename3 = os.path.join(os.path.dirname(__file__),  'advisor.csv')
f3 = codecs.open( filename3, "r", "utf-8" )
filename5 = os.path.join(os.path.dirname(__file__),  'academy.csv')
f5 = codecs.open( filename5, "r", "utf-8" )

x = 32 #len("http://www.wikidata.org/entity/Q")
f2 = open('id_m.csv', mode='a', encoding = 'utf-8')
for line in f1:
    end = line.index(',',0,len(line))
    b_line = line[end+1:len(line)]
    #fio = getSurnameAndName(b_line)
    a = line[32:end]
    #print(a, ": ", b_line)
    f2.write(a+ '\n')
f1.close()
f2.close()

f4 = open('id_adv.csv', mode='a', encoding = 'utf-8')
for line in f3:
    end = line.index(',',0,len(line))
    b_line = line[end+1:len(line)]
    #fio = getSurnameAndName(b_line)
    a = line[32:end]
    #print(a, ": ", b_line)
    f4.write(a+ '\n')
f4.close()
f3.close()

f6 = open('id_acad.csv', mode='a', encoding = 'utf-8')
for line in f5:
    end = line.index(',',0,len(line))
    b_line = line[end+1:len(line)]
    #fio = getSurnameAndName(b_line)
    a = line[32:end]
    #print(a, ": ", b_line)
    f6.write(a+ '\n')
f5.close()
f6.close()
print(1)
