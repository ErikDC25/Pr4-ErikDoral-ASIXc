"""
Erik Doral
4-12-2023
ASIXc 1A M03 UF1
"""
BLANC = "⬜"
NEGRE = "⬛"
res = 9
for col in range(1, 9):
    print(res-col, " ", end="")
    for fil in range(1, 9):
        if (fil + col) % 2 == 0:
            print(NEGRE, end=" ")
        else:
            print(BLANC, end=" ")
    print("")
print("  ", end=" ")
for let in range(ord("a"), ord("i")):
    print(chr(let), end=" ")
