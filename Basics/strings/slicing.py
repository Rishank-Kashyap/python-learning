s = "Python Programming"

first_six = s[:6]
print(first_six)

last_four = s[-4:]
print(last_four)

rev_text = s[::-1]
print(rev_text)

print(s[::2])

words = s.split()
reversed_word = words[::-1]
reversed_sentence = " ".join(reversed_word)
print(reversed_sentence)
