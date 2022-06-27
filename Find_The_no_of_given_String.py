from unittest import result


str1 = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
print("Original string: ",str1)
str_num=[i for i in str1.split(" ")]
print(str_num)

length=len(str_num)
print(length)

myDigit= [int(x) for x in str_num if x.isdigit()]

print(sorted(myDigit))

result2=filter(lambda x: x>length,myDigit)

for i in result2:
    print(i,end=" "+"\n")

txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x,end=" ")

txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 4)

print(x)