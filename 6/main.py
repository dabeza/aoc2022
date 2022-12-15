


f = open("input.txt","r")
stream = f.readline()
# print((stream))
for j in range(4,len(stream)+1):
    if len(set(stream[j-4:j]))>3:
        print("answer 1 is: " +  str(j))
        break

for j in range(14,len(stream)+1):
    if len(set(stream[j-14:j]))>13:
        print("answer 2 is: " +  str(j))
        break