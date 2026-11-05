a=[1,2,3]
b=a # now both pointing to same object
b.append(4)
print(id(a), a)
print(id(b), b)

b=[1, 2, 3] # different object now for b
a.append(5)
print(id(a), a)
print(id(b), b)


x=10
y=x # both pointing to same object
y+=1 # now integers are immutable so x and y will point to different objects
print(id(x), x) # pointing to same previous object so x=10
print(id(y), y) # pointing to new object so y=11