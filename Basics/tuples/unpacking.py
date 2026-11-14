x=1
y=2
x,y=y,x

print(x)
print(y)

list=[1, 2, 3, 4, 5]
(first, *middle, last)=list
print(first)
print(middle)
print(last)

items=[("Rishank", 25), ("Naman", 24)]
for name, age in items:
    print(name,  age)
    

def min_max(nums):
    return  min(nums), max(nums)

smallest, largest = min_max([4, 9, 1, 7])
print(smallest, largest)
