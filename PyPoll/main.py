import os 
import csv

#set file path
csvfile = os.path.join("C:/Users/Abbi/Desktop/election_data.csv")

#declare variables
total_votes = 0
candidates = {}
winner = []
max_votes = []

#read data
with open(csvfile, "r") as file: 
    reader = csv.reader(file)
    #skip header
    next(reader)

    #loop through each row
    for row in reader:
        #count votes
        total_votes += 1

        #get candidate name from row
        can_name = row[2]

        #check if candidates name is aldready in dict
        if can_name in candidates:
           candidates[can_name] += 1

        else:
            candidates[can_name] = 1

#set new vairable
results = []

#go through candidates and calculate percenatge of votes
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, votes, percentage))

#find the winner
for candidates, votes, percentage in results:
    if votes > max_votes:
        max_votes = votes
        winner = candidate