file = [list(i.replace("\n", "")) for i in open("input.txt", "r").readlines()]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

startRow, startCol = 0, 0
for row in range(len(file)):
    for col in range(len(file[row])):
        if file[row][col] == "^":
            startRow = row
            startCol = col

        
def findPath(file, startRow, startCol):

    indexRow, indexCol = startRow, startCol
    indexRow -= 1
    ornt = 0

    visited = set()

    out = 0

    while indexRow in range(len(file)) and indexCol in range(len(file[0])):
        
        if file[indexRow][indexCol] == "#":
            indexRow -= dirs[ornt][0]
            indexCol -= dirs[ornt][1]
            ornt = (ornt + 1) % 4
        else:
            if (indexRow, indexCol) not in visited:
                    out += 1

            visited.add((indexRow, indexCol))
            indexRow += dirs[ornt][0]
            indexCol += dirs[ornt][1]
    return visited

     
     
def checkCycle(file, startRow, startCol):

    indexRow, indexCol = startRow, startCol
    indexRow -= 1

    ornt = 0
    visited = []

    while indexRow in range(len(file)) and indexCol in range(len(file[0])):
        
        #print(visited, ornt)

        if (indexRow, indexCol, ornt) in visited:
                return True
        
        if file[indexRow][indexCol] == "#":
            indexRow -= dirs[ornt][0]
            indexCol -= dirs[ornt][1]
            ornt = (ornt + 1) % 4
        else:
            visited.append((indexRow, indexCol, ornt))
            indexRow += dirs[ornt][0]
            indexCol += dirs[ornt][1]
    
    return False

#need to keep searching as we can go through the start point multiple times

#to check cycle it is enough to check if the same point is passed with the same
#orientation as the gaurd will follow the same path then

#not enough to just check (startRow, startCol) as we can pass the same start
#point with multiple orientations so we need to keep searching until
#either there is a cycle and we pass through the start point with the same orientation

#or we go out of bounds

#implicit assumptions: either cycle or go out of bounds


#only need to search for obstructions not in the way of the gaurd

""" out = 0
for rowInd, row in enumerate(file):
     for colInd, col in enumerate(row):
        print(rowInd, colInd)
        if file[rowInd][colInd] not in ["^", "#"]:
            file[rowInd][colInd] = "#"
            if checkCycle(file):
                out += 1
            file[rowInd][colInd] = "."

print(out) """

out = 0
count = 0

outLength = len(findPath(file, startRow, startCol))

for rowInd, colInd in findPath(file, startRow, startCol):
    #print(rowInd, colInd)
    print(count, " / ", outLength)
    if file[rowInd][colInd] not in ["^", "#"]:
        file[rowInd][colInd] = "#"
        if checkCycle(file, startRow, startCol):
            out += 1
        file[rowInd][colInd] = "."
    count += 1

print(out)