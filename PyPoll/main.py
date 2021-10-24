# Import dependencies
import os
import csv
from collections import Counter
# Define the path and read in the csv file
with open("Resources/election_data.csv", 'r') as election_data:
    csv_reader=csv.reader (election_data, delimiter=',')
    csv_header=next(csv_reader)
# Declaration for the variable   
    votes=[]  
# Looping through the csv files to store the pool of the votes into the variable votes
    for row in csv_reader:
        votes.append(row[2])
# count the votes for each candidates using the counter function
#caculate the total votes by len() and store in total_votes and print and write to the analysis_result.txt file
counts=Counter(votes)
total_votes=len(votes)
print("Election Results")
print("------------------------------")
print(f"Total Votes:{total_votes}")
print("------------------------------")
f=open('analysis/analysis_result.txt', 'w')
f.write("Election Results\n")
f.write("------------------------------\n")
f.write(f"Total Votes:{total_votes}\n")
f.write("------------------------------\n")
# parse the candidates and vote counts into two lists
Candidates=counts.keys()
votes_pool=counts.values()
#loop through the candidates to print out and write to the txt file for the percentage of votes for each candiates
for candidate  in Candidates:
    percentage_of_votes=round(counts[candidate]/total_votes*100,3)
    print(f"{candidate}: {percentage_of_votes}% ({counts[candidate]})")
    f.write(f"{candidate}: {percentage_of_votes}% ({counts[candidate]})\n")
# Loop through the candidates again to find the winner and also print and write to the txt output file. 
print("------------------------------")
f.write("------------------------------\n")
for candidate  in Candidates: 
    if counts[candidate]==max(votes_pool):     
        print(f"winner: {candidate}")
        f.write(f"winner: {candidate}\n")
print(f"-----------------------------")
f.write("------------------------------\n")
f.close()
# Checking if the data is written to file or not
file= open('analysis/analysis_result.txt', 'r')
print(file.read())
file.close()




