a=[1,2]
b=[1,2]
c=a
print(a==b) # True: same values in both variables
print(a is b) # False: objects are different
print(a is c) # True: objects are same

x=None
print(x is None) # None is singleton, only NoneType object 
print(x==None) # works here,  but class can override __eq__ to lie
print(type(None)) # it is of NoneType

p=256
q=int("256")
print(p is q) # True: as q is cached object

r=1000
s=int("1000") # outside cache, so a new object is made
print(r is s) # False
print(r==s) # True: always compare numbers with ==