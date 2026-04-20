import json
import os

def cache(filename, use_kwargs=False):
    def decorator(func):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                storage = json.load(f)
        else:
            storage = {}

        def wrapper(*args, **kwargs):
            if use_kwargs:
                key = str(sorted(kwargs.items()))
            else:
                key = str(args)

            if key not in storage:
                storage[key] = func(*args, **kwargs)
                with open(filename, "w") as f:
                    json.dump(storage, f)

            return storage[key]

        return wrapper
    return decorator

@cache("cache.json", use_kwargs=False)
def slow_multiply(a, b):
    print(f"вычисляем {a}*{b}")
    return a * b

print(slow_multiply(3, 4))
print(slow_multiply(3, 4))
print(slow_multiply(5, 6))
