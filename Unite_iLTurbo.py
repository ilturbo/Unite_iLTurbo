#!/usr/bin/python
# https://github.com/ilturbo

import re

inputList = []
for file in ['File1.txt','File2.txt']:
    with open(file,'r') as infile:
        for line in infile:
            inputList.extend(re.sub('[^A-Za-z0-9,]+', '', line).split(","))
print(inputList)
with open('UniteFile.txt','w') as outfile:
    for line in inputList:
        outfile.write(line + '\n')
