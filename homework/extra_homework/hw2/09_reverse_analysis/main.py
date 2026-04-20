list = [1, 4, -3, 0, 10, 6, 7, 8]

for i in range(len(list) - 1, -1, -1):
    if list[i] % 2 == 0:
        print(list[i])
