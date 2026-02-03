# def sample_decorator(func):
#     def wrapper():
#         print("before the function is called: ")
#         func()
#         print("after the function is called")

#     return wrapper

# @sample_decorator
# def say_hello():
#     print("hello, world")
# @sample_decorator
# def bye():
#     print("bye")
# bye()
# say_hello()



# def smart_division(func):
#     def inner(a, b):
#         print("We are dividing", a, "by", b)
#         if b == 0:
#             print("Invalid operation: division by zero is undefined")
#             return
#         else:
#             return func(a, b)
#     return inner

# @smart_division
# def division(a, b):
#     return a / b


# print(division(20, 2))
# print(division(20, 0))


# def smart_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Function arguments:", args, kwargs)
#         result = func(*args, **kwargs)
#         print("Function executed successfully.")
#         return result
#     return wrapper

# @smart_decorator
# def greet_person(name, age):
#     print(f"Hello {name}, you are {age} years old.")

# greet_person("Emma", 28)

# greet_person(name='avi', age=00)

def bold_decorator(func):
    def wrapper():
        return f"{func()}"
    return wrapper

def italic_decorator(func):
    def wrapper():
        return f"{func()}"
    return wrapper

@bold_decorator
@italic_decorator
def formatted_text():
    return "Decorators are powerful!"

print(formatted_text())


def fun1(*n,**m):
    print(n,m)

fun1(1,2,3,b="hello")