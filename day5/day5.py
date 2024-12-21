import functools

file = open("./input.txt", "r").readlines()

rules = []
seqs = []

#using hashmap is the most effecient solution
#process the input data into the ordering and sequences

isNW = False
for line in file:
    if line == "\n":
        isNW = True
        continue

    if isNW:
        seqs.append(line.replace("\n", ""))
    else:
        rules.append(line.replace("\n", ""))

seqs = [i.split(",") for i in seqs] 

ruleDict = [] 

for rule in rules:
    fst, snd = (rule.split("|")[0], rule.split("|")[1])

    #(value, comes after value)
    ruleDict.append((fst, snd))

out = 0

def ordering(x, y):
    if x == y:
        return 0
    
    for fst, snd in ruleDict:
        if fst == x and snd == y:
            return 1
        elif fst == y and snd == x:
            return -1
    
    return 0

out = 0

for seqIndex, seq in enumerate(seqs):
    temp = True
    for index, val in enumerate(seq):
        for fst, snd in ruleDict:
            if fst in seq and snd in seq and val == fst:
                if snd not in seq[index:]:
                    temp = False
    
    if not temp:
        sortedSeq = sorted(seq, key=functools.cmp_to_key(ordering))
        out += int(sortedSeq[len(sortedSeq) // 2])
        
print(out)
#need to search through each element in the sequence but we 
#can get the ordering from the orderings in a hasmap
#to get O(1) look up of valid orderings

#hash map will allow us to avoid this third for loop search
""" out = 0

for seqIndex, seq in enumerate(seqs):
    temp = True
    for index, val in enumerate(seq):
        for fst, snd in ruleDict:
            if fst in seq and snd in seq and val == fst:
                if snd not in seq[index:]:
                    temp = False
    
    if not temp: """

"""
        BASICALLY IMPLEMENTED ONE ITERATION OF BUBBLE
        SORT BUT WE NEED TO KEEP DOING THE SAME THING
        UNTIL THE LIST IS SORTED
        algo: take one element and compare the rest of the list and then
        add it into the sorted list and do it repeatedly
        - need to keep doing it more than one pass
        - same as bubble sort but we need to keep doing it so all 
        - the intermediary elements are sorted!!!
        
        problem with this sorting is that it only goes through the list once
        we need to sort the whole list but this only does one pass so some stuff
        is not sorted like 
        
        Bad Pair is:  95   43
        ['89', '26', '43', '95', '83']

        so the 95 and 43 will not be sorted in the first pass
        need to sort it on the second pass ect.

        basically idea is to use a sorting algorithm with
        a custom compare function based on the orderings.
        
        """
""" tempSeq = []


        cmpLen = len(seq)

    --> NEED A SECOND WHILE LOOP OUTSIDE THAT CHECKS IF SORTED AND DOES THE THING
    INSIDE REPEATEDLY

    
        while (len(tempSeq) < cmpLen): INSTEAD OF WHILE WITH THE LENGTH OF THE LIST
            DO IT UNTIL THE LISTS ARE SORTED 
            ---> NEED A FUNCTION THAT CHECKS IF SORTED AND WHILE LOOP ON THAT!
            for i, v in enumerate(seq):
                if i == 0:
                    subSeq = seq[i+1:]
                elif i == len(seq)-1:
                    subSeq = seq[:i]
                else:
                    subSeq = seq[:i-1]+seq[i:]
                
                allValid = True

                for fst, snd in ruleDict:
                    if fst == v and snd in subSeq:
                        allValid = False
                        break
                
                if allValid:
                    tempSeq.insert(0, v)
                    seq.pop(i)
        seqs[seqIndex] = tempSeq """
        #print(len(tempSeq), cmpLen)
        
        #out += int(tempSeq[len(tempSeq) // 2])

""" for seqIndex, seq in enumerate(seqs):
    temp = True
    for index, val in enumerate(seq):
        for fst, snd in ruleDict:
            if fst in seq and snd in seq and val == fst:
                if snd not in seq[index:]:
                    temp = False
                    print("Bad Pair is: ", fst, " ", snd)
    
    if not temp:
        print(seq) """
    

""" if temp:
        out += int(seq[len(seq)//2]) """

"""     if not temp:
        newSeq = [] 
        tempSeq = seq

        while (len(tempSeq) > 0):
            for i, v in enumerate(tempSeq):
                works = True
                for fst, snd in ruleDict:
                    if fst == v and snd in tempSeq and snd not in tempSeq[:i-1]+tempSeq[i:]:
                        
                        works = False
                        break
                if works == True:
                    print("yay")
                    newSeq.append(v)
                    tempSeq = tempSeq[:i-1]+tempSeq[i:]
                    break
            print(tempSeq)
        
        newSeq += tempSeq

        print(newSeq) """


### if in the list => ordering applies (not in list or ordering applies)

""" for seq in seqs:
    for index, val in enumerate(seq):
        if val in ruleDict:
             """


""" ruleDict = {} 

for rule in rules:
    fst, snd = (rule.split("|")[0], rule.split("|")[1])

    if snd in ruleDict.keys():
        ruleDict[snd].append(fst)
    else:
        ruleDict[snd] = [fst]

for seq in seqs:
    for index, val in enumerate(seq):
        temp = True
        for """

#create a dictionary from the orderings

""" ruleDict = {} 
for rule in rules:
    fst, snd = (rule.split("|")[0], rule.split("|")[1])

    if fst in ruleDict.keys():
        ruleDict[fst].append(snd)
    else:
        ruleDict[fst] = [snd]

revRuleDict = {}

for key, val in zip(ruleDict.keys, ruleDict.values):
    revRuleDict """


#run split on the sequences to get the correct data values 

""" def check(items, xs):
    for i in items:
        if i not in xs:
            print(items, xs)
            return False
    
    return True

for seq in seqs:
    temp = True
    for index, val in enumerate(seq):
        if val in ruleDict:
            if not check(ruleDict[val], seq[index:]):
                temp = False
    
    print(seq, temp) """

""" 
revert the hash table and 
use the values to check if the key is 
in front of the value in the sequence


23:45

if 45 in the sequence then 23 is before it

use this logic to go from back of list
to the forward of the list

preserve the ordering

left:right

left to right maps one to many

but right to left maos many to one
so it is valid
 """