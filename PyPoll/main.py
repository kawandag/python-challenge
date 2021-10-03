import os
import csv

# path to the source file
electionpath = os.path.join('.', 'Resources', 'election_data.csv')

outputFile = os.path.join("Election Analysis.txt")


# variables

totalVotes = 0
candidates= [] # list of candidates
votesWon= {} # dictionary that will hold the total number of votes
winCount= 0 # to hold winning count
winner= "" # hold the winner
voterOutput= ""

# read the csv file
with open(electionpath) as election_data:
    csvreader = csv.reader(election_data, delimiter=',')
    
    #read header row
    header = next(csvreader)
    #move to first row
    firstRow = next(csvreader)
    
    # rows will be in lists
    #index 0 is voter id
    #index 1 is county
    #index 2 is candidate
    
    # count total number of votes
    totalVotes += 1
    
    
    for row in csvreader:
        totalVotes += 1
         # list of candidates
        if row[2] not in candidates:
            candidates.append(row[2])
            
            # add value to dictionary
            # {"key": value }
            # start the count at 1 for the votes
            votesWon[row[2]] = 1
            
        else: 
            # add a vote to count if candidate is already in list
            votesWon[row[2]] += 1



        
for candidates in votesWon:
    # get the votes won and percentage
    votes = votesWon.get(candidates)
    votePct = (float(votes) / float(totalVotes)) * 100.00
    voterOutput += f"{candidates}: {votePct:.2f}% ({votes})\n"
    
    


       

    #compare voes to the winning count
    if votes > winCount:
        winCount = votes
        winner= candidates
winOutput = f"Winner: {winner}"
        

# output
output = (
    f"Election Results\n"
    f"------------------------------\n"
    f"Total Votes: {totalVotes} \n"
    f"------------------------------\n"
    f"{voterOutput} \n"
    f"------------------------------\n"
    f"{winOutput}"
    
)
print(output)
with open(outputFile, "w") as textFile:
    textFile.write(output)

