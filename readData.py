import numpy as np
import matplotlib.pyplot as plt

run100m = np.loadtxt("run100m.d")

t = run100m[:,0] # array of all rows, first column
x = run100m[:,1] # array of all rows, second column

plt.plot(t,x)
plt.xlabel('t')
plt.ylabel('x')
plt.show()
