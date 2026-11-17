def make_counter():
    count = 0

    def counter():
        nonlocal count  # "count means the ENCLOSING one"
        count += 1
        return count

    return counter  # return the function, not counter()


c1 = make_counter()
c2 = make_counter()
print(c1())  # 1
print(c1())  # 2
print(c1())  # 3
print(c2())  # 1   ← c2 has its OWN count


# global jumps to the module level.
# nonlocal goes to the nearest enclosing function.