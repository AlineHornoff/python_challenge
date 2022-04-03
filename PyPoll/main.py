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
    #with open("ElectionResults.txt","a") as file:

        # Write in text file
        #file.write("Election Results\n")
        #file.write("----------------------\n")
        #file.write(f"Total Votes: {TotalVotes}\n")
        #file.write("----------------------\n")
        # List of candiates and percentage of votes for each candidate
        #file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
        #file.write("----------------------\n")
        #The Winner
        #file.write(f"winner: {winning_candidate}\n")
        #file.write("----------------------\n")

        # Close text file
        #file.close

    #Save the results to our text file.
    with open("ElectionResults", "w") as txt_file:
        
        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        
        # Save the final vote count to the text file.
        txt_file.write(election_results)
        for candidate_name in candidate_votes:
            
            # Retrieve vote count and percentage
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (
                f"{candidate_name}: {vote_percentage:.3f}% ({votes:,})\n")
            
        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)

        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
           winning_count = votes
           winning_candidate = candidate_name
           winning_percentage = vote_percentage

        # Print the winning candidate's results to the terminal.
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.3f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        
        # Save the winning candidate's results to the text file.
        txt_file.write(winning_candidate_summary)