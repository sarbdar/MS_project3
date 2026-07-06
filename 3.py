import numpy as np

exact = np.exp(1)-1
head = 0
tail = 1
n = 10
h = (tail - head) / n
x = np.linspace(head,tail,n+1)
y = np.exp(x)
trap = h * ((y[0]+y[n]) / 2+np.sum(y[1:n]))
simpson = h/3 * (y[0]+ y[n]+ 4*np.sum(y[1:n:2])+ 2*np.sum(y[2:n-1:2]))
t = np.array([-1/np.sqrt(3),1/np.sqrt(3)])
w = np.array([1,1])
xg = (tail-head) / 2*t + (head+tail)/2
gauss = (tail-head) / 2*np.sum(w*np.exp(xg))
print("exactValue   =",exact)
print("zozangei     =",trap)
print("Simpson      =",simpson)
print("Gaussian     =",gauss)
print("\n")
print("zozangeError =",abs(exact-trap))
print("SimpsonError =",abs(exact-simpson))
print("GaussianError=",abs(exact-gauss))