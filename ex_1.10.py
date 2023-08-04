# ploting dice roll using matplotlib

import matplotlib.pyplot as plt

from dieclass import Die

die_1=Die(9)
die_2=Die(9)

results=[]
for result in range(100):
    result=die_1.roll()+die_2.roll()
    results.append(result)
print(results)

frequencies=[]
for i in range(2,die_1.numb_sides+die_2.numb_sides+1):
    frequency=results.count(i)
    frequencies.append(frequency)
print(frequencies)

plt.bar(results,frequencies,color='maroon',width=0.4)

plt.show()

