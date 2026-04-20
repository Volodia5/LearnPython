def digit_sum(n):
    return sum(int(d) for d in str(n))

def digit_count(n):
    return len(str(n))

n = int(input("Введите число: "))

s = digit_sum(n)
c = digit_count(n)

print(f"Сумма: {s}")
print(f"Количество цифр: {c}")
print(f"Разность: {s - c}")
