#!/usr/bin/env python
# -*- coding: utf-8 -*-
# пример комментария по-русски

#
# Read Wikidata list of persons, extracts expert's rating and other parameters

def getSurnameAndName(string):
    first = string.index('"',0, len(string))
    end = string.rindex('"',0, len(string))
    name = string[first+1:end]
    return name
    
import os

# read from from folder ./data
filename = os.path.join(os.path.dirname(__file__), 'data', 'WP_Person_math.csv')

# print(filename)
# print("Start reading file")
f = open( filename, 'r')
date = dict()
rating = dict()

# content = f.readlines()

for line in f: 
    # extract name of person, print Name="..", 
    # split by comma, extract (1) expert rating, (2) year of article creation, 
    # e.g. rating=N, article_year=2013
    print("source = "+line)
    
    fio= getSurnameAndName(line)
    # print("fio: {}\n".format(fio))
    
    # cut off the surname and name from line
    end = line.rindex('"',0, len(line))
    line = line[end + 2:]
    # print("line without name = {}\n".format(line))
    line = line.split(',')
    # print("after split line = {}".format(line))
    d = line[1]
    year =line[5]
    # i = int(year) - 2001
    rating[fio] = d
    date[fio] = year
    print('rating:' + fio + ': ' + rating[fio])
    print( fio + ': ' +"{}\n".format(date[fio]))  

f.close() 
