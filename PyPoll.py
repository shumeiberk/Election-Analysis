# # Import the datetime class from the datetime module.
# import datetime
# # Use the now() attribute on the datetime class to get the present time.
# now = datetime.datetime.now()
# # Print the present time.
# print("The time right now is ", now)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_load) as election_data:

    # Print the file object
    print(election_data)

with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------" + "\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

txt_file.close()


# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize a total vote counter
total_votes = 0

# candidate options
candidate_options = []
candidate_votes = {}

with open(file_to_load) as election_data:

    # to do: read and analyze the data here
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    #print(headers)

    for row in file_reader:
        # adds total vote count
        total_votes += 1

        # candidate name for each row
        candidate_name = row[2]

        # if candidate does not match any existing candidates
        if candidate_name not in candidate_options:

            # add candidate name to the candidate list
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1


print(total_votes)
print(candidate_options)
print(candidate_votes)

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate]
    # 3. Calculate the percentage of votes.
    vote_percentage = int(votes) / int(total_votes) * 100

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate

    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate}: received {vote_percentage: .1f}% of the vote.")

    winning_candidate_summary = (
        f"----------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------\n"
    )
    print(winning_candidate_summary)