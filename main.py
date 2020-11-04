import os, csv, math
from itertools import combinations

# Variables
list1 = []

# Path to collect data from the current folder
shooting_data_csv = os.path.join('175_groups.csv')

# Functions



# Read in the CSV file
with open(shooting_data_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=';')

    # Remove header
    csv_header = next(csvreader)

    # Convert csv to a list
    my_list = list(csvreader)


for i_list in my_list:
    print(i_list)
    for comb in combinations(i_list,2):
        #print(math.dist(comb[0],comb[1]))
        print((comb[0]))


#        .338LMCh1s'sF4v0ritC4l!
