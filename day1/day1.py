inputFile = open("./input.txt", "r").readlines()

vec1 = []
vec2 = []

for i, line in enumerate(inputFile):
    nums = line.split("   ")
    vec1.append(int(nums[0].replace("\n", "")))
    vec2.append(int(nums[1].replace("\n", "")))

hset = {} #create a frequency hash table from vec1

for index, value in enumerate(vec1):
    if value in hset:
        hset[value] += 1
    else:
        hset[value] = 1

#calculate similarity score

out = 0

for i in vec2:
    if i in hset:
        out += i*hset[i]

print(out)
#calculate difference score
""" vec1.sort()
vec2.sort()

out = 0

for i, j in zip(vec1, vec2):
    out += abs(i-j)

print(out) """

