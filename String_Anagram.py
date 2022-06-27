from collections import Counter
from unittest import result

from matplotlib.pyplot import text

texts = ["bcda", "abce", "cbda", "cbea", "adcb"]

str="abcd"

result=list(filter(lambda x: (Counter(str)==Counter(x)),texts))
print(result)