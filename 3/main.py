print("Day 3 puzzle!")

f = open("input.txt","r")
rucksacks = f.readlines()

# Function for getting prio
def getPrio(arg):
    prio = ord(arg)
    if prio > ord('Z'):
        # small letter  
        return prio-ord('a') + 1
    else : 
        # big letter
        return prio-ord('A') + 27


prioSum = 0
groupPrio = 0
i = 0
for rucksack in rucksacks :   
    if i == 0:
        commonItems = set(rucksack.strip())
    else:
        commonItems = commonItems.intersection(set(rucksack))
    i+=1
    # print(commonItems)
    if i ==3:
        i = 0
        groupPrio += getPrio(commonItems.pop())

    compartment1 = set(rucksack[:len(rucksack)//2])
    compartment2 = set(rucksack[len(rucksack)//2:])
    dupe = compartment1.intersection(compartment2)
    prioSum += getPrio(dupe.pop())


print("First answer: " + str(prioSum))
print("Second answer: " + str(groupPrio))

f.close