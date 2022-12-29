

print("Day 4 puzzle!")

f = open("input.txt","r")
pairs = f.readlines()
number_of_total_overlaps = 0
number_of_semi_overlaps = 0
for pair in pairs : 
    delimiters = [int(i) for i in pair.strip().replace("-",",").split(",")]
    # question 1
    if ((delimiters[1]>delimiters[3]) == (delimiters[0]<delimiters[2]))| ((delimiters[1]<delimiters[3]) == (delimiters[0]>delimiters[2])):
        # total overlap!
        number_of_total_overlaps +=1

    #question 2
    if ((delimiters[1]>=delimiters[2]))&(delimiters[3]>=delimiters[0]):
        # some overlap
        print(delimiters)
        number_of_semi_overlaps +=1

print("Answer to question 1: " +str(number_of_total_overlaps))
print("Answer to question 2: " +str(number_of_semi_overlaps))