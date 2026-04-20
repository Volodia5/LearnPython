lst = [1, 4, -3, 0, 10]
print(f"старый список: {lst}")

for i in range(1, len(lst)):
    j = i
    while j > 0 and lst[j - 1] > lst[j]:
        lst[j - 1], lst[j] = lst[j], lst[j - 1]
        j -= 1

print(f"сортированый список: {lst}")
