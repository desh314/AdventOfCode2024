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

#75,97,47,61,53

for seq in seqs:

    tempSeq = []

    cmpLen = len(seq)

    while (len(tempSeq) < cmpLen):
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
                tempSeq.append(v)
                seq.pop(i)
    
    out += int(tempSeq[len(tempSeq) // 2])
                

print(out)
    

