from collections import defaultdict

group = ["apple", "avocado", "banana", "blueberry", "cherry"]

answer = {}
for item in group:
    if item[0] not in answer:
        answer[item[0]]=[item]
    else:
        answer[item[0]].append(item)
    
print(answer)

answer2={}
for item in group:
    answer2.setdefault(item[0], []).append(item)
print(answer2)

# defaultdict — a missing key automatically gets list()
answer3=defaultdict(list)
for item in group:
    answer3[item[0]].append(item)
    
print(dict(answer3))
