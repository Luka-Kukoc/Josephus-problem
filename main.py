import math
x = int(input("How many people are there? "))
if math.log2(x).is_integer():
    print("Josephus should be at position: 1")
else:
    i = 1
    lst = []
    while i < x:
        i *= 2
        lst.append(i)
    b = lst[-2]
    winner = str(1 + 2*(x-b))
    print("Josephus should be at position:" + winner)
