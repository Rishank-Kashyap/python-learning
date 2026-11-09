text = " hello, WORLD. welcome to python "

print(text.strip())

print(text.title())

words = text.split()
print(words)

print(text.strip().startswith("hello"))

print("".join(words))

print(text.replace("WORLD", "Python"))
print(text)

print(text.find("hello"))
print(text.count("e"))

info = "name=Rishank;age=25;city=Delhi"
items = info.split(";")
print(items)
person = dict(pair.split("=") for pair in info.split(";"))
print(person)