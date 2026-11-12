class Countdown:
    def __init__(self, n):
        self.current = n

    def __iter__(self):
        return self # the object is its own iterator

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # signals the end, like hasNext() == false
        value = self.current
        self.current -= 1
        return value

for num in Countdown(3):   # you loop over it, you don't print it
    print(num)             # 3 2 1



def countdown(n):
    while n>0:
        yield n
        n-=1
        
for num in countdown(3): print(num)
for num in countdown(3): print(num)

# Class: ~10 lines (__init__, __iter__, __next__, manual StopIteration).
# Generator: 4 lines. `yield` creates __iter__/__next__ and raises
# StopIteration automatically when the function returns.