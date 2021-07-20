#Import modules 
import os
import csv

#Set Path for input and output of poll data
voter_csv = os.path.join('Resources','election_data.csv')
file_output = "Vote Analysis.txt"

#Set Variables 
vote_count = {}
vote_per = {}
vote_total = 0

with open(voter_csv, newline="") as csvfile:
    vote_reader = csv.reader(csvfile, delimiter=",")
    next(vote_reader)

    #Loop through CSV
    for row in vote_reader:

        #Count total votes
        vote_total += 1

        #Count votes for each candidate
        if row[2] in vote_count:
            vote_count[row[2]] += 1

         #Add Candidate and set value if needed
        else:
            vote_count[row[2]] = 1

#Variable to set bucket for winner
winner_count = 0

#Loop through vote_count dictionary to calculate the vote percentage and to determine the winner
for candidate in vote_count:
    
    #Calculate and store candidate vote percentage
    vote_per[candidate] = (vote_count[candidate] / vote_total) * 100

    #Determine the winner
    if vote_count[candidate] > winner_count:
        winner_count = vote_count[candidate]
        winner = candidate

#Write text file with results
with open(file_output, 'w', newline="") as txtfile:

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