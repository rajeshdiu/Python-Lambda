


from audioop import reverse
from tkinter.tix import Tree


myNames=["Rajesh Das","Tusher Dhali","Kakon Roy","Niloy Paul","Jebul Amin","Aniik Singha"]

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]


data = [("B", 5, "20"), ("A", 1, "5"), ("C", 6, "10")]
data.sort(key=lambda x: x[0])

ids = ['id5', 'id1', 'id2', 'id5', 'id4', 'id3']
ids.sort(key=lambda x: (x[1:]))

print(ids)

myList=[31,43,70,37,68,89,23,90]
myList.sort(reverse=True)

print(myList)

ids = [5, 2, 3, 1, 4]

res = sorted(ids, key=lambda x: x, reverse=False)

print(res)



subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key=lambda x:x[1])
print("\nSorting the List of Tuples:")
print(subject_marks)