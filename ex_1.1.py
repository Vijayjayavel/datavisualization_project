# ploting cubes values

import matplotlib.pyplot as plt

integers=[i for i in range(1,6)]

cubes=[i**3 for i in integers]

plt.plot(integers,cubes)

plt.scatter(integers,cubes,s=100)

plt.show()