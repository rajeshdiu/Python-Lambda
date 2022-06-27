mystring=[1, 2, 3, 5, 7, 8, 9, 10]
print("Original String")
print(mystring)

odd=list(filter(lambda x: (x%2 != 0) , mystring))

print("Odd list is")
print(odd)

even=list(filter(lambda x: (x%2 == 0) , mystring))

print("Even list is")
print(even)