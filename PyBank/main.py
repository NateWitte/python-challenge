#Need to import os and csv
import os
import csv

#Since it is already in our "PyBank" folder, we can just open it
with open('budget_data.csv') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")