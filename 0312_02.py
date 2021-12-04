import numpy as np

def getOxygen (lista, index):
    if len(lista) == 1:
        return lista[0]
    one = 0
    zero = 0
    rm = []
    for i in lista:
        if i[index] == "1":
            one += 1
        else:
            zero += 1
    for count, i in enumerate(lista):
        if (i[index] == "0" and zero <= one):
            rm.append(count)
        elif (i[index] == "1" and zero > one):
            rm.append(count)
    lista = np.delete(lista, rm)
    return getOxygen(lista, index+1)

def CO2 (lista, index):
    if len(lista) == 1:
        return lista[0]
    one = 0
    zero = 0
    rm = []
    for i in lista:
        if i[index] == "1":
            one += 1
        else:
            zero += 1
    for count, i in enumerate(lista):
        if (i[index] == "0" and one < zero):
            rm.append(count)
        elif (i[index] == "1" and one >= zero):
            rm.append(count)
    lista = np.delete(lista, rm)
    return CO2(lista, index+1)

file = open("0312_01.txt", "r")
read = file.readlines()
for i in range(len(read)):
    read[i] = read[i].replace("\n","")
print(read)

oxy = getOxygen(read, 0)
co2 = CO2(read, 0)

a = 0
b = 0

for i in range(len(oxy)):
    if oxy[i] == "1":
        a += 2**(len(oxy)-1-i)
    if co2[i] == "1":
        b += 2**(len(oxy)-1-i)

print(a*b)
