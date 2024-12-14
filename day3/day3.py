file = open("input.txt", "r").read()

pos = []

""" out = 0

def getNum (index):
    num = ""
    while (ord('0') <= ord(file[index]) <= ord('9')):
        num += file[index]
        index += 1
    return num, index

for index, value in enumerate(file):
    if file[index:index+4] == "mul(":
        index += 4
        num, newIndex = getNum(index)
        if file[newIndex] != "," or num == "":
            pass
        else:
            n1 = int(num)
            num, newIndex = getNum(newIndex+1)
            n2 = int(num)
            if file[newIndex] != ")":
                pass
            else:
                out += n1*n2 """



out = 0

def checkNum(string):
    for i in string:
        if not (ord('0') <= ord(i) <= ord('9')):
            return False
    
    return True


pS = [i.split(")")[0].split(",") for i in file.split("mul(")]

for i in pS:
    if len(i) != 2 or not(checkNum(i[0])) or not(checkNum(i[1])):
        pass
    else:
        out += int(i[0]) * int(i[1])

        

print(out)       