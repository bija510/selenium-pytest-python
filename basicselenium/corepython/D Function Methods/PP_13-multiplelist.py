"""Iterating multiple lists at the same time """
#Start From lecture 43
L1 = [1, 2, 3]
L2 = [6, 7, 8, 22, 30, 40]

for a, b in zip(L1, L2):
    if a > b:
        print(a)
    else:
        print(b)
