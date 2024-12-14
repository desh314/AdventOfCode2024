file = open("input.txt", "r").readlines()[0]

print(file)
pos = []

for index, value in enumerate(file):
    if value+file[index+1]+file[index+2] == "mul":
        pos.append(file[i:i+])

