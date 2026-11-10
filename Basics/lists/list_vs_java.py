list_input=["Cat", "Dog", "Horse", "Elephant", "Bee", "Zebra"]

print([word.upper() for word in list_input if len(word)>3])

words_by_length = sorted(list_input, key=lambda w: (len(w), w), reverse=True)
print(words_by_length)