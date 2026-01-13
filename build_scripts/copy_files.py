'''
Setup and convert the 
'''
import subprocess
import os
import csv

SOURCE_DIR = "./src/"
BUILD_DIR = "./repo_example/m2-dcp"
FILES_CHANGED_CSV = os.path.join("./files.csv")


# Read in the files that changed
csv_reader = csv.DictReader(open(FILES_CHANGED_CSV))

for row in csv_reader:
    print(row['source_path'])