# colors to cubes plot

import matplotlib.pyplot as plt

integers=[i for i in range(1,6)]

cubes=[i**3 for i in integers]

plt.plot(integers,cubes,c='g')

plt.scatter(integers,cubes,c='r',cmap=plt.cm.Reds,s=100)

plt.show()