def min_divisor(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return i

n = int(input("Введите число: "))
print(f"Наименьший делитель: {min_divisor(n)}")
