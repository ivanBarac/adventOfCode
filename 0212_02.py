file = open("0212_01.txt", "r")
read = file.readlines()
dicti = {"forward": 0, "depth": 0}
aim = 0
for i in range(len(read)):
    read[i] = read[i].split(" ")
    if read[i][0] == "forward":
        dicti["forward"] += int(read[i][1])
        dicti["depth"] += aim*int(read[i][1])
    elif read[i][0] == "up":
        aim -= int(read[i][1])
    else:
        aim += int(read[i][1])

print(dicti["forward"] * dicti["depth"])
file.close()