def cache(func):
    storage = {}

    def wrapper(*args):
        if args not in storage:
            storage[args] = func(*args)
        return storage[args]

    return wrapper

@cache
def slow_add(a, b):
    print(f"считаем {a}+{b}")
    return a + b

print(slow_add(1, 2))
print(slow_add(1, 2))
print(slow_add(3, 4))
