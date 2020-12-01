from pylab import *
import matplotlib.pyplot as plt

x0, x1, dx = 0.0, 10.0, 1 # start, end, step
n = int(ceil((x1-x0)/dx) + 1) # n has to be an integer
x = zeros((n,1),float)
y = zeros((n,1),float)
for i in range(n):
    x[i] = x0 + i*dx
    y[i] = sin(x[i])

xx = linspace(0,10,1000) # this is equivalent to previous lines
yy = sin(xx)

plt.plot(x,y) # line plot
plt.plot(xx,yy,':') # dotted line plot
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()
