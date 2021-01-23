#Need to import os and csv
import os
import csv

#Variables
votecount = 0
votedcandidates = {}
with open('election_data.csv') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        votecount=votecount+1
        candidate = row[2]
        if not candidate in votedcandidates:
            votedcandidates[candidate]=1
        else:
            votedcandidates[candidate]+=1

for i in votedcandidates:
    print(f"{i} received {votedcandidates[i]} votes")


print(f"Total number of votes: {votecount}")