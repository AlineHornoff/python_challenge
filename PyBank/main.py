import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

def budget_data(month_data):
    date = str(month_data[0])
    profit = int(month_data[1])

# Open and read csv
with open(budget_data_csv, 'r') as csv_file:


    # Read the header and skip the header
    csvreader = csv.reader(csv_file, delimiter=',')
    csv_reader = next(csvreader)

    # Add text 'Financial Analysis'
    print("Financial Analysis")

    # Add '------' break
    print("----------------------")

    # Create total number of month included in the data set
    month_count = sum(1 for lin in csv_file)
    print(f"Total Months: {month_count}")

    # Create net total amount of "Profit/Losses" over the entire period
    NetProfitLoss = sum(int(NetProfitLoss[1]))
    print(f"Total: {NetProfitLoss}")

    # Find the greatest increase in profts (date and amount) over the entire period
    # Find the average of the change in "Profit/Losses" the entire period
    # Find the greatest decrease in loses (date and amount) over the entire period
    # Summarise and print 'Financial Analysis'
    # Export a text file with the results    

    
