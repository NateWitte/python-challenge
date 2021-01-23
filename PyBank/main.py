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
#Output to Terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {monthcounter}")
print(f"Total: ${round(totalcounter)}")
print(f"Average Change: ${round(averagedifference,2)}")
print(f"Greatest Increase in Profits: {maxdifmonth} (${round(maxdifference)})")
print(f"Greatest Decrease in Profits: {mindifmonth} (${round(mindifference)})")

#Output to TxT file
text_file = open("FinancialAnalysis.txt", "w")
text_file.write("Financial Analysis\n")
text_file.write("----------------------------\n")
text_file.write(f"Total Months: {monthcounter}\n")
text_file.write(f"Total: ${round(totalcounter)}\n")
text_file.write(f"Average Change: ${round(averagedifference,2)}\n")
text_file.write(f"Greatest Increase in Profits: {maxdifmonth} (${round(maxdifference)})\n")
text_file.write(f"Greatest Decrease in Profits: {mindifmonth} (${round(mindifference)})\n")
text_file.close()
