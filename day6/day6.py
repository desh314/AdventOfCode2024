file = open("./input.txt", "r").readlines()

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def printGrid(grid):
    for i in grid:
        print(i)

def initGrid(file):
    grid = []

    cords = [0,0]

    for rowInd, row in enumerate(file):
        temp = []
        for colInd, col in enumerate(row.replace("\n", "")):
            if col == "^":
                cords = [rowInd, colInd]
            temp.append(col)
        grid.append(temp)

    return grid, cords


def path(cords, grid):
    #print(cords)

    ornt = 0
    
    orgCords = [cords[0], cords[1]]

    move = 0

    while (0 <= cords[0] < len(grid) and 0 <= cords[1] < len(grid[0])):

        #print(cords, orgCords, ornt)

        if cords == orgCords and move > 1 and ornt == 3:
                #print("CYCLE")
                return True
        

        if grid[cords[0]][cords[1]] == "#" or grid[cords[0]][cords[1]] == "O":
            cords[0] -= dirs[ornt][0]
            cords[1] -= dirs[ornt][1]

            ornt = (ornt+1) % 4
        
        elif grid[cords[0]][cords[1]] == "X":
            cords[0] += dirs[ornt][0]
            cords[1] += dirs[ornt][1]
        else:
            #out += 1
            grid[cords[0]][cords[1]] = "X"
            cords[0] += dirs[ornt][0]
            cords[1] += dirs[ornt][1]

        move += 1
    
    return False

out = 0

grid, cords = initGrid(file)

print(cords)

for rowInd in range(len(grid)):
    for colInd in range(len(grid[rowInd])):
        if grid[rowInd][colInd] not in ["^", "#"]:
            
            grid[rowInd][colInd] = "O"
            print(rowInd, colInd)
            if path(cords, grid):
                out += 1
            
            grid, cords = initGrid(file)

print(out)















            





        
