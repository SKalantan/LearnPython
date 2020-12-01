import numpy as np
import matplotlib.pyplot as plt

m = np.array([1.0,2.0,4.0,6.0,9.0,11.0])
V = np.array([0.13,0.26,0.50,0.77,1.15,1.36])

print(m[0]) # Print first element in array m
print(m[3]) # Print forth element in array m

print(V[0]) # Print first element in array V
print(V[3]) # Print forth element in array V

plt.plot(m,V,'o')
plt.xlabel('m (kg)')
plt.ylabel('V (l)')
plt.show()
