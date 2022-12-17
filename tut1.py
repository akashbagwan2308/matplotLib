# Matplotlib Tuts

import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1,11)
print(x)
y = 2*x*x
Y= 3*x*x
z =4*x*x
print(y)
#   Simple plot

# plt.plot(x,y)
# plt.show()

#  Plot with title and axis

# plt.plot(x,y)
# plt.title("First line plot")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()

#  plot with color and linestyle

# plt.plot(x,y,color = 'g',linestyle = ':',linewidth = 2)
# plt.title("First line plot")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.show()

# Plot two/multiple graphs in same plane

plt.plot(x,y,color = 'g',linestyle = ':',linewidth = 2)
plt.plot(x,Y,color = 'red',linestyle = '--',linewidth = 2)
plt.plot(x,z,color = 'blue',linestyle = '-.',linewidth = 2)
plt.title("First line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()