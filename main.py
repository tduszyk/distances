import pandas as pd
import math

shot_distances = []

# function to calculate a distance between two shots
def distance(x1, y1, x2, y2: int):
    dist: float = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

# create list with pairs of shots
#shots = [[-1,4],[-2,2],[-1,2],[1,2],[3,3]]
#pairs = list(zip(shots, shots[1:] + shots[:1]))

# function to open and process the csv file
# def process_file(filename):
#      open_file = open(filename, "r")
#      for row in open_file:
#           shots = row.split(";")
#           print(shots)
file_to_load = ('/home/popeye/Repositories/GitHub/distances/175_groups.csv')
shooting_data = pd.read_csv(file_to_load, delimiter=';', index_col=None, header=None)
print(shooting_data.head())



# main program
# for i in pairs:
#     shot = distance(i[0][0], i[0][1], i[1][0], i[1][1])
#     shot_distances.append(shot)
#
# print(shot_distances)
