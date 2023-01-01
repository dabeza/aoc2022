import numpy as np 
import matplotlib.pylab as plt
import matplotlib.cm as cm

print("It's Dijkstra time")


#inverting getHeight so that we are moving rom peak to start instead
#i.e., peak has height 0, and start has height 25
def getHeight(arg):
    if arg == "S":
        return getHeight("a")
    elif arg == "E":
        return getHeight("z")
    else:
        return ord('z') - (ord(arg))
    
f = open("input.txt","r")
lines = f.readlines()
f.close()

# print(getHeight('S'))
# exit()

height_map = [[] for i in lines[0].strip()]
row = 0
for line in lines:    
    col = 0
    for char in line.strip():
        if char == "E": #inverted starting position to target for question number 2
            start = [row,col]
        elif char == "S": #inverted starting position to target for question number 2
            targt = [row,col]
        # print(char)
        height_map[col].append(getHeight(char))
        col+=1
    row +=1

# making height_map a numpy array
height_map = np.array(height_map)
#for some reason it is transposed from what I want when generated this way.
height_map = height_map.transpose()

#Initializing variables for Dijkstra
dists = (np.ones(height_map.shape)*height_map.shape[0]*height_map.shape[1])
dists[start[0],start[1]] = 0
unvisited = set()
visited = set()
c = start

        
#Dijkstra algorithm
def add_if_legal(new_c,current_height) -> tuple:
    global visited
    next_height = height_map[new_c[0],new_c[1]]
    
    if ((current_height+1)>=next_height) & (not (tuple(new_c) in visited)):
        # step is legal, add to set
        return tuple(new_c)

def find_neighbours(c) ->set:
    global visited,height_map
    current_height = height_map[c[0],c[1]]
    neighbours = set()
    # check left
    if c[0]>0:
        new_c = [c[0]-1,c[1]]
        neighbours.add(add_if_legal(new_c,current_height))
        
        # step right
    if c[0]<height_map.shape[0]-1:
        new_c = [c[0]+1,c[1]]
        neighbours.add(add_if_legal(new_c,current_height))
            
    # step up
    if c[1]>0:
        new_c = [c[0],c[1]-1]
        neighbours.add(add_if_legal(new_c,current_height))
        
    # step down
    if c[1]< height_map.shape[1]-1:
        new_c = [c[0],c[1]+1]
        neighbours.add(add_if_legal(new_c,current_height))
        
    neighbours -= {None}
    return neighbours

# First visited node
neighbours = find_neighbours(c)
unvisited = unvisited.union(neighbours)
max_dist = height_map.shape[0]*height_map.shape[1]
next_c = neighbours.copy().pop()
# Main Dijkstra loop
while len(unvisited)>0:

    dist = dists[c[0],c[1]]
    while len(neighbours) >0 :
        n = list(neighbours.pop())
        if dists[n[0],n[1]] > dist + 1:
            dists[n[0],n[1]] = dist + 1
    visited.add(tuple(c))
    
    smallest_dist = max_dist
    
    next_set = unvisited.copy()
    while next_set:
        n = list(next_set.pop())
        if dists[n[0],n[1]] < smallest_dist:
            next_c = tuple(n)
            smallest_dist = dists[n[0],n[1]] 
    unvisited.discard(next_c)
    c = list(next_c)
    neighbours = find_neighbours(c)
    unvisited = unvisited.union(neighbours)
    

targt_dist=dists[targt[0],targt[1]]
print("Number of from start are: ", int(targt_dist))

# question two: find the position in dist, whish has height a, in where dist(a) is smallest
# (had to invert the Dijkstra matrix so that it starts at the peak for this to work)
visited_copy = visited.copy()
shortest_scenic = height_map.shape[0]*height_map.shape[1]
a_height = getHeight('a')
while visited : 
    c = list(visited.pop())
    if height_map[c[0],c[1]] == a_height:
        # this is an "a"
        scenic_dist = dists[c[0],c[1]]
        if scenic_dist < shortest_scenic:
            shortest_scenic = scenic_dist
        
print("Number of steps in scenic is: ", int(shortest_scenic))    
