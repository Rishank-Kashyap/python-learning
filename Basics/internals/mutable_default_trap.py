def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(5)) # [5]
print(add_item(6)) # [5, 6]
print(add_item(7)) # [5, 6, 7]
# so here whats happening is that we are having the same items object getting element added


def  add_item_fixed(item, items=None):
    if items is None:
        items=[] # a fresh list always
    items.append(item)
    return items
    
print(add_item_fixed(2)) # [2]
print(add_item_fixed(8)) # [8]
print(add_item_fixed(9)) # [9]
