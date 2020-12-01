from pylab import *
import matplotlib.pyplot as plt

x = linspace(0,10,1000)
a = 1.0
f = x**2*exp(-a*x)*sin(pi*x)
plt.plot(x,f)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
