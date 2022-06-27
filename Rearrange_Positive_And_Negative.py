from unittest import result


array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
print("Original arrays:")
print(array_nums)

res = sorted(array_nums, key=lambda x: 0 if x == 0 else -1 / x)
print(res)

