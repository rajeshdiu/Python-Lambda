sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']

sample_names2=list(filter(lambda x: x[0].isupper() and x[1:].islower(),sample_names))

myJoin=len(''.join(sample_names2))

print(myJoin)