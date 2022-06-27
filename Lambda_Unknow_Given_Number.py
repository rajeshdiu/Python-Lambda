from unittest import result


def my_function(n):

    myLambda=lambda x:x*n

    return  myLambda

result=my_function(2)

print(result(15))

result=my_function(3)

print(result(15))


result=my_function(4)

print(result(15))


result=my_function(5)

print(result(15))

