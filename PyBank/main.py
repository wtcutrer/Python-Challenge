#Import modules
import os
import csv

#Create lists
months = []
profit_loss = []

#Set path 
budget_csv = os.path.join('budget_data.csv')

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
        profit_loss.append(float(row[1]))

#Calculate total months 
total_months = (len(months))

#Calculate the net amount
net_amount = sum(profit_loss)

#Calculate the average change
avg_change = net_amount / total_months

#Calculate the greatest increase
max_profit = max(profit_loss)

#Using the index of the greatest increase
index_max = profit_loss.index(max_profit)
max_month = months[index_max]

#Calculate the greatest decrease
min_profit = min(profit_loss)

#Find Date
index_min = profit_loss.index(min_profit)
min_month = months[index_min]

financial_analysis = (f'''Financial Analysis
----------------------------------
Total Months: {total_months}
Total: ${net_amount:.2f}
Average Change: {avg_change:.2f}
Greatest Increase in Profits: {max_month} {max_profit:.2f}
Greatest Decrease in Profits: {min_month} {min_profit:.2f}''')

#Print out analysis
print(financial_analysis)

#Create a .txt file containing the same analysis in the print out
analysis = open('financial_analysis.txt', 'w')

analysis.write(financial_analysis)

analysis.close()

