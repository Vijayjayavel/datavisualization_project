# random plot using 'plot' keyword


import matplotlib.pyplot as plt

from randomwalk import RandomWalk


rw=RandomWalk()
rw.fill_walk()
plt.figure(figsize=(10, 6))

point_numbers=list(range(rw.num_points))
plt.plot(rw.x_values,rw.y_values,linewidth=5)

plt.scatter(0,0,c='g',edgecolors='none',s=1000)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c='r',s=1000)

plt.savefig('random_conplt.png')
plt.show()