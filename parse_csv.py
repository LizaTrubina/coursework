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

# read from from folder ./data
filename = os.path.join(os.path.dirname(__file__), 'data', '19DecWP_Person_math_matem.csv')
# filename = os.path.join(os.path.dirname(__file__), 'data', 'WP_Person_math.csv')

f = codecs.open( filename, "r", "utf-8" )
# f = open( filename, 'r')
# date = dict()
# rating = dict()
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
    print("line = '{0}'".format(line))
    line = line.split(',')
    print("len(line) = {0}".format(len(line)))
    rat = line[1]
    year = line[5]

    if year and rat:            # parse only the year is available
       # date[fio] = year
        age = 2019-int(year)
       # rating[fio] = rat
        sum= round((0.38 * age)+ (0.3* int(rat)),1) # todo move round to print format
        my_rating[fio] = sum
        print( fio + ': ' +"{}\n".format(my_rating[fio])) 
       # print('rating:' + fio + ': ' + rating[fio])
       # print( fio + ': ' +"{}\n".format(date[fio]))  
 

f.close() 
