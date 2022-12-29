
def drawPixel(register,pixel) -> bool:
    return abs(register-pixel)<2



register = 1
cycle = 0
signals = []
signal_counter = 1

f = open("input.txt","r")
lines = f.readlines()
f.close()

cycle = 0
instruction_pointer = 0
print("CRT for question 2:")
crt = ""
for i in range(42):
    crt+="-" 
# print(crt)

addx_input = 0
number_of_instructions = len(lines)
while instruction_pointer<number_of_instructions:
    if not cycle%40:
        print(crt)
        crt = " "
    
    if drawPixel(register,cycle%40):
        crt += "#"
    else:
        crt+= "."

    cycle +=1
    line = lines[instruction_pointer]
    # print(line.strip())
    
    if cycle >= 20*signal_counter:
        # odd, i.e  in middle of cycle
        signals.append(20*signal_counter*register)
        # print(register," ",cycle)
        signal_counter+=1
    #
    instruction = line.strip().split(" ")
    if instruction[0] == "addx":
        if addx_input:
            register += addx_input
            addx_input = 0
            instruction_pointer += 1 
        else:
            addx_input = int(instruction[1])
    else:
        instruction_pointer += 1

    
signals = [signals[i] for i in range(0,signal_counter-1,2)]
# print(signals)
sum_of_signals = sum(signals)
print(crt)
crt = ""
for i in range(42):
    crt+="-" 
print(crt)

print("answer 1 is: ", sum_of_signals)


