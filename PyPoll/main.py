#PyPoll's Main file

#dependencies for os operations and working with csv files which we'll be doing
import os
import csv

totalVotes = 0 #variable to track total number of votes
votes = { "Khan" : 0, #dictionary to keep track of each candidates' votes
          "Correy" : 0,
          "Li" : 0,
          "O'Tooley" : 0}

csvpath = os.path.join('Resources', 'election_data.csv')
#read in the file using csv methods we imported and the csvpath variable we created with os
with open(csvpath, newline='') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) #read the header row first to not count it as the contents
    for row in csvreader: #iterate through everything else
        if row[0] in (None, ""): #Make sure the program doesn't try to read past the end of the file and mess up
            break #exit out of the for loop
        votes[row[2]] += 1
        totalVotes += 1
        
def printing(text): #method to print to console at the same time as writing to file
    print(text)
    f.write(text + "\n")
    
with open('voting results.txt', 'w') as f: #printing the voting results
    printing("Election Results \n----------------------------")
    printing("Total Votes: " + str(totalVotes))
    printing("----------------------------")
    #the percentage of votes each candidate receives is calculated and formatted in the printing statement
    #instead of being calculated before and stored in a variable
    printing("Khan: " + str("{0:.0f}%".format(votes["Khan"]/totalVotes * 100)) + " (" + str(votes["Khan"]) + ")")#the percentage and number of votes received by each candidate
    printing("Correy: " + str("{0:.0f}%".format(votes["Correy"]/totalVotes * 100)) + " (" + str(votes["Correy"]) + ")")
    printing("Li: " + str("{0:.0f}%".format(votes["Li"]/totalVotes * 100)) + " (" + str(votes["Li"]) + ")")
    printing("O'Tooley: " + str("{0:.0f}%".format(votes["O'Tooley"]/totalVotes * 100)) + " (" + str(votes["O'Tooley"]) + ")")
    printing("----------------------------\nWinner: "+ str(max(votes, key=votes.get)) +"\n----------------------------")  