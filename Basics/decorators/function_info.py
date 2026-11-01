def function_info(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        print(f"Number of args for {func.__name__} is {args_value} and {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@function_info
def summation(a, b):
    return a+b

summation(2,3)

@function_info
def greet(name, greeting="Hello!"):
    print(f"{greeting}, {name}")
    
greet("Rishank", greeting="Hii!")