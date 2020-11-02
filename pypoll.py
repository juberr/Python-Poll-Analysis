# Data we need to retieve
# The total number of votes cast
# List of candidates who received votes
# % of votes each candidate won
# Winner of election

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Desktop","UofT Bootcamp","Module 3 - Python","resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    
    rowcount = 0
    for row in file_reader:
        rowcount +=1
        print(row)
    print(rowcount)