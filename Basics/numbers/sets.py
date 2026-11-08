java = {'Ravi', 'Shyam', 'Raju', 'Babu'}
python = {'Jagat', 'Alpha', 'Beta', 'Ravi'}

both = java & python
either = java | python
only_java = java- python
only_python = python - java
exactly_one = java ^ python

print(both)
print(either)
print(only_java)
print(only_python)
print(exactly_one)