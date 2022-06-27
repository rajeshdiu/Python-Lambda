

from unittest import result


texts = ["php", "w3r", "Python", "abcd", "Java", "aaa","kanak","did"]
print("Orginal list of strings:")
print(texts)

result=list(filter(lambda x: (x=="".join(reversed(x))),texts))
print(result)



listmy=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

listmy.sort(key=lambda x: x[1])
print(listmy)