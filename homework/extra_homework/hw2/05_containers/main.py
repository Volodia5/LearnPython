n = int(input("Количество контейнеров: "))
containers = []
for _ in range(n):
    w = int(input("Введите вес: "))
    while w > 200:
        w = int(input("Введите вес: "))
    containers.append(w)

x = int(input("\nВведите вес нового контейнера: "))
while x > 200:
    x = int(input("Введите вес нового контейнера: "))

pos = next((i for i, c in enumerate(containers) if c < x), len(containers))
print(f"\nНомер: {pos + 1}")
