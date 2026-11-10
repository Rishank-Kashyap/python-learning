nums=list(range(1, 11))

squares = [num**2 for num in nums]
print(squares)

print([num for num in squares if num%2==0])

print(["even" if n%2==0 else "odd" for n in nums])

nested = [[1, 2], [3, 4], [5]]
print([item for sublist in nested for item in sublist])

print([(x, y) for x in range(1, 4) for y in range(1, 4) if x!=y])