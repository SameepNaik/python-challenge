# Import modules
import os
import csv
from collections import Counter

# Set path for file
csvpath = os.path.join("budget_data.csv")

# Set lists
months = []
profit = []
change = []
temp_list = []

# Read CSV file
with open(csvpath, newline="") as csvfile:
    budget_data = csv.reader(csvfile, delimiter=",")

    # Skip header
    csv_header = next(csvfile)

    # Loop through CSV file    
    for row in budget_data:
        months.append(row[0])

        # Fill list with row 1 and convert to integer
        profit.append(int(row[1]))

        # Calculate average profit
        average_profit = sum(profit)/len(profit)
    
 
    # Calculate month to month change
    change = [j-i for i, j in zip(profit[:-1], profit[1:])]

# Output
print(" ")
print(" ")
print("Budget Analysis")
print(" ")
print("--------------------------")
print("Total Months: " +str(len(months)))
print("Total: $" +str(sum(profit)))
print("Average Change: %" +str("%.2f" %(sum(change)/len(change))))
print("Greatest Incrcease in Profits: " "($"+str(max(change))+")")
print("Greatest Decrease in Profits: " "($"+str(min(change))+")")

# Text file to write to
output_path = os.path.join("pybank_new.txt")

# Open the file 
with open('pybank_new.txt', 'w') as f:
    line1 = "Budget Analysis"
    line2 = " "
    line3 = "--------------------------"
    line4 = "Total Months: " +str(len(months))
    line5 = "Total: $" +str(sum(profit))
    line6 = "Average Change: %" +str(sum(change)/len(change))
    line7 = "Greatest Incrcease in Profits: " "($"+str(max(change))+")"
    line8 = "Greatest Decrease in Profits: " "($"+str(min(change))+")"
    f.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7,line8))
