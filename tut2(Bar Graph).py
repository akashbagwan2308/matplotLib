# Matplotlib ---- Bar Graphs
from matplotlib import pyplot as plt
import numpy as np

student = {"Bob": 87,"Matt":56,"Sam":27}
names = list(student.keys())
values = list(student.values())

#  simple bar plot
plt.bar(names,values)
plt.show()

# bar plot with title and labels

plt.bar(names,values)
plt.title("Bar Plot")
plt.xlabel("Names")
plt.ylabel("Marks")
plt.show()

#  Horizontal Bar plot

plt.barh(names,values,color = "green")
plt.title("Bar Plot")
plt.xlabel("Marks")
plt.ylabel("Names")
plt.grid(True)
plt.show()

