file = open("0212_01.txt", "r")
read = file.readlines()
dicti = {}
for i in range(len(read)):
    read[i] = read[i].split(" ")
    if read[i][0] in dicti:
        dicti[read[i][0]] += int(read[i][1])
    else:
        dicti[read[i][0]] = int(read[i][1])

print(dicti["forward"]*(dicti["down"]-dicti["up"]))
file.close()