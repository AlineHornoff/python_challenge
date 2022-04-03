import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    csv_header = next(csv_file)

    # Create total number of votes cast
    TotalVotes = sum(1 for row in csv_file)

    # Summarise and print 'Election Results'
    print("Election Results")
    print("----------------------")
    # Print total votes
    print(f"Total Votes: {TotalVotes}")
    print("----------------------")

    # reset csvreader
    csv_file.seek(0)
    next(csv_reader)


    # Total Vote Counter
    total_votes = 0

    # Candidate Options and Vote Counters
    candidate_options = []
    candidate_votes = {}

    # Winning Candidate and Winning Count Tracker
    winning_candidate = ""
    winning_count = 0

        # For each row...
    for row in csv_reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        # (In a way, our loop is "discovering" candidates as it goes)
        if candidate_name not in candidate_options:

            # Add it to the list of candidates in the running
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        # Then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

    # Get candidate votes
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        
        # get vote percentage
        vote_percentage = float(votes) / float(total_votes) * 100

        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
    
        # Summarise and print 'Election Results'
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")

    # Summarise and print 'Election Results'
    print("-----------------------------")
    print(f"winner: {winning_candidate}")
    print("-----------------------------")
    
    #------------------------------------
    # Export a text file with the results 
    #------------------------------------

    # create text file
    #file = open("ElectionResults","w")

    # Write in text file
    #file.write("Election Results\n")
    #file.write("----------------------\n")
    #file.write(f"Total Votes: {month_count}\n")
    #file.write("----------------------\n")
    # List of candiates and percentage of votes for each candidate
    #file.write("----------------------\n")
    #The Winner
    #file.write(f"Average Change: ${round(sum(AverageChange)/len(AverageChange),2)}\n")
    #file.write("----------------------\n")

    # Close text file
    #file.close