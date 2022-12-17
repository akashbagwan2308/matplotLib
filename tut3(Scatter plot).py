# Scatter plot

from matplotlib import pyplot as plt
x = [10,20,30,40,50,60,70,80,90]
y = [9,8,7,6,5,4,3,2,1]
z = [1,2,3,4,5,6,7,8,9]

# simple scatter plot
plt.scatter(x,y)
plt.show()

# plot with extra parameters
plt.scatter(x,y,marker="*",c="red",s=100)
# plt.bar(x,y)
# plt.plot(x,y,color ="pink")
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# some extra
plt.scatter(x,y,marker="*",c="red",s=100)
plt.scatter(x,z,marker=".",c="black",s=100)
# plt.bar(x,z)
# plt.plot(x,y,color ="pink")
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# subplots
plt.subplot(1,2,1)
plt.scatter(x,y,marker="*",c="red",s=100)
plt.scatter(x,z,marker=".",c="black",s=100)
plt.title("Scatter Plot 1")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.subplot(1,2,2)
plt.scatter(x,y,marker=".",c="black",s=100)
plt.scatter(x,z,marker="*",c="red",s=100)
plt.title("Scatter Plot 2")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
