import os
import csv

# set file path
csvpath = os.path.join("C:/Users/Abbi/Desktop/budget_data.csv")

#declare variables
total_months = []
total_profits = []
profit_changes = 0
monthly_changes = []
previous_value = 0

#open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header
    csv_reader= next(csvreader)

    for row in csvreader:

        #total of months and profit/losses
        total_months.append(row[0])
        total_profits.append(row[1])

    print(len(total_months))

    total_profits=[int(x) for x in total_profits] 
    total_profits_sum=sum(total_profits) 
print (total_profits_sum) 

for i in range(len(total_profits)-1):
    monthly_changes.append(total_profits[i+1]-total_profits[i])
