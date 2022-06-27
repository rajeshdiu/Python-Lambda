Original_list=[2, 4, -6, -9, 11, -12, 14, -5, 17]

print(Original_list)

print(sum(list(filter(lambda x: x<0,Original_list))))
print(sum(list(filter(lambda x: x>0,Original_list))))