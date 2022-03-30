import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read each row of data after the header
    for row in csv_reader:
        print(row)

    # Add text 'Financial Analysis'
    # Add '------' break
    # Create total number of month included in the data set
    # Create net total amount of "Profit/Losses" over the entire period
    # Find the greatest increase in profts (date and amount) over the entire period
    # Find the greatest decrease in loses (date and amount) over the entire period
    # Summarise and print 'Financial Analysis'
    # Export a text file with the results    

    
