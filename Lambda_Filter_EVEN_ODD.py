nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nEven numbers from the said list:")

evenNum=list(filter(lambda x:(x%2==0),nums))

print(evenNum)

print("\nOdd numbers from the said list:")

OddNum=list(filter(lambda x:(x%2!=0),nums))


print(OddNum)