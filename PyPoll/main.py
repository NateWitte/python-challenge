#Need to import os and csv
import os
import csv

#Variables
votecount = 0
with open('election_data.csv') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        votecount=votecount+1
print(f"Total number of votes: {votecount}")