# Data we need to retieve
# The total number of votes cast
# List of candidates who received votes
# % of votes each candidate won
# Winner of election

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("../module work/resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    
    rowcount = 0
    for row in file_reader:
        rowcount += 1
        
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {rowcount:,}\n"
        f"-------------------------\n")

    
    txt_file.write(election_results)        
    

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]

        vote_perc = float(votes) / float(rowcount) * 100

        if (votes > winning_count) and (vote_perc > winning_percentage):
            winning_count = votes
            winning_percentage = vote_perc
            winning_candidate = candidate_name
        candidate_results = (f"{candidate_name}: {vote_perc:.1f}% ({votes:,})\n")
        txt_file.write(candidate_results)


    
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    txt_file.write(winning_candidate_summary)


