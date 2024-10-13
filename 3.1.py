def summa(y,k):
    s=0
    for i in range(-5,6):
        s+=y[k+i]
    return s/11
from pylab import plot,show,xlim
from numpy import loadtxt
data=loadtxt("sunspots.txt",float)
x=data[:,0]
y=data[:,1]
plot(x,y)
for i in range(0,1000):
    y[i]=summa(y,i)
plot(x,y)
xlim(0,1000)
show()