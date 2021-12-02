file = open("0112_01.txt", "r")
read = file.readlines()
dicti = {}
count = 1
deeper = 0
for i in range((len(read)-2)):
    dicti[i] = int(read[i]) + int(read[i+1]) + int(int(read[i+2]))

i = 1
while i < len(dicti):
    if dicti[i] > dicti[i-1]:
        deeper += 1
    i += 1
print(deeper)
file.close()