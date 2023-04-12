import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv')

plt.figure()
mtcars.groupby(['cyl']).mean().plot.bar(y='mpg',stacked=True)
plt.show()

mtcars.boxplot(by='cyl', column=['wt'])
plt.show()

manual = mtcars[mtcars['am'] == 0]['mpg']
automatic = mtcars[mtcars['am'] == 1]['mpg']

plt.hist(manual, alpha=0.5, label='Manual')
plt.hist(automatic, alpha=0.5, label='Automatic')
plt.legend(loc='upper right')
plt.xlabel('MPG')
plt.ylabel('Frekvencija')
plt.show()

manual2 = mtcars[mtcars['am'] == 0]
automatic2 = mtcars[mtcars['am'] == 1]

plt.scatter(manual2['hp'], manual2['qsec'], c='blue', label='Manual')
plt.scatter(automatic2['hp'], automatic2['qsec'], c='orange', label='Automatic')
plt.legend(loc='upper left')
plt.xlabel('Horsepower')
plt.ylabel('Quarter Mile Time (s)')
plt.show()

