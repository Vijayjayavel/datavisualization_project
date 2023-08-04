#plotting random plot

import matplotlib.pyplot as plt

from randomwalk import RandomWalk


rw=RandomWalk()
rw.fill_walk()
plt.figure(figsize=(10, 6))

point_numbers=list(range(rw.num_points))
plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Reds,edgecolors='none',s=20)

plt.scatter(0,0,c='g',edgecolors='none',s=100)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c='b',s=100)

plt.savefig('random_plot.png')
plt.show()