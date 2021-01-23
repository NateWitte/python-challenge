#Need to import os and csv
import os
import csv

#Create variables
monthcounter = 0
totalcounter = 0
previoustotal = 0
maxdifference = 0
maxdifmonth = "None"
mindifference = 0
mindifmonth = "None"
totaldifference = 0
#Since it is already in our "PyBank" folder, we can just open it
with open('budget_data.csv') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        currentvalue = float(row[1])
        monthcounter=monthcounter+1
        totalcounter=totalcounter + currentvalue
        difference = currentvalue-previoustotal
        if monthcounter>1:
            totaldifference = totaldifference + difference
            if (difference>maxdifference):
                maxdifference = difference
                maxdifmonth = row[0]
            if (difference <mindifference):
                mindifference = difference
                mindifmonth = row[0]
        previoustotal = currentvalue

    averagedifference=totaldifference/(monthcounter-1)
    print(f"Total Months: {monthcounter}")
    print(f"Total: {totalcounter}")
    print(f"Average Difference: {averagedifference}")
    print(f"Max difference was {maxdifference} on {maxdifmonth}")
    print(f"Min difference was {mindifference} on {mindifmonth}")