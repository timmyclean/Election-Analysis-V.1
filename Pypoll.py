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
# Open the election results and read the file.
with open(file_to_load) as election_data:

#to do: read and analyze the data here
# read the file object with reader function.

    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)
    print(headers)

    #
# Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
    
        
            

   
   
    # Print the file object.
#print(election_data)




# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

#replaced with below to clean up
with open(file_to_save,'w') as txt_file:

# Using the with statement open the file as a text file.
#outfile = open(file_to_save, "w")replaced by below

    txt_file.write("Counties in the Election\n----------------------------")
    
    # Write couties to the file.
    txt_file.write("\nArapahoe\nDenver\nJefferson")

# Close the file
#outfile.close()



