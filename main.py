import os, csv
from scipy.spatial import distance
from itertools import permutations

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

    my_list = list(csvreader)

#print(my_list)

for i in my_list:
    print(i)

