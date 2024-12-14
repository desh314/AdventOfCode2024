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




def checkNum(string):
    for i in string:
        if not (ord('0') <= ord(i) <= ord('9')):
            return False
    
    return True


def getOut(string):
    out = 0
    pS = [i.split(")")[0].split(",") for i in string.split("mul(")]

    for i in pS:
        if len(i) != 2 or not(checkNum(i[0])) or not(checkNum(i[1])):
            pass
        else:
            out += int(i[0]) * int(i[1])
    return out

"""
validInst = []
temp = ""
index = 0

while (index < len(file)):
    if file[index:index+4] == "do()":
        while (file[index:index+7] != "don't()" and index < len(file)):
            temp += file[index]
            index += 1
        validInst.append(temp)
        temp = ""
    else:
        index += 1 """

nums = [getOut(i.split("don't()")[0]) for i in file.split("do()")]

fOut = 0

for i in nums:
    fOut += i

print(fOut)
    