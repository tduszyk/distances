import os, csv, math
from itertools import combinations

# Variables
list1 = []

# Path to collect data from the current folder
shooting_data_csv = os.path.join('175_groups.csv')

# Functions
def distance(x1,y1,x2,y2):
    dist = ((x1-x2)**2 + (y1-y2)**2)**.5
    return dist


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
        print(comb)
        print(type(comb))



#        .338LMCh1s'sF4v0ritC4l!
