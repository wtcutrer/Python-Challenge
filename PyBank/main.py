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

        #Add Shift in Proftit/Loss
        margin_shift.append(float(row[1]))

#Calculate the net amount
net_amount = sum(margin_shift)

#Calculate the greatest increase
greatest_profit = max(margin_shift)
index_max = margin_shift.index(greatest_profit)
best_month = months[index_max]

#Calculate the greatest decrease
least_profit = min(margin_shift)
index_min = margin_shift.index(least_profit)
worst_month = months[index_min]

#Calculate total months 
total_months = (len(months))

#Calculate the average change
avg_change = net_amount / total_months

budget_analysis = (f'''Financial Analysis
----------------------------------
Total Months: {total_months}
Total: ${net_amount:.2f}
Average Change: {avg_change:.2f}
Greatest Increase in Profits: {best_month} {greatest_profit:.2f}
Greatest Decrease in Profits: {worst_month} {least_profit:.2f}''')

#Print out analysis
print(budget_analysis)
analysis = open('Budget Analysis.txt', 'w')
analysis.write(budget_analysis)
analysis.close()
