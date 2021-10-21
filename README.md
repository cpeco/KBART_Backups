# KBART_Backups
### Methods for splitting the ["My Selected Titles (KBART)"](https://help.oclc.org/Metadata_Services/WorldShare_Collection_Manager/Knowledge_base_collections/Use_collection_data_with_other_services/Download_knowledge_base_data_for_a_third-party#My_Selected_Titles_(KBART)) file from OCLC WMS

Once you have downloaded your library's "My Selected Titles (KBART)" file, you can use of one of the following Python scripts, hosted in this repository, to split your file into smaller files:  
* [Split by Size](https://github.com/cpeco/KBART_Backups/blob/79465c4d4c39b733c9078a62da7199e686c9e4f2/KBART_Backup_Recovery_SplitBySize.py)
* [Split by Collection ID](https://github.com/cpeco/KBART_Backups/blob/79465c4d4c39b733c9078a62da7199e686c9e4f2/KBART_Backup_Recovery_SplitByCollection.py) 

To use these scripts, you must save the .py file in the same folder as your "My Selected Titles (KBART)" file. Update the script with the exact filename of the "My Selected Titles (KBART)" file (the scripts each indicate where to do this). Then, you should be able to run the script, and partitioned files should appear in that same folder. 
