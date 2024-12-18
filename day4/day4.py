
#dynamic programming solution?

#first fill out all the valid x's and then all the M's around the X's and
#on for all the letters to find the solutions. 
#the #of x's is the count 

#brute force search the rows, columns and diagonals??
""" for index, value in enumerate(file):
    for indexSub, valueSub in enumerate(value):
        if valueSub == "X" and file[index+1][indexSub] != "X" and :
            solvedGrid[value] """

#use a 4x4 kernel of valid XMAS values and apply it on a the grid, 
#if there is a row, column or diagonal match then its valid

""" class Grid:
    def __init__(self, nested):
        self.grid = nested
    
    def blankGrid(self, rows, cols):
        self.grid = []
        for i in range(rows):
            tempRow = []
            for j in range(cols):
                tempRow.append(".")
            self.grid.append(tempRow)
    
    def printGrid(self):
        for i in self.grid:
            print(i)
        
solGrid = Grid([])
dataGrid = Grid(file)

solGrid.blankGrid(len(file), len(file[0]))

solGrid.printGrid()
dataGrid.printGrid() """

#recursive search
#1)check for the next letter in the surroundings
#2)check for the next letter in the surroundings
#3)if no valid letters than stop the search in that 
#recrusive direction
""" 
word = "XMAS"

colLen = len(file[0])
rowLen = len(file)

##recursive grid search on every X

#brute force might be more effecient

def search(searchLetter, col, row):

    if (0 <= col and col < colLen and 0 <= row and row < rowLen):
        if (word[searchLetter] != file[row][col] or searchLetter >= len(word)):
            return 0
        if (searchLetter == len(word)-1 and word[searchLetter] == file[row][col]):
            return 1

    
        search(searchLetter+1, col+1, row)
        search(searchLetter+1, col-1, row)

        search(searchLetter+1, col, row+1)
        search(searchLetter+1, col, row-1)

        search(searchLetter+1, col+1, row)
        search(searchLetter+1, col-1, row)


for rowNum, row in enumerate(file):
    for colNum, col in enumerate(row):
        if (col == "X"):
            count = 0
            search(0, colNum, rowNum)
            print(count) """
""" 
colLen = len(file[0]) - 1
rowLen = len(file) - 1

def check(guess, val):
    if (len(guess) > len(val)):
        return False
    
    for index, char in enumerate(guess):
        if (char != val[index]):
            return False
    
    if (len(guess) == len(val)):
        return True
    
    return False

count = 0

def search(string, colNum, rowNum, count):
    #print(string)

    if (len(string)>len("XMAS")):
        return

    if (rowNum > rowLen or colNum > colLen or colNum < 0 or rowNum < 0):
        return
    
    if check(string, "XMAS"):
        print(string)
        count = count + 1
        return
        
    search(string+file[rowNum][colNum], rowNum, colNum+1, count)
    search(string+file[rowNum][colNum], rowNum, colNum-1, count)

    search(string+file[rowNum][colNum], rowNum+1, colNum, count)
    search(string+file[rowNum][colNum], rowNum-1, colNum, count)

    search(string+file[rowNum][colNum], rowNum-1, colNum-1, count)
    search(string+file[rowNum][colNum], rowNum+1, colNum+1, count)

    search(string+file[rowNum][colNum], rowNum+1, colNum-1, count)
    search(string+file[rowNum][colNum], rowNum-1, colNum+1, count)
    
    

for rowNum, row in enumerate(file):
    for colNum, col in enumerate(row):
        if (col == "X"):
            search("", colNum, rowNum, count)
            print(count)
            count = 0 """

#file is rows

file = open("input.txt", "r").readlines()

rows = list([i.replace("\n", "") for i in file])


def transpose(xs):
    return ["".join([i[j] for i in xs]) for j in range(0, len(xs))]

cols = transpose(rows)

# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33

#diagl
# 03
# 02 13
# 01 12 23 

# 00 11 22 33
# 10 21 32
# 20 31
# 30

#we actaully only need to generate
#the bottom cause then flip

#diagr is the same algorithm but flip the cols and then
#transpose on that

def diag(row, col, grid):
    diagStr = ""
    while (row < len(grid) and row >= 0 and col >= 0 and col < len(grid[0])):
        diagStr += grid[row][col]
        row += 1
        col += 1
    return diagStr

diagsL = [diag(0, i, rows) for i in range(len(rows[0]))] + [diag(i, 0, rows) for i in range(1,len(rows))]
tempRows = list(reversed(rows))
#print(tempRows)
diagsR = [diag(0, i, tempRows) for i in range(len(rows[0]))] + [diag(i, 0, tempRows) for i in range(1,len(rows))]

#print(diagsR)
""" out = 0

for i in rows:
    if "XMAS" in i:

        out += i.count("XMAS")
    if "XMAS" in i[::-1]:

        out += i[::-1].count("XMAS")

for i in cols:
    if "XMAS" in i:

        out += i.count("XMAS")
    if "XMAS" in i[::-1]:

        out += i[::-1].count("XMAS")

for i in diagsR:
    if "XMAS" in i:

        out += i.count("XMAS")
    if "XMAS" in i[::-1]:

        out += i[::-1].count("XMAS")

for i in diagsL:
    if "XMAS" in i:

        out += i.count("XMAS")
    if "XMAS" in i[::-1]:

        out += i[::-1].count("XMAS")

print(out)
 """

""" def checkX(diag1, diag2):
    length = 0
    if len(diag1) <= len(diag2):
        length = len(diag1)
    else:
        length = len(diag2)
    
    for i in range(1, length-1):

        if diag1[i] == "A" and diag1[i] == diag2[i] and diag1[i-1:i+2] in ["SAM", "MAS"] and diag2[i-1:i+2] in ["SAM", "MAS"]:
            print(diag1[i-1:i+2], diag2[i-1:i+2])
            print(diag1, diag2)
            return True
    
    return False

out = 0 """



""" for i in diagsL:
    for j in diagsR:
        #print(i,j)
        if checkX(i, j):
            out += 1 """
count = 0
for rowNum, row in enumerate(rows):
    for colNum, col in enumerate(row):
        if col == "A" and (rowNum-1 >= 0 and rowNum+1 < len(rows) and colNum+1 <len(rows[0]) and colNum-1 >= 0):
            temp = 0

            if rows[rowNum+1][colNum-1] + col + rows[rowNum-1][colNum+1] in ["MAS", "SAM"]:
                temp += 1
            if rows[rowNum+1][colNum+1] + col + rows[rowNum-1][colNum-1] in ["MAS", "SAM"]:
                temp += 1
            
            if temp == 2:
                count += 1


print(count)
#101
#010
#101
    