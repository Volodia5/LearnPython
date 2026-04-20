def bread(func):
    def wrapper():
        return "Bread\n" + func() + "Bread"
    return wrapper

def meat(func):
    def wrapper():
        return func() + "Meat\n"
    return wrapper

def tomato(func):
    def wrapper():
        return func() + "Tomato\n"
    return wrapper

def salat(func):
    def wrapper():
        return func() + "Salat\n"
    return wrapper

@bread
@salat
@tomato
@meat
def make_sandwich():
    return ""

print(make_sandwich())
