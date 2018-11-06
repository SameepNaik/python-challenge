# Import modules
import os
import csv
from collections import Counter
# Read csv file
csvpath = os.path.join("election_data.csv")

# Lists
voter_id =[]
county = []
candidate = []

# Open csv
with open(csvpath, newline="") as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")

    # Skip header
    csv_header = next(csvfile)
    for row in election_data:
        
        # Fill lists with columns
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# Calculate total number of votes
total_vote_cast = len(voter_id)

# Count candidate list to determine number of votes
khan_count = candidate.count("Khan")
correy_count = candidate.count("Correy")
li_count = candidate.count("Li")
otooley_count = candidate.count("O'Tooley")

# Calculate percentage of votes
khan_percent = (khan_count/total_vote_cast)*100
correy_percent = (correy_count/total_vote_cast)*100
li_percent = (li_count/total_vote_cast)*100
otooley_percent = (otooley_count/total_vote_cast)*100

# Call Counter to tabulate results and ranking
results = Counter(candidate)

# Output
print(" ")
print(" ")
print("Election Results")
print(" ")
print("--------------------------")
print("Total Votes: " +str(total_vote_cast))
print("--------------------------")
print("Khan: " +("%.3f" % khan_percent)+ "%  (" +str(khan_count)+")")
print("Correy: " +("%.3f" % correy_percent)+ "%  (" +str(correy_count)+")")
print("Li: "+("%.3f" % li_percent)+ "%  (" +str(li_count)+")")
print("O'Tooley: "+("%.3f" % otooley_percent)+ "%  (" +str(otooley_count)+")")
print("--------------------------")
print("Winner: " +str(results.most_common(1)))
print("--------------------------")

# Text file to write to
output_path = os.path.join("pypoll_new.txt")

# Open the file 
with open('pypoll_new.txt', 'w') as f:
    line1 = "Election Results"
    line2 = " "
    line3 = "--------------------------"
    line4 = "Total Votes: " +str(total_vote_cast)
    line5 = "--------------------------"
    line6 = "Khan: " +("%.3f" % khan_percent)+ "%  (" +str(khan_count)+")"
    line7 = "Correy: " +("%.3f" % correy_percent)+ "%  (" +str(correy_count)+")"
    line8 = "Li: "+("%.3f" % li_percent)+ "%  (" +str(li_count)+")"
    line9 = "O'Tooley: "+("%.3f" % otooley_percent)+ "%  (" +str(otooley_count)+")"
    line10 = "--------------------------"
    line11 = "Winner: " +str(results.most_common(1))
    line12 = "--------------------------"
    f.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,\
    line3,line4,line5,line6,line7,line8,line9,line10,line11,line12))



