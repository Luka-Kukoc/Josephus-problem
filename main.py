import math
x = int(input("How many people are there? "))
if math.log2(x).is_integer():
    print("Josephus should be at position: 1")
else:
    i = 1
    while i < x:
        if i * 2 > x:
            break
        else:
            i *= 2
    winner = str(1 + 2*(x-i))
    print("Josephus should be at position:" + winner)
