import matplotlib.pyplot as plt

input=[i for i in range(1,6)]
squares=[i**2 for i in range(1,6)]

plt.plot(input,squares,linewidth=3) # marks of x,y value as continues plot

plt.scatter(input,squares,s=100) # marks of x,y value as doted plot
plt.show()

