

 ###### Objectives ######

# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

###### Output ######

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)


# Import Packages
import os
import csv
# Set Path
csv_path = os.path.join("Resources","budget_data.csv")
#input_file = "Resources/budget_data.csv"

#Define List
date_list = []
profit_losses_list = []
changes_list = []

#Define Variables:
number_of_months = 0
#net_profits_losses =0

#average=0
#greatest_increase=0
#greatest_decrease=0
previous_months_pl=0

# Open the csv file for reading
with open(csv_path,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

#Loop through all the rows of the file
    for row in csvreader:
        number_of_months +=1
        date_list.append(row[0])
        profit_losses_list.append(int(row[1]))
        current_months_pl = int(row[1])
        if previous_months_pl == 0:
            change = 0
        else:
            change = current_months_pl - previous_months_pl
            changes_list.append(change)
    
        previous_months_pl = current_months_pl

#Find the changes in Profit/Losses and put in changes list  
        #changeslist.append(change)

#Find the Net Total
    net_total= sum(profit_losses_list) 

# Average = sum(changes list/len of changes list) 
    average = round(sum(changes_list)/(len(changes_list)), 2)

# Greatest increase in profits = max value of changes list
    greatest_increase = max(changes_list)

# Date of Greatest increase = index of max value in changes list
    max_index = changes_list.index(greatest_increase)
    greatest_incr_date = date_list[max_index + 1]

# Greatest decrease in losses = min value of changes list
    greatest_decrease = min(changes_list)

# Date of Greatest decrease = index of min value in changes list
    min_index = changes_list.index(greatest_decrease)   
    greatest_decr_date = date_list[min_index + 1]

# Print Analysis    
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(number_of_months))
    print("Total: $" + str(net_total))
    print("Average Change: $" + str(average))
    print("Greatest Increase in Profits: " + str(greatest_incr_date) +" "+ "(" + "$"+str(greatest_increase)+")")
    print("Greatest Decrease in Profits: " + str(greatest_decr_date) +" "+ "("+"$"+str(greatest_decrease)+")")

# Open text file(analysis.txt) for writing
    f = open("analysis.txt", "w")
# Write data to text file
    f.write("\n"+"Financial Analysis")
    f.write("\n"+"----------------------------")
    f.write("\n"+"Total Months: " + str(number_of_months))
    f.write("\n"+"Total: $" + str(net_total))
    f.write("\n"+"Average Change: $" + str(average))
    f.write("\n"+"Greatest Increase in Profits: " + str(greatest_incr_date) +" "+"(" + "$"+str(greatest_increase)+")")
    f.write("\n"+"Greatest Decrease in Profits: " + str(greatest_decr_date) +" "+"("+"$"+str(greatest_decrease)+")")
# Close text file
    f.close()