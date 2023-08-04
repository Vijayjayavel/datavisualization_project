import matplotlib.pyplot as plt

squares=[i**2 for i in range(9)]
plt.plot([i for i in range(9)],squares,linewidth=5)


plt.title("Square numbers",fontsize=20)
plt.xlabel('integer',fontsize=10)
plt.ylabel('integer',fontsize=10)

plt.tick_params(axis='both',labelsize=10) # to set the label size of x and y axis

plt.show()