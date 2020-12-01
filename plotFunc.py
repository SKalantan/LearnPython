from pylab import *
import matplotlib.pyplot as plt

x = linspace(-5,5,1000)
h = 0.001
f = exp(-x**2) # function
df = zeros(1000,float) # array of zeros
for i in range(1000): # derivative
    df[i] = (exp(-(x[i]+h)**2)-exp(-(x[i]-h)**2))/(2*h)

fig, (ax1, ax2) = plt.subplots(2)

ax1.plot(x,f) # plot function
ax1.set_ylabel('f(x)')
ax2.plot(x,df) # plot derivative
ax2.set_xlabel('x')
ax2.set_ylabel('df(x)/dx')

plt.show()
