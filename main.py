import math

shot_distances = []

def distance(x1, y1, x2, y2: int):
    dist: float = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

# def process_file(filename):
#     open_file = open(filename, "r")
#     for line in open_file:


#process_file('/home/popeye/Repositories/GitHub/distances/175_groups.csv')

# create list with pairs of shots
shots = [[-1,4],[-2,2],[-1,2],[1,2],[3,3]]
pairs = list(zip(shots, shots[1:] + shots[:1]))

# calculate distances between the shots
for i in pairs:
    shot = distance(i[0][0], i[0][1], i[1][0], i[1][1])
    shot_distances.append(shot)

print(shot_distances)
