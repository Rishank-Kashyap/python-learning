# original_dict = {}

# for num in range(1, 6):
#     original_dict[num]=num**2
    
original_dict={
    key: key**2
    for key in range(1, 6)
}

print(original_dict)

swapped_dict = {
    value: key
    for key, value in original_dict.items()
}

# for key, value in original_dict.items():
#     swapped_dict[value]=key
    
print(swapped_dict)

# for key, value in original_dict.items():
#     if value<10:
#         del original_dict[key]

original_dict = {
    key: value
    for key, value in original_dict.items()
    if value>=10
}
        
print(original_dict)


names = ["Rishank", "Naman", "Ravi"]
marks = [85, 92, 78]

report={name:mark for name, mark in zip(names, marks)}
print(report)

report2=dict(zip(names, marks))