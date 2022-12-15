

print("Wawaweewa, day 5!")

f = open("input.txt","r")
lines = f.readlines()

i = 0
for line in lines : 
    i +=1
    if line.strip() == "":
        number_of_stacks = int(prev_line.strip()[-1])
        blank_line_number = i
        break
    prev_line = line

stacks = [[] for i in range(number_of_stacks)]

read_cargo = True
i = 0
for line in lines : 
    i +=1
    if i<blank_line_number-1 :
        # make carbo list
        cargos = [line[j*4:j*4+3] for j in range(number_of_stacks)]
        j = -1
        for cargo in cargos :
            j+=1
            if (cargo[0] == '[') :
                # cargo!
               stacks[j].insert(0,cargo[1].strip())

            
    elif i>blank_line_number:
        x = line.strip().split(" ")
        moved_cargos, source, destination = int(x[1]),int(x[3])-1,int(x[5])-1
        # question 1
        for k in range(moved_cargos):
            stacks[destination].append(stacks[source].pop())

        # question 2
        transport = []
        for k in range(moved_cargos):
            transport.append(stacks_9001[source].pop())       
        for k in range(moved_cargos):
            stacks_9001[destination].append(transport.pop())       
        
    else :
        stacks_9001 = [stacks[j].copy() for j in range(number_of_stacks)]
        continue

answer1 = []
[answer1.append(stacks[i].pop()) for i in range(number_of_stacks)]
print("answer 1 is: " + "".join(answer1))

answer2 = []
[answer2.append(stacks_9001[i].pop()) for i in range(number_of_stacks)]
print("answer 1 is: " + "".join(answer2))

        
       

