#Need to import os and csv
import os
import csv

#Create variables
monthcounter=0
totalcounter=0
#Since it is already in our "PyBank" folder, we can just open it
with open('budget_data.csv') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        monthcounter=monthcounter+1
        totalcounter=totalcounter + float(row[1])

    print(f"Total Months: {monthcounter}")
    print(f"Total: {totalcounter}")
    print("This is a test")
