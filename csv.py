import random
import csv
import os

def write_record(path,p,i,t,r):
    # find if file exists
    file_exists = False
    if os.path.exists(path):
        file_exists = True
    with open(path, 'a') as file:
        results_writer = csv.writer(file)
        results_writer.writerow([p,i,t,r])
        

    