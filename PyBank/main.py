#Import modules
import os
import csv

#Create lists
months = []
margin_shift = []

#Set path 
budget_csv = os.path.join('Resources','budget_data.csv')

#Open CSV
with open(budget_csv, newline="") as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=",")

    #Skip the header
    next(budget_reader)

    #Loop CSV file
    for row in budget_reader:

        #Add date
        months.append(row[0])

        #Add Profit/Loss
        margin_shift.append(float(row[1]))

#Calculate total months 
total_months = (len(months))

#Calculate the net amount
net_amount = sum(margin_shift)

#Calculate the average change
avg_change = net_amount / total_months

#Calculate the greatest increase
greatest_profit = max(margin_shift)

#Using the index of the greatest increase
index_max = margin_shift.index(greatest_profit)
best_month = months[index_max]

#Calculate the greatest decrease
least_profit = min(margin_shift)

#Find Date
index_min = margin_shift.index(least_profit)
worst_month = months[index_min]

budget_analysis = (f'''Financial Analysis
----------------------------------
Total Months: {total_months}
Total: ${net_amount:.2f}
Average Change: {avg_change:.2f}
Greatest Increase in Profits: {best_month} {greatest_profit:.2f}
Greatest Decrease in Profits: {worst_month} {least_profit:.2f}''')

#Print out analysis
print(budget_analysis)

#Create a .txt file containing the same analysis in the print out
analysis = open('Budget Analysis.txt', 'w')

analysis.write(budget_analysis)

analysis.close()

