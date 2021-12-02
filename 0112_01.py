file = open("0112_01.txt", "r")
read = file.readlines()
deeper = 0
for count, value in enumerate((read[1:])):
    if int(value) > int(read[count]):
        deeper += 1
print(deeper)
file.close()