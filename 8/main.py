f = open("input.txt","r")
lines = f.readlines()
number_of_columns = (len(lines[0].strip()))
number_of_rows = len(lines)
tree_columns = [[] for i in range(number_of_columns)]
tree_rows  = [[] for i in range(number_of_rows)]
for i  in range(number_of_rows) :
    line = lines[i].strip()
    for j in range(number_of_columns):
        tree_height = int(line[j])
        tree_rows[i].append(tree_height)
        tree_columns[j].append(tree_height)

# print(tree_rows)
# print(tree_columns)

# input is parsed

def visible(row,i)-> bool:
    visible1 = True
    visible2 = True
    for tree in row[:i]:
        if row[i]<=tree:
            # print(row[i])
            visible1 = False
    
    for tree in row[i+1:]:
        if row[i]<=tree:
            visible2 = False
    return visible2 or visible1

def scenic_score(row,i) -> int:
    dist1 = 0
    dist2 = 0
    for tree in reversed(row[:i]):
        dist1 += 1
        if row[i]<=tree:
            break
    
    for tree in row[i+1:]:
        dist2 += 1
        if row[i]<=tree:
            break
    return dist1*dist2

visible_trees = 0
best_score = 0
for i in range(1,number_of_columns-1):
    for j in range(1,number_of_rows-1):
        # print(tree_rows[i],tree_rows[i][j],visible(tree_rows[i],j),"   ",tree_columns[j],tree_columns[j][i],visible(tree_columns[j],i))
        if visible(tree_rows[i],j) or visible(tree_columns[j],i):
            visible_trees += 1
        score = scenic_score(tree_rows[i],j) * scenic_score(tree_columns[j],i)
        if score > best_score:
            best_score = score
        # print(not_visible(tree_rows[0],3))

visible_trees += number_of_columns*number_of_rows - (number_of_rows-2)*(number_of_columns-2)
print("answer 1 is: " , visible_trees)
print("answer 2 is: " , best_score)