import copy

original = [[1, 2], [3, 4]]
shallow = original.copy() # new outer list, same inner list
deep = copy.deepcopy(original) # new outer and inner list

original.append([2, 3, 4]) # changes original's outer list
original[0].append(3) # changes inner list that shallow shares

print(original) # [[1, 2, 3], [3, 4], [2, 3, 4]]
print(shallow) # [[1, 2, 3], [3, 4]]
print(deep) # [[1, 2], [3, 4]]

print(original[0] is shallow[0]) # True: same inner list
print(original[0] is deep[0]) # False: a copy