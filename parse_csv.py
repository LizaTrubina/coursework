#!/usr/bin/env python
# -*- coding: utf-8 -*-
# пример комментария по-русски

# Read Wikidata list of persons, extracts expert's rating and other parameters

def getSurnameAndName(string):
    first = string.index('"',0, len(string))
    end = string.rindex('"',0, len(string))
    name = string[first+1:end]
    return name
    
import os
import codecs
import operator

# read from from folder ./data
filename = os.path.join(os.path.dirname(__file__), 'data', '19DecWP_Person_math_matem.csv')

f = codecs.open( filename, "r", "utf-8" )
# f = open( filename, 'r')

my_rating = dict()

for line in f:
 #   line.encode('cp1251').decode('utf-8')
    # extract name of person, print Name="..", 
    # split by comma, extract (1) expert rating, (2) year of article creation, 
    # e.g. rating=N, article_year=2013
    
    fio= getSurnameAndName(line)
    
    # cut off the surname and name from line
    end = line.rindex('"',0, len(line))
    line = line[end + 2:]
    line = line.split(',')
    # print("len(line) = {0}".format(len(line)))
    if len(line) == 33 and line[1] and line[5]:

        rating = line[1]
        year = line[5]
        # if year and rating:            # parse only the year is available
        age = 2019-int(year)
        sum= round((0.34 * age)+ (0.5* int(rating)),0) # todo move round to print format
        my_rating[fio] = sum

        # print( fio + ': ' +"{}\n".format(my_rating[fio])) 
                    # print('rating:' + fio + ': ' + rating[fio])
                   # print( fio + ': ' +"{}\n".format(date[fio]))
    else: continue


list_d = list(my_rating.items())
list_d.sort(key=lambda i: i[1])
for i in list_d:
    print(i[0], ':', i[1])

f.close() 
