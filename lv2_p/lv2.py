import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 3, 1])
y = np.array([1, 2, 2, 1, 1])

plt.plot(x, y, 'red', linewidth=1, marker=".", markersize=5, markerfacecolor='y')
plt.axis([0,5,0,5])
plt.xlabel('x os')
plt.ylabel('y os')
plt.title('prvi primjer')
plt.show()