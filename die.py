import pygal
from dieclass import Die

die=Die()

results=[die.roll() for i in range(1000)]
print(results)

freqencies=[results.count(value) for value in range(1,die.numb_sides+1)]
print(freqencies)

hist=pygal.Bar()

hist.title='Result of rolling one d6 1000 times.'
hist.x_labels=['1','2','3','4','5','6']
hist.x_title='Result'
hist.y_title='Frequecies of the result'

hist.add('d6',freqencies)
hist.render_to_file('Die_visual.svg')
