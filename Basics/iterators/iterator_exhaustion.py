it = iter([1, 2, 3])
for x in it: print(x)
for x in it: print(x) # nothing: iterator already exhausted

squares = (x*x for x in range(3))
for x in squares: print(x)
for x in squares: print(x) # nothing: a generator is an iterator, so also exhausted

list = range(3)
for n in list: print(n)
for n in list: print(n) # will print again as range is an iterable; each `for` calls iter() and gets a fresh iterator


# Iterable: can be looped over many times (list, str, dict, range).
# Iterator: single-use cursor (iter(x), generators). Once exhausted, it stays empty.