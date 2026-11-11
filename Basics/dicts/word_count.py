from collections import Counter

text = "the cat and the dog and the bird"

words = text.split()

counts={}

counts2={}

for word in words:
    if word in counts:
        counts[word] = counts[word]+1
    else:
        counts[word]=1

print(counts)
        
for word in words: 
    counts2[word] = counts2.get(word, 0)+1
        
print(counts2)

counts3=Counter(words)
print(counts3)
print(counts3.most_common(3))