#Need to import os and csv
import os
import csv

#Create variables
rowcounter=0
#Since it is already in our "PyBank" folder, we can just open it
with open('budget_data.csv') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        rowcounter=rowcounter+1

    print(f"Number of rows: {rowcounter}")
