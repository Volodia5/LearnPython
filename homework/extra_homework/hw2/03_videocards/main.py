n = int(input("Количество видеокарт: "))
cards = []
for i in range(n):
    cards.append(int(input(f"{i + 1} видеокарта: ")))

max_card = max(cards)
print(f"Старыt видеокартs: [ {' '.join(str(c) for c in cards)} ]")

cards = [c for c in cards if c != max_card]
print(f"Новыt видеокартs: [ {' '.join(str(c) for c in cards)} ]")
