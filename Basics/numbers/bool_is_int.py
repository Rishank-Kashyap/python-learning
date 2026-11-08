print(True+True) # bool is  a subclass of int
print(sum([True, False, True])) # built in sum function
print(isinstance(True,  int)) # True

numbers = [10, 12, 15, 5, 7, 56]
count = sum(n>10 for n in numbers) # each comparison True/False i.e. 0/1
print(count)