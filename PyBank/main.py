#PyBank's Main file

#dependencies for os operations and working with csv files which we'll be doing
import os
import csv

total = 0 #variable to store the total profits or losses
months = 0 #variable to count how many months the table holds
averageChange = 0 #variable to keep track of average change
csvpath = os.path.join('Resources', 'budget_data.csv')

#read in the file using csv methods we imported and the csvpath variable we created with os
with open(csvpath, newline='') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) #read the header row first to not count it as the contents
    for row in csvreader: #iterate through everything else
        if row[0] in (None, ""): #Make sure the program doesn't try to read past the end of the file and mess up
            break #exit out of the for loop
        if months == 1: #set maxIncrease and maxDecrease to the second row only once
            maxIncrease = row #'maxIncrease' (and decrease) keeps track of the row the maxIncrease occurs on so we know the month too
            preceedingMaxI = previousRow #keep track of previous row for maxIncrease and maxDecrease too
            maxDecrease = row
            preceedingMaxD = previousRow #'preceedingMaxD (and preceedingMaxI) keep track of the row before the 'maxDecrease' (and increase) rows so we can calculate the actual max increase/decrease
        total += int(row[1])
        if months > 0:
            change = int(row[1]) - int(previousRow[1])
            averageChange += change 
            if change > (int(maxIncrease[1]) - int(preceedingMaxI[1])): #find a new max increase
                maxIncrease = row
                preceedingMaxI = previousRow
            if change < (int(maxDecrease[1]) - int(preceedingMaxD[1])): #find a new max decrease
                maxDecrease = row
                preceedingMaxD = previousRow
        months += 1
        previousRow = row #set the previous row at the end of the loop so we can keep track of the change
    averageChange = round(averageChange / (months - 1),2) #calculate the average change, round to 2 decimal places
    
def printing(text): #method to print to console at the same time as writing to file
    print(text)
    f.write(text + "\n")

with open('financial analysis.txt', 'w') as f: #printing the actual financial analysis
    printing("Financial Analysis \n----------------------------")
    printing("Total Months: " + str(months))
    printing("Total: $" + str(total))
    printing("Average Change: $" + str(averageChange))
    printing("Greatest Increase in Profits: " + maxIncrease[0] + " ($" + str(int(maxIncrease[1]) - int(preceedingMaxI[1])) + ")")
    printing("Greatest Decrease in Profits: " + maxDecrease[0] + " ($" + str(int(maxDecrease[1]) - int(preceedingMaxD[1])) + ")")
