# Matplotlib Tuts

import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1,11)
print(x)
y = 2*x*x
Y= 3*x*x
z =4*x*x
print(y)
print(Y)
print(z)
#   Simple plot

plt.plot(x,y)
plt.show()

 # Plot with title and axis

plt.plot(x,y)
plt.title("First line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

 # plot with color and linestyle

plt.plot(x,y,color = 'g',linestyle = ':',linewidth = 2)
plt.title("First line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

# Plot two/multiple graphs in same plane

plt.plot(x,y,color = 'g',linestyle = ':',linewidth = 2)
plt.plot(x,Y,color = 'red',linestyle = '--',linewidth = 2)
plt.plot(x,z,color = 'blue',linestyle = '-.',linewidth = 2)
plt.title("First line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

 # Plot with grid

plt.plot(x,y,color = 'g',linestyle = ':',linewidth = 2)
plt.plot(x,Y,color = 'red',linestyle = '--',linewidth = 2)
plt.plot(x,z,color = 'blue',linestyle = '-.',linewidth = 2)
plt.title("First line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)   # to show grid
plt.show()

 # Sub plots of row 1 ,column 2
plt.subplot(1,2,1)
plt.plot(x,y,color = 'g',linestyle = '-',linewidth = 2)
plt.title("First line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.subplot(1,2,2)
plt.plot(x,Y,color = 'red',linestyle = '-.',linewidth = 2)
plt.title("Second line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()

 # Sub plots of row 2 ,column 1
plt.subplot(2,1,1)
plt.plot(x,y,color = 'g',linestyle = '-',linewidth = 2)
plt.title("First line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.subplot(2,1,2)
plt.plot(x,Y,color = 'red',linestyle = '-.',linewidth = 2)
plt.title("Second line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()

 # Sub plots of row 2 ,column 2
plt.subplot(2,2,1)
plt.plot(x,y,color = 'g',linestyle = '-',linewidth = 2)
plt.title("First line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.subplot(2,2,2)
plt.plot(x,Y,color = 'red',linestyle = '-.',linewidth = 2)
plt.title("Second line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.subplot(2,2,3)
plt.plot(x,y,color = 'g',linestyle = '-',linewidth = 2)
plt.title("First line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.subplot(2,2,4)
plt.plot(x,Y,color = 'red',linestyle = '-.',linewidth = 2)
plt.title("Second line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()


