file = open("./input.txt", "r")

""" totalSafe = 0

for index, line in enumerate(file):
    fmtLine = [int(i) for i in line.replace("\n", "").split(" ")]
    isSafe = 1
    diff = []
    if (fmtLine[0] > fmtLine[1]):
        for i, j in zip(fmtLine[:-1], fmtLine[1:]):
            if i < j or i == j or i - j < 1 or i - j > 3:
                isSafe = 0
                break
    else:
        for i, j in zip(fmtLine[:-1], fmtLine[1:]):
            if i > j or i == j or i - j < 1 or i - j > 3:
                isSafe = 0
                break """
    
"""     diff = []
    inc = fmtLine[0] < fmtLine[1]
    for i, j in zip(fmtLine[:-1], fmtLine[1:]):
        if inc and i-j < 0:
            isSafe = 0
            break
        if not inc and i-j > 0:
            isSafe = 0
            break
        diff.append(abs(i-j))
    
    print(isSafe)
    
    if isSafe == 1:
        for i in diff:
            if i not in [1,2,3]:
                isSafe = 0
                break
    
    totalSafe += isSafe

print(totalSafe) """
    
##using a hash map

def checker(fmtLine):
    diff = []
    
    for nxt, curr in zip(fmtLine[1:], fmtLine[:-1]):
        diff.append(curr-nxt)

    for nxt, curr in zip(diff[1:], diff[:-1]):
        if nxt*curr < 0 or abs(curr) not in [1,2,3] or abs(nxt) not in [1,2,3]:
            return 0
    
    return 1


safeScore = 0

for index, line in enumerate(file):
    fmtLine = [int(i) for i in line.replace("\n", "").split(" ")]

    diff = []
    isSafe = 0

    for i in range(0, len(fmtLine) ):
        #print(fmtLine[:i]+fmtLine[i+1:])
        if checker(fmtLine[:i]+fmtLine[i+1:]) == 1:
            isSafe = 1
            break

    
    
    if checker(fmtLine) == 1:
        isSafe = 1

    safeScore += isSafe

print(safeScore)
    
    



    

