
array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
array_nums2 = [1, 2, 4, 8, 9]
array_nums3 = [1, 3, 5, 4, 8, 9]


print("Original arrays:")
print(array_nums1)
print(array_nums2)

result=list((filter(lambda x: x in array_nums3,array_nums1)))
print(result)