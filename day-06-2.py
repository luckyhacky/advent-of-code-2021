input = """4,1,1,1,5,1,3,1,5,3,4,3,3,1,3,3,1,5,3,2,4,4,3,4,1,4,2,2,1,3,5,1,1,3,2,5,1,1,4,2,5,4,3,2,5,3,3,4,5,4,3,5,4,2,5,5,2,2,2,3,5,5,4,2,1,1,5,1,4,3,2,2,1,2,1,5,3,3,3,5,1,5,4,2,2,2,1,4,2,5,2,3,3,2,3,4,4,1,4,4,3,1,1,1,1,1,4,4,5,4,2,5,1,5,4,4,5,2,3,5,4,1,4,5,2,1,1,2,5,4,5,5,1,1,1,1,1,4,5,3,1,3,4,3,3,1,5,4,2,1,4,4,4,1,1,3,1,3,5,3,1,4,5,3,5,1,1,2,2,4,4,1,4,1,3,1,1,3,1,3,3,5,4,2,1,1,2,1,2,3,3,5,4,1,1,2,1,2,5,3,1,5,4,3,1,5,2,3,4,4,3,1,1,1,2,1,1,2,1,5,4,2,2,1,4,3,1,1,1,1,3,1,5,2,4,1,3,2,3,4,3,4,2,1,2,1,2,4,2,1,5,2,2,5,5,1,1,2,3,1,1,1,3,5,1,3,5,1,3,3,2,4,5,5,3,1,4,1,5,2,4,5,5,5,2,4,2,2,5,2,4,1,3,2,1,1,4,4,1,5"""


fish = list(map(int, input.split(",")))
#DAYS = 80
DAYS = 256

cat = [0, 0, 0, 0, 0, 0, 0, 0, 0] # days left untils spawn of fish

for i in range(0, len(fish)):
    cat[fish[i]] += 1

print("solution: ", sum(cat))
print(cat)
print("----")
# work with pointer
ptr = 0
for d in range(0, DAYS):
    # safe fish from state 7
    tmp = cat[7]
    
    # move state 8 fish to state 7 fish
    cat[7] = cat[8]
    
    # create new fish
    cat[8] = cat[ptr]
    
    
    # add state 7 fish to normal fish which have timer 6
    cat[ptr] += tmp
    
    #move pointer
    ptr = (ptr + 1) % 7
    print(ptr, cat, sum(cat))

print("----")
print(cat)

print("solution: ", sum(cat))

