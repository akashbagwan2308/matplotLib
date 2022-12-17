# box plot
import pylab as pl
from matplotlib import pyplot as plt
one = [ 1,2,3,4,5,6,7,8,9]
two = [1,2,3,4,5,4,3,2,1]
three = [5,6,6,8,9,6,5,9,2,6,5]

data = list([one,two,three])

# box plot
plt.boxplot(data)
plt.show()
# violin plot
plt.violinplot(data,showmedians=True)
plt.show()
# Pie- chart
fruit = ['Apple','Orange','Mango','Guava']
quantity = [67,34,100,29]

plt.pie(quantity,labels=fruit)
pl.show()

plt.pie(quantity,labels=fruit,autopct='%0.1f%%',colors=['yellow','grey','blue','pink'])
plt.show()

# DoughNut-Chart
plt.pie(quantity,labels=fruit,radius=2)
plt.pie([1],colors=['w'],radius=1)
plt.show()

