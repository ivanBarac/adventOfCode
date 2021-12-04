file = open("0312_01.txt", "r")
read = file.readlines()
dicti = {i: 0 for i in range(len(read[0].replace("\n", "")))}
for i in range(len(read)):
    read[i] = read[i].replace("\n", "")
    for j in range(len(read[i])):
        dicti[j] += int(read[i][j])

gamma = 0
epsilon = 0

for i in dicti:
    if dicti[i] > len(read)//2:
        gamma += 2**(len(read[0])-i-1)
    else:
        epsilon += 2**(len(read[0])-i-1)

print(gamma * epsilon)