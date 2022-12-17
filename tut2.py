# Matplotlib ---- Bar Graphs
from matplotlib import pyplot as plt
import numpy as np

student = {"Bob": 87,"Matt":56,"Sam":27}
names = list(student.keys())
values = list(student.values())

plt.bar(names,values)
plt.show()