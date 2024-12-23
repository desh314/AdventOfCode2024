file = [list(i.replace("\n", "")) for i in open("input.txt", "r").readlines()]

def checkCycle(grid):
    sr, sc = 0, 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if file[r][c] == "^":
                sr = r
                sc = c

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    ornt = 0

    out = 0

    visited = []

    ir, ic = sr, sc

    ir -= 1

    while ir in range(len(file)) and ic in range(len(file[0])):

        if file[ir][ic] == "#":
                ir -= dirs[ornt][0]
                ic -= dirs[ornt][1]

                ornt = (ornt+1) % 4
        else:
            if (ir, ic) not in visited:
                out += 1
            

            if ir == sr and ic == sc and ornt == 0:
                temp = True
                for i in range(len(visited)):
                        if file[ir][ic] == "#":
                            ir -= dirs[ornt][0]
                            ic -= dirs[ornt][1]

                            ornt = (ornt+1) % 4
                        else:
                            if (ir, ic) not in visited:
                                temp = False
                                break
                            
                            visited.append((ir, ic))
                            ir += dirs[ornt][0]
                            ic += dirs[ornt][1]
                if temp:
                    print("CYCLE")
                    return True
    
    return False
                  
#cycle means you need to check if the whole subsequence of 
# directions is repeated not only the start coordinate
# the whole sequence of cyclic coordinates must be contained
# within the visited sequence        
         
out = 0
for rowInd, row in enumerate(file):
     for colInd, col in enumerate(row):
        if file[rowInd][colInd] not in ["^", "#"]:
            file[rowInd][colInd] = "#"
            if checkCycle(file):
                out += 1
            file[rowInd][colInd] = "."

print(out)
               