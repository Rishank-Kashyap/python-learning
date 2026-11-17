x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)       # local
    inner()
    print(x)           # enclosing

outer()
print(x)               # global


count = 0

def show():
    print(count)  # reading a global works


def increment_broken():
    count += 1  # assigning makes count LOCAL for the whole function


# increment_broken()
# UnboundLocalError: cannot access local variable 'count'...
# Python sees an assignment, treats count as local, then the read
# inside += finds that local still has no value.

def increment():
    global count  # "count means the global one"
    count += 1


show()       # 0
increment()
show()       # 1