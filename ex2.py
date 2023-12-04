"""
Erik Doral
4-12-2023
ASIXc 1A M03 UF1
"""
al = int(input("Digam l'alçada del triangle(Ha de ser un numero entre 2 i 9)"))
for i in range(1, al + 1):
    for j in range(1, i):
        print(j, end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
print("")
