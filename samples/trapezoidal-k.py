from pylab import *
from numpy import *

def f(x):
    return x**4 - 2*x + 1

a  = 0.0
b  = 2.0
x  = []
y  = []
fxi= []
xi = []
xmin= 10
xmax= 200
xint= 10
x0= [0,xmax]
y0= [4.4,4.4]

s0 = (f(a) + f(b))*0.5
for N in arange(xmin,xmax+xint,xint):
   s = 0.00
   dx = (b-a)/N
   for k in range(1,N):
      fk = f(a+k*dx)
      s += fk
   s = (s0 + s)*dx
   x.append(N)
   y.append(s)
   print(N,s)

dx = (b-a)/xmax
for k in arange(a,b+dx,dx):
    fxi.append(f(k))
    xi.append(k)

subplots_adjust(hspace=0.3,wspace=0.2)
subplot(2,1,1)
plot(xi,fxi,color='black',linewidth=2)
xlabel("x",fontsize=10)
ylabel(r'$f(x)(x^4 -2x + 1)$',fontsize=10)
grid(True)
xlim(a,b)

subplot(2,1,2)
scatter(x,y)
plot(x0,y0, color='black')
suptitle(r'$\int_{0}^{2} f(x) dx = 4.4$',fontsize=12)
xlabel("N intervalos",fontsize=12)
ylabel("Intregral por trapézio de f(x)",fontsize=12)
xlim(xmin,xmax)
show()


