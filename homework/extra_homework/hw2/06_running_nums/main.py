lst = [1, 2, 3, 4, 5]
k = int(input("сдвиг: "))
k = k % len(lst)
print(f"старый список: {lst}")
lst[:] = lst[-k:] + lst[:-k]
print(f"новый список: {lst}")
