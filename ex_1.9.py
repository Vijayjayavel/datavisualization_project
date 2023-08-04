# two dice multiplication

import pygal
from dieclass import Die

die_1=Die(5)
die_2=Die(5)

results=[]
for result in range(1000):
    result=die_1.roll()*die_2.roll()
    results.append(result)
print(results)

frequencies=[]
for i in range(2,die_1.numb_sides*die_2.numb_sides+1):
    frequency=results.count(i)
    frequencies.append(frequency)
print(frequencies)

hist=pygal.Bar()

hist.title=f'Result of rolling D{die_1.numb_sides}*D{die_2.numb_sides} for {len(results)} time'
hist.x_labels=[str(x) for x in range(2,die_1.numb_sides*die_2.numb_sides+1)]
hist._x_title='result'
hist._y_title='frequncies of result'

hist.add(f'd{die_1.numb_sides}*d{die_2.numb_sides}',frequencies)
hist.render_to_file('ex_1.9.svg')

