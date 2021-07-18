#Import modules 
import os
import csv

#Open path
voter_csv = os.path.join('Resources','election_data.csv')

#Create dictionary to store vote count
vote_count = {}

#Create dictionary to store vote percentage
vote_per = {}

#Create a variable to hold the total vote count
vote_total = 0

with open(voter_csv, newline="") as csvfile:
    voterreader = csv.reader(csvfile, delimiter=",")

    #Skip header row
    next(voterreader)

    #Loop
    for row in voterreader:

        #Count total votes
        vote_total += 1

        #Count votes for each candidate
        if row[2] in vote_count:
            vote_count[row[2]] += 1

         #If the candidate does not exist in the dictionary add them and set value as 1
        else:
            vote_count[row[2]] = 1

#Create a variable to hold the winner vote count
winner_count = 0

#Loop through vote_count dictionary to calculate the vote percentage and to determine the winner
for candidate in vote_count:
    
    #Calculate and store candidate vote percentage
    vote_per[candidate] = (vote_count[candidate] / vote_total) * 100

    #Determine the winner
    if vote_count[candidate] > winner_count:
        winner_count = vote_count[candidate]
        winner = candidate

#Print out the results while writing them to a text file
results_path = os.path.join('Election Results.txt')

with open(results_path, 'w', newline="") as txtfile:

    txtfile.write(f'''
Election Results
-------------------------
Total Votes: {vote_total}
-------------------------\n''')

    print(f'''\nElection Results
-------------------------
Total Votes: {vote_total}
-------------------------''')

    for candidate, votes in vote_count.items():
        txtfile.write(f'{candidate}: {vote_per[candidate]:.3f}% ({votes})\n')
        print(f'''{candidate}: {vote_per[candidate]:.3f}% ({votes})''')
    
    txtfile.write(f'''-------------------------
Winner: {winner}
-------------------------''')

    print(f'''-------------------------
Winner: {winner}
-------------------------''')