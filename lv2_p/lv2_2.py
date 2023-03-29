import numpy as np
from matplotlib import pyplot
from matplotlib import pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)

pyplot.scatter(data[:,0],data[:,3],c='b',s=data[:,5]*10)
pyplot.xlabel('mpg')
pyplot.ylabel('hp')
for x in range(2,32):
    pyplot.text(data[x,0],data[x,3],s=data[x,5], fontsize = 6, verticalalignment = 'bottom',
         horizontalalignment = 'left')


print('Minimalna vrijednost potrošnje: ', min(data[:,0]))
print('Maksimalna vrijednost potrošnje: ',max(data[:,0]))
print('Srednja vrijednost potrošnje: ',sum(data[:,0])/len(data[:,0]))

a=[]
for i, item in enumerate(data[:,1]):
    if item >= 6:
        a.append(data[i,0])

print('Minimalna vrijednost potrošnje (6 cilinadara): ', min(a))
print('Maksimalna vrijednost potrošnje (6 cilinadara): ', max(a))
print('Srednja vrijednost potrošnje (6 cilinadara): ', sum(a)/len(a))

plt.show()

