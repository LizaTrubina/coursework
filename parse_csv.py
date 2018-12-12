#
# Read Wikidata list of persons, extracts expert's rating and other parameters

import os

# read from from folder ./data
filename = os.path.join(os.path.dirname(__file__), 'data', 'WP_Person_math.csv')

print(filename)
print("Start reading file")
f = open( filename, 'r')

# content = f.readlines()

for line in f: 
    # extract name of person, print Name="..", 
    # split by comma, extract (1) expert rating, (2) year of article creation, 
    # e.g. rating=N, article_year=2013
    print("source="+line)
    # line.split(',')
    #print("after split line="+line)

    # get surname and name - make separate function fio=getSurnameAndName(line)
    first = line.index('"',0, len(line))
    end = line.rindex('"',0, len(line))
    fio = line[first+1:end]
    print("first and last quote positions = ({},{}), name='{}'".format(first, end, fio))

    # cut off the surname and name from line
    line = line[end + 2:]
    print("line without name={}\n".format(line))

f.close() 
