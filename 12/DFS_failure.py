import numpy as np 

print("It's recursion time")


# Function for converting letter to height
def getHeight(arg):
    if arg == "S":
        return 0
    elif arg == "E":
        return getHeight("z")
    else:
        return ord(arg)-ord('a')



f = open("input.txt","r")
lines = f.readlines()
f.close()

height_map = [[] for i in lines[0].strip()]
row = 0
for line in lines:    
    col = 0
    for char in line.strip():
        if char == "S":
            start = [row,col]
        elif char == "E":
            targt = [row,col]
        # print(char)
        height_map[col].append(getHeight(char))
        col+=1
    row +=1

# targt = [4, 3]
height_map = np.array(height_map)
height_map = height_map.transpose()
# print(height_map.shape  )
max_row = height_map.shape[0]-1
max_col = height_map.shape[1]-1
print(height_map.shape)
big_step = height_map.size*2
# print(height_map)
# print(start,targt)
# print(height_map[2,5])
# exit()
visited = list()


def traverse(c:list,visited:list,steps:int) ->int:
    # each traverse tries to traverse  left, right, up, and down. 
    # traverse returns the amount of steps from the current position to the goal. 
    # If a step is illigal or runs into a previously visited square, it a large number is added to steps
    # if a step is legall, the return value of traverse is given.
    # Traverse returns the smallest value of the 4 possible step directions.
    # Traverse returns steps if c == targt
    steps_alternatives = [big_step, big_step, big_step, big_step]
    current_height = height_map[c[0],c[1]]
    # print(current_height)
    if c == targt:
        # print(steps,visited)
        return steps
    visited.append(tuple(c))
    # step left
    if c[0]>0:
        new_c = [c[0]-1,c[1]]

        # ugly repetions ahead....
        next_height = height_map[new_c[0],new_c[1]]
        if ((current_height+1)>=next_height) & (not (tuple(new_c) in visited)):
            # step is legal
            steps_alternatives[0] = traverse(new_c,visited.copy(),steps+1)

    # step right
    if c[0]<max_row:
        new_c = [c[0]+1,c[1]]
        
        next_height = height_map[new_c[0],new_c[1]]
        if ((current_height+1)>=next_height) & (not (tuple(new_c) in visited)):
            # step is legal
            steps_alternatives[1] = traverse(new_c,visited.copy(),steps+1)
            
    # step up
    if c[1]>0:
        new_c = [c[0],c[1]-1]
        
        next_height = height_map[new_c[0],new_c[1]]
        if ((current_height+1)>=next_height) & (not (tuple(new_c) in visited)):
            # step is legal
            steps_alternatives[2] = traverse(new_c,visited.copy(),steps+1)
        
        # step down
    if c[1]<max_col:
        new_c = [c[0],c[1]+1]
        
        next_height = height_map[new_c[0],new_c[1]]
        if ((current_height+1)>=next_height) & (not (tuple(new_c) in visited)):
            # step is legal
            steps_alternatives[3] = traverse(new_c,visited.copy(),steps+1)
    del(visited)
    return min(steps_alternatives)
    
    exit()
        

print("number of steps: ",traverse(start,visited,0))