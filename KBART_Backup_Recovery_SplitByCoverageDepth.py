#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 2024

@author: cpecos
"""
from datetime import datetime

#Need to replace file_name.txt with the name of the file you wish to partition
filename = 'file_name.txt'
#The date that you run the file-splitting will be automatically appended to the front of each split file. 
#If you wish to override this, you will need to change that on this line here.
date = datetime.now().strftime("%Y-%m-%d")

smallfile = None
with open(filename) as bigfile:
    header_line = bigfile.readline() #Identifies the first line of the big file as being a header row.
    last_coverage_depth = 0 
    for lineno, line in enumerate(bigfile):
        current_coverage_depth = line.split('\t')[13] #Identifies the coverage depth column within the big file.
        if current_coverage_depth != last_coverage_depth: #Sets the condition that if the coverage depth changes, a new partitioned file will be created for each new coverage depth category.
            if smallfile:
                smallfile.close()
            small_filename = f'{date}_backup_{current_coverage_depth}.txt' #Establishes the filename format for partitioned files, which includes date, collection ID, and collection name.
            smallfile = open(small_filename, "a")
            smallfile.write(header_line) #Includes the header row at the top of each partitioned file. 
            last_coverage_depth = current_coverage_depth
        smallfile.write(line)
    if smallfile:
        smallfile.close()