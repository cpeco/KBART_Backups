#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 19:36:31 2021

@author: cpecos
"""

lines_per_file = 500000 #Sets the number of lines that will be in each partitioned file.
smallfile = None
with open('file_name.txt') as bigfile: #Need to replace file_name.txt with the name of the file you wish to partition
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0: #The files will be partitioned every time you reach the set number of lines_per_file.
            if smallfile:
                smallfile.close()
            small_filename = 'small_file_{}.txt'.format(lineno + lines_per_file) #Sets the structure for filenames for partitioned files.
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()