import os
import csv

# set file path
csvpath = os.path.join("C:/Users/Abbi/Desktop/budget_data.csv")

#declare variables
total_months = []
total_profits = []
profit_changes = []
monthly_changes = []
previous_value = 0

#open csv file
with open(csvpath) as file:
    reader = csv.reader(file)
    #skip header
    next(reader)

    for row in reader:

        #total of months and profit/losses
        total_months.append(row[0])
        total_profits.append(int(row[1]))


    #net total of profits/losses over entire time
    total_profits=[int(x) for x in total_profits] 
    total_profits_sum = sum(total_profits) 

#changes in profits/losses over time
for i in range(len(total_profits) - 1):
    profit_changes.append(total_profits[i+1] - total_profits[i])

#calculate avg change
average_change = sum(profit_changes) / len(profit_changes)

#find greastest increase and decrease
greatest_increase = max(profit_changes)
greatest_increase_month = total_months[profit_changes.index(greatest_increase) + 1]
greatest_decrease = min(profit_changes)
greatest_decrease_month = total_months[profit_changes.index(greatest_decrease) + 1]

#print results
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total Profit/Losses: ${total_profits_sum}")
print(f"Average Change: ${average_change: .2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")


