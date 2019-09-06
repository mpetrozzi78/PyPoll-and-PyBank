# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # Splt the data on commas                
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the Header
    header = next(csvreader)

    # Setting variables
    total_number_months = 0
    total_amount = 0
    last_profit = 0
    total_changes = 0
    average_change = 0
    greatest_increase = -100000
    greatest_decrease = 100000
    greatest_increase_date = ""
    greatest_decrease_date = ""

    #Looping through rows
    for row in csvreader:

        #Counting rows
        total_number_months = total_number_months + 1
        #Counting total amount
        total_amount = total_amount + float(row[1])

        #Counting the changes
        if last_profit != 0:
            last_profit = float(row[1]) - float(last_profit)
            total_changes = total_changes + last_profit

            #Calculating the Greatest Increase
            if last_profit >= greatest_increase:
                greatest_increase = last_profit
                greatest_increase_date = row[0]
  

            #Calculating the Greatest Decrease
            if last_profit <= greatest_decrease:
                greatest_decrease = last_profit
                greatest_decrease_date = row[0]

           

        last_profit = row[1]
    
    # Calculating the average change
    average_change = total_changes / (total_number_months - 1)

    # Print Financial Analysis Results
    print("'''''''''''''''''''''''''''''''''")
    print("FINANCIAL ANALYSIS")
    print("--------------------------------")
    print("Total Months:  " + str(total_number_months))
    print("Total:  $" + str(int(total_amount)))
    print("Average Change:  $" + str(round(average_change, 2)))
    print("Greatest Increase in Profits:  " + greatest_increase_date + "  ($" + str(int(greatest_increase))+ ")")
    print("Greatest Decrease in Profits:  " + greatest_decrease_date + "  ($" + str(int(greatest_decrease))+ ")")


    #Export a Text file with the results
    #
    import sys
    file = open('Financial_Analysis_Output.txt', 'a')
    sys.stdout = file

    print("'''''''''''''''''''''''''''''''''")
    print("FINANCIAL ANALYSIS")
    print("--------------------------------")
    print("Total Months:  " + str(total_number_months))
    print("Total:  $" + str(int(total_amount)))
    print("Average Change:  $" + str(round(average_change, 2)))
    print("Greatest Increase in Profits:  " + greatest_increase_date + "  ($" + str(int(greatest_increase))+ ")")
    print("Greatest Decrease in Profits:  " + greatest_decrease_date + "  ($" + str(int(greatest_decrease))+ ")")

    file.close()



    
   
