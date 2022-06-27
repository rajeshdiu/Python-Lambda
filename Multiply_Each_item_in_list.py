from unittest import result


nums = [2, 4, 6, 9 , 11]
n = 2
print("Original list: ", nums)
print("Given number: ", n)

result=list(map(lambda x: x*n,nums))

print("Result:",result)

print("Result:",type(result))

myJoin=" ".join(map(str,result))

print(type(myJoin))
print(myJoin)

