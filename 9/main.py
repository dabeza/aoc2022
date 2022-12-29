# import math


def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

class Rope:
    def __init__(self,start_x,start_y,length) -> None:
        self.rope = [[start_x,start_y]]
        self.length = length
        self.visited = {tuple}
        self.start_x = start_x
        self.start_y = start_y
        for i in range(length):
            self.rope.append([start_x,start_y])
        self.visited = {tuple([start_x,start_y])}
        
        

    def step(self,step_direction,step_length):
        current_rope = [c.copy() for c in self.rope]
        # print(current_rope)
        for i in range(step_length):
            #step the head
            for i in range(2):
                self.rope[0][i] += step_direction[i]
            #step the tail
            for j in range(1,self.length+1):
                # determine the vector between head and tail
                k = [self.rope[j-1][i]-self.rope[j][i] for i in range(2)]
                k_abs = [abs(k[i]) for i in range(2)]
                max_k = max(k_abs)
                max_i = k_abs.index(max_k)

                dist = 0
                for c in k:
                    dist += c**2

                
                if dist == 5:
                    # diagonal step
                    self.rope[j][max_i] += k[max_i]-sign(k[max_i])
                    self.rope[j][(max_i+1)%2] += k[(max_i+1)%2]
                elif dist == 8:
                #     double diagonal! 
                    self.rope[j][0] += k[0]-sign(k[0])
                    self.rope[j][1] += k[1]-sign(k[1])
                else:
                    # normal step
                    self.rope[j][max_i] += k[max_i]-sign(k[max_i])
                    
                self.visit()
            
            # self.print_state()
        



    def visit(self):
        # for i in range(1,self.length+1):
        self.visited.add(tuple(self.rope[self.length]))

    def print_state(self):
        print("--------------------------------------------------------------")
        for i in range(6):
            string = ""
            for j in range(6):
                print_dot = True
                for k in range(self.length+1):
                    if (i == self.rope[k][1]) & (j == self.rope[k][0]):
                        print_dot = False
                        if k ==0:
                            string += "H"
                            
                        else:
                            string += str(k)
                        break

                if print_dot:
                    if (i == self.start_y)&(j == self.start_x):
                        string += "s"
                    else:
                        string += "."
            # string += "\n"
            print(string)
           


            
f = open("input.txt","r")
lines = f.readlines()
key = {"R":[1,0], "L":[-1,0],"D":[0,1],"U":[0,-1]}

short_rope = Rope(0,0,1)
long_rope = Rope(0,5,9)
printme = True
for line in lines:
    instruction = line.strip().split(" ")
    step_direction  = key.get(instruction[0],"Error: not direction")
    step_length = int(instruction[1])

    short_rope.step(step_direction,step_length)
    long_rope.step(step_direction,step_length)


print("Answer to question 1 is: ", len(short_rope.visited))
print("Answer to question 2 is: ", len(long_rope.visited))

