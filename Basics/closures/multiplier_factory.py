def make_multiplier(n):
    def multiply(x):
        return x * n  # only READS n, so no nonlocal needed

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))  # 10
print(triple(5))  # 15


# The trap
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])  # [2, 2, 2]
# All 3 lambdas remember the same variable `i`, not its value.
# They run after the loop has finished, when i == 2.

# Fix: a default argument is evaluated when the lambda is CREATED
funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])  # [0, 1, 2]
