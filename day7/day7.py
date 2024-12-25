file = [i.replace("\n", "").split(":") for i in open("./input.txt", "r").readlines()]

#data processing
eqs = {}
for pair in file:
    eqs[int(pair[0])] = [int(i) for i in pair[1].split(" ")[1:]]

def search(currVal, oprnds, target):

    if oprnds == []:
        return currVal == target
    
    if currVal > target:
        return False
    
    if search(currVal+oprnds[0], oprnds[1:], target):
        return True
    
    if search(currVal*oprnds[0], oprnds[1:], target):
        return True

    return search(int(str(currVal)+str(oprnds[0])), oprnds[1:], target)

#how to make more effecient than to use a 3 branch recursion tree
#for part two

#basically a binary tree recursion and use boolean values 
#to go back up the recursion tree
#all we need is one false to elimante the whole branch so we can do
# if search(...)
out = 0

for key in eqs.keys():
    if search(1, eqs[key], key):
        out += key

print(out)

