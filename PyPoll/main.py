import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read each row of data after the header
    # for row in csv_reader:
        # print(row)

    # Add text 'Election Results'
    # Add '------' break
    # Create total number of votes cast
    # Add '------' break
    # Create a complete list of candidates who received votes
    # Find the the percentage of votes each candidate won
    # Find the total number of votes each candidate won
    # Add '------' break
    # Find the winner of the election based on popular vote
    # Add '------' break
    # Summarise and print 'Election Results'
    # Export a text file with the results  
        