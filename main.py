x = int(input("How many people are there? "))
i = 1
lst = []
while i < x:
    i *= 2
    lst.append(i)
b = lst[-2]
a = x - b
winner = str(1 + 2*a)
print("Josephus should be at position:" + winner)