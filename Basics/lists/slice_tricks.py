nums = list(range(1, 11))

print(nums)

print(nums[::2])

print(nums[-3:])

print(nums[::-1])

nums[2:5] = [0,0]
print(nums)

del nums[::2]
print(nums)