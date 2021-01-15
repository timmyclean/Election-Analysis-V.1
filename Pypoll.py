
#the data we need, to parse, process using;
#DEPENDENCIES, PACKAGES, AND MODULES
#total number of votes cast
#A complete list of candidates who recieived votes
#Total # of votes each candidate received
#% of votes each candidate won
#the winner based on popular vote

#assign a variable for the file to load and the path 3.4.2
file_to_load = 'Resources/election_results.csv'

#open the election results and read the file
#election_data = open(file_to_load, 'r') changed from this to below(so you dont have to open() close()) each time



import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to save the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#to do: read and analyze the data here
# read the file object with reader function.

# 1. of 3.5.1 Initialize total vote counter
total_votes = 0

# Candidate Options declaring the list before the "with" statement
candidate_options = []
# Declare empty dict for Candidates to determine their total votes
candidate_votes = {}

# Winning Candidate and Winning Count Trakcer
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)
    #print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
     # 2. Add to the total vote count
        total_votes += 1
    
    # 3. Print Total votes
    #print(total_votes)

    # Print the Candidate name for each row 
        candidate_name = row[2]
    # if the candidate does not match any existing candidate..
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # 2. Begin tracking the candidates vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1

# determine % of votes for each candidate by looping thru the counts
# 1. Iterate thru the candidate list
for candidate_name in candidate_votes:
    # 2. retrieve vote count of candidate
    votes = candidate_votes[candidate_name]
    # 3. calculate the % of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # 4. print the candidate name and % votes
    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote")

    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winnning count

# to do: print out each candidate name, vote count, and % ofvotes to the terminal

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. if true then set winning_count = votes and winning_percent = vote &
        winning_count = votes
        winning_percentage = vote_percentage
        # 3 Set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n") 


winning_candidate_summary = (
    f"------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage:{winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)






# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

#replaced with below to clean up
#with open(file_to_save,'w') as txt_file:

# Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")replaced by below

    #txt_file.write("Counties in the Election\n----------------------------")
    
    # Write couties to the file.
    #txt_file.write("\nArapahoe\nDenver\nJefferson")

# Close the file
#outfile.close()



