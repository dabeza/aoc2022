# paramaters
file_name = "input.txt"
number_of_rounds = [20,10000]

class Monkey:
    def __init__(self,items:list,operation:str,test_numerator:int,if_true:int,if_false:int) -> None:
        self.items = items
        self.operation = eval("lambda old: " + operation)
        self.test_numerator = test_numerator
        self.if_true = if_true
        self.if_false = if_false
        self.inspections = 0

    def find_target(self,worry)-> int:
        if not worry%self.test_numerator: # is divisible by numerator
            return self.if_true
        else :
            return self.if_false

    def inspect(self,item) -> int:
        item = self.operation(item)
        self.inspections +=1
        return item

    def throw(self) -> None:
        global monkeys, chilling
        item = self.items.pop(0)        # hold item
        item = self.inspect(item)       # inspect item
        if chilling:
            item = item//3                  # get bored of item and loose worrylevel
        else:
             # worry = X * product_of_all_tests + Y. 
             # If worry%test = 0, then Y%test = 0 as X*product_of_all_tests%test = 0. 
             # Thus, worry of any item can be replaced by Y.
             # Y = worry % product_of_all_tests
            item = item % product_of_all_tests
        target = self.find_target(item) # decide monkey friend target
        monkeys[target].items.append(item)

    def take_turn(self):
        while 0<len(self.items):
            self.throw()
        
# parse monkeys

f = open(file_name,"r")
lines = f.readlines()
f.close()

product_of_all_tests = 1
for question in range(2):
    monkeys = []
    i = 0
    chilling = not question
    while i <len(lines):
        # monkey number on first position: skip as list their list index accounts for this
        i+=1
        #monkey list
        items = [int(item) for item in lines[i].split(":")[1].split(",")]
        i += 1
        # get operation string
        operation = lines[i].split("=")[1].strip()
        i +=1
        # test numerator
        test_numerator = int(lines[i].split("by")[1].strip())
        
        product_of_all_tests *= test_numerator
        i+=1

        if_true = int(lines[i].split("monkey")[1].strip())
        i+=1

        if_false = int(lines[i].split("monkey")[1].strip())

        monkeys.append(Monkey(items,operation,test_numerator,if_true,if_false))
        i+=2  #extra space

    for round in range(number_of_rounds[question]):
        for monkey in monkeys:
            monkey.take_turn()

    inspections = [monkey.inspections for monkey in monkeys]
    tmp = inspections.copy()
    tmp.sort()
    print("Monkey business " + str(question+1) +" is: ", tmp[-1]*tmp[-2])
