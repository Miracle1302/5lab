
array = []


for i in range(7, 0, -1):
    array.append([i] * 7)


for row in array:
    print(" ".join(map(str, row)))
