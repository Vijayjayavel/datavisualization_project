import matplotlib.pyplot as plt

x_values=[i for i in range(1,10)]
y_values=[i**2 for i in x_values]

plt.scatter(x_values,y_values,c=x_values,edgecolors='none',cmap=plt.cm.Reds,s=200)
plt.axis([0,10,0,100])

plt.savefig('squares_plot.png',bbox_inches='tight')
plt.show()


#bbox_inches helps to save fig only not the extra white spaceb