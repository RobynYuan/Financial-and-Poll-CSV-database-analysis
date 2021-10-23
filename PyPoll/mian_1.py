import os
import csv
from collections import Counter
with open("Resources/election_data.csv", 'r') as election_data:
    csv_reader=csv.reader (election_data, delimiter=',')
    csv_header=next(csv_reader)
# Declaration for the variable   
    votes=[]  
# Looping through the csv files to store the pool of the votes 
    for row in csv_reader:
        votes.append(row[2])
    counts=Counter(votes)
total_votes=len(votes)
print("Election Results")
print("------------------------------")
print(f"Total Votes:{total_votes}")
print("------------------------------")
Candidates=counts.keys()
votes_pool=counts.values()
for candidate  in Candidates:
    print(f"{candidate}:{counts[candidate]/total_votes*100}% ({counts[candidate]})")
print(f"----------------------------")   
for candidate  in Candidates: 
    if counts[candidate]==max(votes_pool):     
        print(f"winner: {candidate}")
print(f"-----------------------------")
# candidate_information
# A=counts["Khan"]
# print(A)
# B=A/total_votes
# print(B)
# print(counts)
# total_votes=len(votes)
# print(total_votes)
# #    for row in csv_reader:
# #         months.append(row[0])     
# # # caculate the net total 
# #         net_total=sum(profit_Losses)
# # # Looping through the profit_looses list to populate the variable "monthly change'
# #     for i in range(len(profit_Losses)-1):
# #         monthly_change.append(profit_Losses[i+1]-profit_Losses[i])
# # # Find the max and min for the monthly_change and index the row that gives the max and min 
# #     max_increase=max(monthly_change)
# #     max_decrease=min(monthly_change)
# #     max_increase_month=monthly_change.index(max_increase)+1
# #     max_decrease_month=monthly_change.index(max_decrease)+1
# # # Print the results    
# # print("Financial Analysis")
# # print("--------------------------")
# # print (f"Total Months:{len(months)}")
# # print (f"Total: $ {net_total}")
# # print (f"Average  Change: ${round(sum(monthly_change)/(len(profit_Losses)-1),2)}")
# # print(f"Greatest Increase in Profits: {months [max_increase_month]}(${max_increase})")
# # print(f"Greatest Decrease in Profits: {months [max_decrease_month]}(${max_decrease})")

