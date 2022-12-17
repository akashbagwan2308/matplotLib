# Histogram
from matplotlib import pyplot as plt

data = [1,3,3,3,3,9,9,5,4,4,8,8,8,6,7]

# simple histogram
plt.hist(data)
plt.show()

# histogram with labels
plt.hist(data,color='r')
plt.title("Histogram")
plt.ylabel("frequency")
plt.xlabel("Data")
# plt.grid()
plt.show()

# ###Working with datasets
# import pandas as pd
# iris = pd.read_csv('iris.csv')
# iris.head()
#
# plt.hist(iris['Petal.Length'],bins=50,color='yellow')
# plt.show()

