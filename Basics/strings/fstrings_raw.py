import math

x=math.pi
name="Rishank"
big=1234567

print(f"{x:.2f} is pi value") # 3.14: 2 decimal places
print(f"{big:,}") # 1,234,567: thousands separators
print(f"[{name:>10}]") # [   Rishank]: right-aligned in 10 chars (< left, ^ center)
print(f"{x=}") # x=3.141592653589793: handy for debugging
print(f"{x=:.3f}") # x = 3.142: combine both

print("C:\\new\\test") # escape each backslash
print(r"C:\new\test") # raw string: backslashes are kept as-is