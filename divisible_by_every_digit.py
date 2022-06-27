from unittest import result


mylist=[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

print(list)


result = list(filter(lambda x: (x%x==0),mylist))

print(result)