def even_generator(limit):
    yield from range(2, limit + 1, 2)


for num in even_generator(10):
    print(num)
