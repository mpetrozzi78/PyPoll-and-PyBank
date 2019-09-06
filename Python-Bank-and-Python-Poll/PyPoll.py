# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
# Module to do the sorting
import operator

#csvpath = os.path.join('..', 'Resources', 'election_data.csv')
election_file = open('election_data.csv', "r")

# Splt the data on commas                
csv1 = csv.reader(election_file, delimiter=',')

# Skip the Header
header = next(csv1)

# Setting Variables
sum_votes = 0

# Dictionary of results
results = {}

# Calculations for each row
for row in csv1:
    
# Calculating total votes of all candidates    
    sum_votes = sum_votes + 1
    
# assigning values to the results dictionary

# If the candidate on the csv file is already present in our dictionary
    if row[2] in results.keys(): 
# if "key_name" in dic_name.keys():
		
# Add the counter value of the corresponding key
        results[row[2]] += 1

# If the candidate is not present in our dictionary
    else:
		
        results[row[2]] = 1
	
# Sorting the dictionary after gone through all the calculations for each row of the csv file
sorted_results = sorted(results.items(), key=operator.itemgetter(1), reverse=True)

#Printing the results
print("'''''''''''''''''''''''''''''''''")
print("ELECTION RESULTS")
print("--------------------------------")
print("Total Votes:  " + str(sum_votes))
print("--------------------------------")
#print (sorted_results)

for k, v in sorted_results:
    val=str(v)
    percent=round((float(val)/float(sum_votes))*100)
    print(k + ": "  +  str(percent) + '%' + ' ('+ str(v) + ')')

print("--------------------------------")
# Print the greatest number with candidate
maximum = max(results, key=results.get) 
print("Winner: " + maximum)
print("--------------------------------")
#print(maximum, results[maximum])

#Export a Text file with the results
    
import sys
file = open('Election_Results_Output.txt', 'a')
sys.stdout = file

print("'''''''''''''''''''''''''''''''''")
print("ELECTION RESULTS")
print("--------------------------------")
print("Total Votes:  " + str(sum_votes))
print("--------------------------------")
#print (sorted_results)


for k, v in sorted_results:
    val=str(v)
    percent=round((float(val)/float(sum_votes))*100)
    print(k + ": "  +  str(percent) + '%' + ' ('+ str(v) + ')')

print("--------------------------------")
# Print the greatest number with candidate
maximum = max(results, key=results.get) 
print("Winner: " + maximum)
print("--------------------------------")

file.close()