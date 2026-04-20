word = input("Введите слово: ")
if word == word[::-1]:
    print("Слово - палиндромом")
else:
    print("Слово - не палиндромом")
