films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
favorites = []

count = int(input("Сколько фильмов хотите добавить? "))
for _ in range(count):
    film = input("Введите название: ")
    if film in films:
        favorites.append(film)
    else:
        print(f"фильма {film} нет :(")

print(f"список любимых фильмов: {', '.join(favorites)}")
