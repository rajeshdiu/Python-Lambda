myDict=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

print("Original String is")
print(myDict)
myDict.sort(key=lambda x: x["color"])

print("After sorting color")
print(myDict)