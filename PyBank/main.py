import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

#def budget_data(month_data):
    #month = str(month_data[0])
    #profit_loss = int(month_data[1])
    #return profit_loss

# Open and read csv
with open(budget_data_csv, 'r') as csv_file:


    # Read the header and skip the header
    csvreader = csv.reader(csv_file)
    csv_reader = next(csvreader)

    # Create total number of month included in the data set
    month_count = sum(1 for row in csv_file)

    # reset csvreader
    csv_file.seek(0)
    next(csvreader)
    
    # Create net total amount of "Profit/Losses" over the entire period
    sum_profit = 0
    sum_loss = 0
    TotalProfitLoss = 0
    Profit = 0
    
    for row in csvreader:
        profit = int(row[1])
        if profit > 0:
            sum_profit = sum_profit + profit
        elif profit < 0:
            sum_loss = sum_loss + profit
    TotalProfitLoss = sum_profit - sum_loss

    # reset csvreader
    csv_file.seek(0)
    next(csvreader)

    # Find the average of the change in "Profit/Losses" for the entire period
    total = []
    
    for row in csvreader:
        total.append(int(row[1]))

    AverageChange = [y-x for x, y in zip(total[:-1], total[1:])]

    # reset csvreader
    csv_file.seek(0)
    next(csvreader)
      
    # Find the greatest increase in loses (date and amount) over the entire period
    #GreatestIncrease = []
    months = []
    GreatestIncrease = []

    for row in csvreader:
        months.append(row[0])
        GreatestIncrease.append(int(row[1]))

    # Look for index number of greatest increase and store in 'MonthsMaxIndex'
    for a, b in enumerate(GreatestIncrease):
        if b == max(GreatestIncrease):
            MonthsMaxIndex = (a)

    # Store the month with the greatest increase in 'GreatestIncreaseMonth'
    for c in [months[MonthsMaxIndex]]:
        GreatestIncreaseMonth = c

     # reset csvreader
    csv_file.seek(0)
    next(csvreader) 

    months = []
    GreatestDecrease = []

    for row in csvreader:
        months.append(row[0])
        GreatestDecrease.append(int(row[1]))

    # Look for index number of greatest decrease and store in 'MonthsMinIndex'
    for d, e in enumerate(GreatestDecrease):
        if e == min(GreatestDecrease):
            MonthsMinIndex = (d)

    # Store the month with the greatest decrease in 'GreatestDecreaseMonth'
    for f in [months[MonthsMinIndex]]:
        GreatestDecreaseMonth = f

    

    # Summarise and print 'Financial Analysis'
        print("Financial Analysis")
        print("----------------------")
        print(f"Total Months: {month_count}")
        print(f"Total: ${TotalProfitLoss}")
        print(f"Average Change: ${round(sum(AverageChange)/len(AverageChange),2)}")
        print(f"Greatest Increase in Profits: {GreatestIncreaseMonth} (${max(GreatestIncrease)})")
        print(f"Greatest Decrease in Profits: {GreatestDecreaseMonth} (${min(GreatestDecrease)})")

    # Export a text file with the results 
       

    
