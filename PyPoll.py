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

with open(file_to_load) as election_data:

    # to do: read and analyze the data here
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

    #for row in file_reader:
    #    print(row)