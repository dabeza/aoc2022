

f = open("input.txt","r")
lines = f.readlines()
f.close()

i = 0

def compare(left,right,indent) -> int:
    my_indent =" "
    for i in range(3*indent):
        my_indent+=" "
    # print(my_indent," - Compare ",left," vs ", right)
    indent+=1
    if (type(left) is int ) and (type(right) is int):
        # both are ints, return true if left is smaller or equal to right
        if left ==right :
            return 0
        elif left < right:
            return 1
        else:
            return -1
    elif (type(left) is list) and (type(right) is list):
        length_left,length_right = len(left),len(right)
        for j in range(max([length_left,length_right])):
            if j>length_left-1:
                # ran out of left: return 0 if both are same length otherwise return 1
                if length_left==length_right:
                    return 0
                return 1
            elif j> length_right-1:
                # ran out right, since we're not out of left: return false
                return -1    
            # check 
            cmp = compare(left[j],right[j],indent) 
            if cmp != 0:
                return cmp
        # made it here: all checks have been 0, return 1?
        return 0
    elif (type(left) is list) and not (type(right) is list):
        # turn right into list and compare
        return compare(left,[right],indent)
    elif not (type(left) is list) and (type(right) is list):
        # turn left into list and compare
        return compare([left],right,indent)
    else:
        print("ran into error when comparing:")
        print("\n",left,"\n",right)
        exit()


# Question 1
pair = 0
good_pairs = 0
signal = []
while i < len(lines):
    pair +=1
    left = eval(lines[i].strip())
    right = eval(lines[i+1].strip())
    i+=3

    # print("== Pair ",pair," ==")
    # print("comparing:","\n",left,"\n",right)
    result = compare(left,right,0)
    # print(result,"\n")
    if result>0:
        good_pairs += pair
        signal.append(left)
        signal.append(right)
    else: 
        signal.append(right)
        signal.append(left)
    
    
print("Answer Q1: ", good_pairs)

i = 0
I = len(signal)
signal.append([[2]])
signal.append([[6]])

sorted = []
sorted.insert(0,signal.pop(0))
last_index,failed_insertions = 0,0

while signal:
    insert = signal.pop(0)
    # print(insert)
    insertion_failed = True
    # test first position
    if compare(insert,sorted[0],0) >0:
        sorted.insert(0,insert)
        insertion_failed = False
    elif compare(sorted[last_index], insert,0)>0:
        sorted.append(insert)
        insertion_failed = False
    else:
        for j in range(1,last_index):
            if compare(insert,sorted[j],0) >0 and compare(sorted[j-1],insert,0) >0:
                sorted.insert(j,insert)
                insertion_failed = False
                break
    if insertion_failed:
        failed_insertions +=1
        signal.append(insert)
    else:
        last_index +=1
    
for i in range(len(sorted)):
    # print(i+1," : ", sorted[i])
    if sorted[i] == [[2]]:
        m1 = i+1
    elif sorted[i] == [[6]]:
        m2 = i+1
        
# print(sorted) 
print("Answer Q2: ",m1*m2 )

# print("number of failed sorting insertions: ",failed_insertions)