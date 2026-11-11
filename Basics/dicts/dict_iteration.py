dictionary = {"Rishank": 85, "Naman": 92, "Ravi": 78}

for key, value in dictionary.items(): print(key, value)

# max_marks=0
# topper=""
# for key, value in dictionary.items():
#     if value>max_marks: topper = key
#     max_marks=max(max_marks, value)
      
# print(topper)
# print(max_marks)

topper=max(dictionary, key=dictionary.get)
print(topper, dictionary[topper])

sorted_by_marks=sorted(dictionary, key=dictionary.get, reverse=True)

print(sorted_by_marks)