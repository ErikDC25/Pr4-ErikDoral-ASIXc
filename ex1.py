"""
Erik Doral
4-12-2023
ASIXc 1A M03 UF1
"""
num0 = 0
numpos = 0
numne = 0

for i in range(0, 10):
    num = int(input("Digam un numero:"))
    if num == 0:
        num0 = num0 + 1
    elif num <= -1:
        numne = numne + 1
    else:
        numpos = numpos + 1
print("Hi han:", num0, "ceros,", numne, "numeros negatius i", numpos, "numeros positius.")


