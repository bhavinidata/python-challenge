#!/usr/bin/env python
# coding: utf-8

# In[1]:


def main():
    import os
    import csv

    # set the path for source file to read
    csv_path = os.path.join("Resources", "election_data.csv")

    # List to store data
    voter_id = []
    candidate_list = []
    final_candidate_list = []
    new_dict = {}

    # Open file and read with csvreader. store data in list
    with open (csv_path, "r") as elec_datafile:
        csv_reader = csv.reader(elec_datafile, delimiter=",")
        csvheadr = next(elec_datafile)

        for row in csv_reader:
            voter_id.append(row[0])
            candidate_list.append(row[2])

    # count total number of votes
    total_votes = len(voter_id)

    # Print the results
#     print(f"Election Results")
#     print(f"------------------------")
#     print(f"Total Votes: {total_votes}")

    print(f"""
Election Results
------------------------
Total Votes: {total_votes}
------------------------
""")
    # create a dictionary for each candidate with name as key and total votes as value.
    # check if key is not in the dictionary, add key and one to the value, 
    # otherwise just increase the value to get the total votes for each candidate.
    for name in candidate_list:
        if name in new_dict:
            new_dict[name] += 1
        else:
            new_dict[name] = 1

    # set output file path.
    output_file = os.path.join("elect_Res.txt")
    # Print output to the terminal as well as in text file
    with open (output_file, "w") as datafile:
        print(f"""
Election Results
------------------------
Total Votes: {total_votes}
------------------------
""", file = datafile)
#         print(f"Election Results", file = datafile)
#         print(f"------------------------", file = datafile)
#         print(f"Total Votes: {total_votes}", file = datafile)
#         print(f"------------------------")
        for name in new_dict:
            total_per = format(round((new_dict[name]/total_votes)*100), ".3f")
            print(f"{name}: {total_per}% ({new_dict[name]})")
            print(f"{name}: {total_per}% ({new_dict[name]})", file = datafile)
        winner = max(new_dict, key = new_dict.get)
        print(f"""
------------------------
Winner: {winner}
------------------------
""")
        print(f"""
------------------------
Winner: {winner}
------------------------
""", file = datafile)
        
#         print(f"------------------------")
#         print(f"------------------------", file = datafile)
#         print(f"Winner: {winner}")
#         print(f"Winner: {winner}", file = datafile)
#         print(f"------------------------")
#         print(f"------------------------", file = datafile)
        
if __name__ == "__main__":
    main()






