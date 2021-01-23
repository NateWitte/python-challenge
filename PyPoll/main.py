#Need to import os and csv
import os
import csv

#Variables
votecount = 0
votedcandidates = {}
with open('election_data.csv') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        votecount=votecount+1
        candidate = row[2]
        if not candidate in votedcandidates:
            votedcandidates[candidate]=1
        else:
            votedcandidates[candidate]+=1

print("Election Results")
print("-------------------------")
print(f"Total Votes: {votecount}")
print("-------------------------")
winner="None"
mostvotes=0
for i in votedcandidates:
    if votedcandidates[i]>mostvotes:
        mostvotes=votedcandidates[i]
        winner = i
    thiscandidate=i
    votes = votedcandidates[i]
    percentage = (votes/votecount)*100
    percentage = round(percentage,3)
    print(f"{i}: {percentage}% ({votedcandidates[i]})")
