# custom dice visual

import pygal
from dieclass import Die

die_1=Die()
die_2=Die(8)

results=[]
for result in range(1000):
    result=die_1.roll()+die_2.roll()
    results.append(result)
print(results)

frequencies=[]
for i in range(2,die_1.numb_sides+die_2.numb_sides+1):
    frequency=results.count(i)
    frequencies.append(frequency)
print(frequencies)

hist=pygal.Bar()

hist.title='Result of rolling D6 and D8 for 1000 time'
hist.x_labels=['2','3','4','5','6',',7','8','9','10','11','12','13','14']
hist._x_title='result'
hist._y_title='frequncies of result'

hist.add('d6+d8',frequencies)
hist.render_to_file('dice_visual.svg')

