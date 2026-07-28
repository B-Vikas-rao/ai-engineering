def decorator(function):
    def wrapper():
        print("Before Function")
        function()
        print("After Function")
    return wrapper

@decorator
def greet():
    print("Hello!")

greet()