import os
import csv

#source to read revenue data file
outputFile = os.path.join("Budget Analysis.txt")
budgetpath = os.path.join('.', 'Resources', 'budget_data.csv')

print("Financial Analysis")
print("--------------------------")

# variables
totalMonths = 0
netTotal = 0
monthlyChange = [] # lists of average changes
months = [] #initialize list of months

# read the csv file
with open(budgetpath) as budget_data:
    csvreader = csv.reader(budget_data)
    
    # read the header row
    header = next(csvreader)
    # move to the first row
    firstRow = next(csvreader)

    
    # increment the count of the total months
    totalMonths += 1
    
    netTotal += float(firstRow[1])
    
    # for avgChange find previous net
    prevAmt = float(firstRow[1])
            
    for row in csvreader:
        totalMonths += 1
        netTotal += float(row[1])
        
        # calculate net change inside of loop
        netChange = float(row[1]) - prevAmt
        # add to the list of monthly changes
        monthlyChange.append(netChange)
        
        # add first month change occurred
        months.append(row[0]) # do this because month is in index 0
        
        prevAmt = float(row[1])
        
# calculate average net change
averageChangePerMonth = sum(monthlyChange) / len(monthlyChange)

# variables
greatIncrease = ["months[0]", monthlyChange[0]] 
greatDecrease = ["months[0]", monthlyChange[0]]

# use this loop to calculate the index of the greatest and least montly change
for m in range(len(monthlyChange)):
    # calculate the greatest increase and decrease
    if(monthlyChange[m] > greatIncrease[1]):
        # if the value is greater than the greatest increase, that value becomes the new greatest increase
        greatIncrease[1] = monthlyChange[m]
        # update the month
        greatIncrease[0] = months[m]   

    if(monthlyChange[m] < greatDecrease[1]):
        greatDecrease[1] = monthlyChange[m]
        greatDecrease[0] = months[m]
                      
# output
output = (
    f"Total Months: {totalMonths} \n"
    f"Total: ${netTotal:,.2f} \n"
    f"Average Change: ${averageChangePerMonth:,.2f} \n"
    f"Greatest Increase in Profits: {greatIncrease[0]} Amount ${greatIncrease[1]:,.2f} \n"
    f"Greatest Decrease in Profits: {greatDecrease[0]} Amount ${greatDecrease[1]:,.2f}"
    )
    
print(output)

#export output variable to text file
with open(outputFile, "w") as textFile:
    textFile.write(output)

