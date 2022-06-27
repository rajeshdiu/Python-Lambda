nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
print("Orginal list:")
print(nums)
result = list(filter(lambda x: (x%19==0 or x%13==0),nums))
print(result)