
# rock: 1 pt : X : A
# paper : 2 pt : Y : B
# scissors : 3 pt : Z : C

# loose : 0 pt
# tie: 3 pt
# win : 6 pt

f = open("input.txt","r")
print("Day 2 puzzle!")
lines = f.readlines()
elfStrats = "ABC"
cheatStrats = "XYZ"

for i in range(2):
    totPts = 0
    for line in lines : 
        pts = 0
        line.strip()
        elfStrat = elfStrats.find(line[0])
        if i:
            key = cheatStrats.find(line[2])
            if key == 0 :
                #  loose - pick 1 less than elf (if B pick X)
                cheatStrat = elfStrat -1
                if cheatStrat == -1 : 
                    cheatStrat = 2
            elif key == 1:
                # tie - pcik elfStrat
                cheatStrat = elfStrat
            else :
                # win : pick 1 more than elf
                cheatStrat = elfStrat +1
                if cheatStrat == 3 : 
                    cheatStrat = 0
        else : 
            cheatStrat = cheatStrats.find(line[2])

        pts += cheatStrat+1
        # print(elfStrat)
        # print(cheatStrat)
        result = elfStrat-cheatStrat
        # print(result)
    
        if (result == 0):
            # tie
            pts += 3
        # elif (result == 1):
        #     # loss
        elif (result == 2):
            # edge case win: rock vs scissors
            pts += 6
        elif (result == -1):
            # winner winner chicken dinner
            pts += 6

        totPts += pts


    print("Answer " + str(i+1) + ": " + str(totPts))
    f.close