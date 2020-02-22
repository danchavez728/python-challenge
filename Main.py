# import os module
import os
# import cs reader 
import csv

# set file path 
filepath = "04-Pandas/Instructions/PyBank/Resources/budget_data.csv"

# set month value
monthsAmount = 0 
# set month changed
monthChanged = []
# set value for previous amount
lastAmount =0 
# set change value 
change = 0 
# set total value 
total = 0 
# set greatest loss 
greatestLosses = ["", 999999999] 
# set greatest profit
greatestProfit = ["", 0]
# set revenue av
revenueAv = []

# open csv file with csv reader 
with open(filepath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # start loop formulas 
    for row in reader:
        monthsAmount = monthsAmount + 1
        total = total + int(row["Total"])

        # calculate greatest loss 
    if (change < greatestLosses[1]):
        greatestLosses[1] = change
        greatestLosses[0] = row["Month"]
    
        
     #calculate geratestProfit
    if (change > greatestProfit[1]):
        greatestProfit[0] = row["Month"]
        greatestProfit[1] = change
    
    # calculate months and totals 
    change = int(row["Total"]) -lastAmount
    lastAmount = int(row["Total"])
    monthChanged = monthChanged +[row["Month"]]
    # calculate average 
    revenueAv = sum(change) / len(change)

    # print text to sheet
        print(f"Budget Data Analysis'+'\n")
        print(f"**************************'+'\n")
        print(f"Total Months : {monthChanged}")
        print(f"total: $ {total}")
        print(f"Greatest Loss: (${greatestLosses}")
        print(f"Greatest Profit: (${greatestProfit}")

