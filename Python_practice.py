print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
if counties[2] != 'Jefferson':
    print(counties[2])
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties")
else:
    print("Arapahoe and El Paso are not in the list of counties")
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is the list of counties and El Paso is not in the list of counites")

# "for" loop itereate through lists and tuples    

for county in counties:
    print(county)

# "for" loop using range function 3.2.10

for i in range(len(counties)):
    print(counties[i])

counties_tuple = ("Arapahoe", "Denver", "Jefferson")

# 2 ways of getting outputs for Tuples

for i in range(len(counties_tuple)):
    print(counties_tuple[i])

for county in counties_tuple:
    print(county)
    
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# usinf "for" loops with dicts first 2 "keys" "arapahoe" next 2 "values" "#######"
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)

#value loops with for

for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])

# "key value pairs of a dict" "for" 'key', 'value' in dict_name.items():
    #print(key, value)

for county, voters in counties_dict.items():
    print(county, voters)

#skill drill print each county and registered voters from counties_dict using concatenation

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

#iterate thru a list of Dicts

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)

#iterate thru lists of dicts using range function

for i in range(len(voting_data)):
    print(voting_data[i])

#get the values from a list of dicts "nested" loops

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#retrieve the # of registered voters, same if you want name replace ["voters"] with ["county"]

for county_dict in voting_data:
    print(county_dict["registered_voters"])

#using f strings with dicts condensed from above using concatenation f" {}

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


#f-string literals printing formats 3.2.8 & 3.2.11
# How many votes did you get?
#my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
#total_votes = int(input("What is the total votes in the election? "))

# Calculate the percentage of votes you received.

#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")

#now becomes with f string from above 2 lines

#print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#Multiline F-strings following replaces entire code from #f-string down

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

#formatting floating-point deciamals f'{value:{width}.{precision}}}' precision is :.2f above in blue

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(f'{county} county has {voters:,} registered voters')

#formatting with lists of dicts???

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

#Dependencies Packages and Mods

#Import the datetime class from the datetime module

import datetime as dt

#Use the now() attribute on the datetime class to get the present time.

now = dt.datetime.now()

#print the preset time

print("the time right now is", now)
