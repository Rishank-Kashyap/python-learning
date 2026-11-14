distances = {
    ("Delhi", "Mumbai"): 1400,
    ("Delhi", "Jaipur"): 280,
    ("Delhi", "Bihar"): 1100
}
print(distances[("Delhi", "Bihar")])

# bad = {["Delhi", "Mumbai"]: 1400} 
#list is mutable and keys can't be mutable as kay are made hashcode but we can use tuple as tuples are immutable and can be used to make hashcode