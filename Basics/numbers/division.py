import math

print(7//2) # it is math.floor(a/b)
print(-7//2) 
print(7%3) # a%b=a-b.[a/b]
print(-7%3)
print(7/2) # divide
print(2**10) # power of  a number
print(divmod(17, 5)) # will giv (quotient, remainder)

print(0.1+0.2) # binary floats can't store 0.1 exactly
print(0.1+0.2==0.3) # False: java doubles behaves the same
print(math.isclose(0.1+0.2, 0.3)) # True: compare floats with tolerance