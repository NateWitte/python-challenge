#Need to import os and csv
import os
import csv

#Variables
votecount = 0
votedcandidates = []
with open('election_data.csv') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        votecount=votecount+1
        candidate = row[2]
        newcandidate = True
        for people in votedcandidates:
            if candidate == people:
                newcandidate = False
        
        if newcandidate == True:
            votedcandidates.append(candidate)

for i in votedcandidates:
    print(f"{i}")


print(f"Total number of votes: {votecount}")