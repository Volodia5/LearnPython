def bread(func):
    def wrapper():
        print("Bread")
        func()
        print("Bread")
    return wrapper

def meat(func):
    def wrapper():
        func()
        print("Meat")
    return wrapper

def tomato(func):
    def wrapper():
        func()
        print("Tomato")
    return wrapper

def salat(func):
    def wrapper():
        func()
        print("Salat")
    return wrapper

@bread
@salat
@tomato
@meat
def make_sandwich():
    pass

make_sandwich()
