nums = [1,2,3,4,5,6]

it=iter(nums)
while True:
    try:
        print(next(it))
    except StopIteration:
        break
        

# for x in items: runs the iterator till StopIteration
# iter(nums) is an iterator that one can iterate
# iterable nums is something that is iterated