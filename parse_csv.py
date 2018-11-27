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
    print line, 

f.close() 
