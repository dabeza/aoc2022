
elves = []
i = 0
maxCalory = -1
elfCalories = []
topThreeElves = 0
# print("hello world ")
f = open("input.txt","r")
lines = f.readlines()
elf = []
for x in lines:
    i +=1

    line = x.strip()
    # print(line)
    if line == '':
        # empty line - > check calorie of elf -> new elf
        elfCalory = 0
        for food in elf : 
            elfCalory += int(food)
        if maxCalory < elfCalory : 
            maxCalory = elfCalory
        elfCalories.append(elfCalory)
        elf = []
    else:
        # not empty line -> calory -> add to elf
        elf.append(line)

elfCalories.sort(reverse=True)

print(maxCalory)

for j in range(3) :
    topThreeElves += elfCalories[j]
print(topThreeElves)
#hello?
    

