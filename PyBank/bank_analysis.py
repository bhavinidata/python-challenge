#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import csv

# List to store data
date = []
profit_losses = []
monthlychange = {"dates": [],
                 "change": []}

# set the path for source file to read
csv_path = os.path.join("Resources", "budget_data.csv")

# Open file and read with csvreader. store data in list
with open (csv_path, "r") as bankanalysisfile:
    csv_reader = csv.reader(bankanalysisfile, delimiter=",")
    csvheader = next(bankanalysisfile)
    
    for row in csv_reader:
        date.append(row[0])
        profit_losses.append(int(row[1]))
        last_index = len(profit_losses) - 1
#       if there are more than one elements in profit_losses list then find the difference between the two.
#       and store the date as key and differences as value in new dictionary "monthly_change".
        if last_index > 0:
            change_in_profit_losses = profit_losses[last_index] - profit_losses[last_index-1]
            monthlychange["dates"].append(row[0])
            monthlychange["change"].append(change_in_profit_losses)

print(f"Financial Analysis")
print(f"---------------------------")

# Find the total months
total_month = len(date)
print(f"Total Months: {total_month}")

# Find net proft/Losses
net_profit_losses = sum(profit_losses)
print(f"Total: ${net_profit_losses}")

# Find the average of monthly changes in profit losses.
avg_of_changes = sum(monthlychange["change"])/(len(monthlychange["change"]))
print(f"Average change: {round(avg_of_changes,2)}")

max_profit = max(monthlychange["change"])
max_loss = min(monthlychange["change"])
max_profit_month = monthlychange["dates"][monthlychange["change"].index(max_profit)]
print(f"Greatest Increase in Profits: {max_profit_month}, (${max_profit})")
max_loss_month = monthlychange["dates"][monthlychange["change"].index(max_loss)]
print(f"Greatest Decrease in Profits: {max_loss_month}, (${max_loss})")

# set the output file path.
output_file = os.path.join("financial_analysis.txt")
# Print output to the terminal as well as in text file
with open (output_file, "w") as datafile:
    print(f"Financial Analysis", file = datafile)
    print(f"---------------------------", file = datafile)
    print(f"Total Months: {total_month}", file = datafile)
    print(f"Total: ${net_profit_losses}", file = datafile)
    print(f"Average change: {round(avg_of_changes,2)}", file = datafile)
    print(f"Greatest Increase in Profits: {max_profit_month}, (${max_profit})", file = datafile)
    print(f"Greatest Decrease in Profits: {max_loss_month}, (${max_loss})", file = datafile)


# In[ ]:




