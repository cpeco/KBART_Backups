#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 08:30 2021

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
    last_oclc_collection_id = 0 
    for lineno, line in enumerate(bigfile):
        current_oclc_collection_id = line.split('\t')[-5] #Identifies the collection ID column within the big file.
        oclc_collection_name = line.split('\t')[-6] #Identifies the collection name column within the big file.
        oclc_collection_name_edit = oclc_collection_name.replace('/','-').replace(':', '--') #Replaces non-admissable characters within collection names, so that they can be used in filenames.
        if current_oclc_collection_id != last_oclc_collection_id: #Sets the condition that if the collection ID changes, a new partitioned file will be created for each new collection ID. 
            if smallfile:
                smallfile.close()
            small_filename = f'{date}_backup_{current_oclc_collection_id}_{oclc_collection_name_edit}.txt' #Establishes the filename format for partitioned files, which includes date, collection ID, and collection name.
            smallfile = open(small_filename, "w")
            smallfile.write(header_line) #Includes the header row at the top of each partitioned file. 
            last_oclc_collection_id = current_oclc_collection_id
        smallfile.write(line)
    if smallfile:
        smallfile.close()