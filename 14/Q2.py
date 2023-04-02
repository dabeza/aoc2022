""" 
start by drawing the rock formation
get all coordinates, make the cave 1 larger depth larger and wider than the largest coordinates
format example
     xx
     xx
     xx
     
yyy  .#
yyy  .#


Cave stored as a matrix
"""
x_source = 500
y_source = 0

import numpy as np
import os
import matplotlib.pyplot as plt
from collections import deque

# print(os.path.dirname(__file__) + "/input.txt")
# f = open(os.path.dirname(__file__) + "/test_input.txt", "r")
f = open(os.path.dirname(__file__) + "/input.txt", "r")
lines = f.readlines()
f.close()

yMin = 0
yMax = -float("inf")

def write_cave(cave,cols):
    return

def line_to_coordinates(line):
    coordinates = deque()
    coords = line.split()
    for coord in coords:
        if coord != "->":
            c_str = coord.split(",")
            c_int = list(map(int, c_str))
            coordinates.append(c_int)
    return coordinates



def get_max_coordinates(coordinates, max_coords) -> list:
    for coord in coordinates :
        if coord[0]<max_coords[0]:
            max_coords[0] = coord[0]
        if coord[0]>max_coords[1]:
            max_coords[1] = coord[0]
        if coord[1]>max_coords[3]:
            max_coords[3] = coord[1] 
    return max_coords


rock_formations = []
inf = float("inf")
max_coords = [inf, -inf, 0, 0]
for x in lines:
    line = x.strip()
    coordinates = line_to_coordinates(line)
    rock_formations.append(coordinates)
    max_coords = get_max_coordinates(coordinates, max_coords)
    # print(coordinates)

# EDIT FOR Q2
max_coords[1] = x_source + max_coords[3]+5
max_coords[0] = x_source - max_coords[3]-5

x_vec = np.arange(max_coords[0]-1,max_coords[1]+2,dtype=int)
y_vec = np.arange(max_coords[2],max_coords[3]+3,dtype=int)
cave = np.zeros((y_vec.size, x_vec.size),dtype=int)
# a = print(x.size)
# print(max_coords)
x0 = max_coords[0]-1
y0 = max_coords[2]
xf = max_coords[1]+1
yf = max_coords[3]+1
print(max_coords)

cave[y_source-y0,x_source-x0] = 1
for rock_formation in rock_formations:
    p1 = rock_formation.popleft()
    for rock in rock_formation :
        p2 = rock
        if p1[0]==p2[0]:
            # add in y
            y = [p1[1]-y0,p2[1]-y0]
            y.sort()
            cave[y[0]:(y[1]+1),p1[0]-x0]=2
        else :
            #add in x
            x = [p1[0]-x0,p2[0]-x0]
            x.sort()
            cave[p1[1]-y0,x[0]:(x[1]+1)] =2
        p1 = p2

# Edit Q2
cave[-1,:] = 2

# sand  = 3
plt.style.use('_mpl-gallery-nogrid')
fig, ax = plt.subplots()


more_sand = True
more_sand = True
sand = 0
while more_sand:
    y = y_source-y0
    x = x_source-x0
    shifty = True
    while shifty:
        if cave[y+1,x] ==4 : #abyss!
            shifty = False
            more_sand = False
        elif cave[y+1,x] == 0:
            y += 1
        elif cave[y+1,x-1] ==0:
            y += 1
            x += -1
        elif cave[y+1,x+1] ==0:
            y += 1
            x += 1
        else: # sand is still, stop being shifty
            cave[y,x] = 3
            sand +=1
            shifty = False
            if y==y_source-y0:
                more_sand = False
    


print("Answer Q2: ", sand)
ax.imshow(cave)
plt.show()