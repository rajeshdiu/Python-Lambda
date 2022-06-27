nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)


squareof=list(map(lambda x:x**2,nums))

print("Square list of integers:")
print(squareof)

CubeOf=list(map(lambda x:x**3,nums))

print("Cube list of integers:")
print(CubeOf)