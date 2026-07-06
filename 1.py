import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from sympy import symbols,simplify

x = np.array([1,2,3,4,5,6])
y = np.array([1,3,5,8,5,2])
n = len(x)
X = symbols('X')
P = 0
for i in range(n):
    L = 1
    for j in range(n):
        if j != i:
            L = L * (X-x[j]) / (x[i]-x[j])
    P = P + y[i] * L

P_simplified = simplify(P)
print("\n")
print("lagrange interpolation polynomial (degree {}):".format(n-1))
print("\n")
print(P_simplified)
print("\ncoefficients :")
poly_coeffs = [float(P_simplified.coeff(X, k)) for k in range(n)]
for k, coeff in enumerate(poly_coeffs):
    print(f"  x^{k}: {coeff:.6f}")
print("\n")

def lagrange(x_val):
    result = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if j != i:
                L = L * (x_val-x[j]) / (x[i]-x[j])
        result = result + y[i] * L
    return result

cs = CubicSpline(x,y,bc_type='natural')

print("\n")
print("Cubic Spline Coefficients:")
print("[x_i, x_{i+1}]:")
print("S_i(x) = a_i + b_i*(x-x_i) + c_i*(x-x_i)^2 + d_i*(x-x_i)^3")
print("\n")

for i in range(n-1):
    coeffs = cs.c[:,i]
    a_i = coeffs[3]
    b_i = coeffs[2]
    c_i = coeffs[1]
    d_i = coeffs[0]
    print(f"Interval {i+1}: [{x[i]:.1f}, {x[i+1]:.1f}]")
    print(f"  a_{i+1} = {a_i:.6f}")
    print(f"  b_{i+1} = {b_i:.6f}")
    print(f"  c_{i+1} = {c_i:.6f}")
    print(f"  d_{i+1} = {d_i:.6f}")

xx = np.linspace(min(x),max(x),200)
yy_lagrange = np.array([lagrange(xi) for xi in xx])
yy_spline = cs(xx)
plt.figure(figsize=(12,8))
plt.plot(x,y,'ro',markersize=10,label='main points')
plt.plot(xx,yy_lagrange,color="blue",label='lagrange')
plt.plot(xx,yy_spline,'--',label='cubic spline')
plt.xlabel('x',fontsize=12)
plt.ylabel('y',fontsize=12)
plt.title('lagrange vs cubic spline',fontsize=14)
plt.legend(fontsize=11)
plt.grid(True,alpha=0.3)
plt.tight_layout()
plt.show()

print("\n")
print("comparison of values at midpoints:")
print("\n")
test = np.array([1.5,2.5,3.5,4.5,5.5])
print(f"{'x':>8}{'lagrange':>12}{'spline':>12}{'difference':>12}")
print("=================================================")
for i in test:
    yLAG = lagrange(i)
    ySP = cs(i)
    diff = abs(yLAG - ySP)
    print(f"{i:>8.2f}{yLAG:>12.6f}{ySP:>12.6f}{diff:>12.6f}")