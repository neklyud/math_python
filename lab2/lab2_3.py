import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, sin, cos, abs, e

# ---------------------

def f1(x):
    return 5 + 4 * cos(2 * x) + 2 * sin(3 * x) - cos(4 * x)

def f2(x):
    return abs(x)

def f3(x):
    if x >= -pi and x < 0:
        return -1
    if x >= 0 and x <= pi:
        return 1
    return 0

def fft_coeff(k, y_nodes):
    n = len(y_nodes)
    if (n == 2):
        A = y_nodes[0] + y_nodes[1] * ((-1) ** k)
        return A
    even = y_nodes[0:n:2]
    odd = y_nodes[1:n:2]
    Ek = fft_coeff(k, even)
    Ok = fft_coeff(k, odd)
    cf = ((-1j) * k * pi * 2) / n
    Ak = Ek + (e ** cf) * Ok
    return Ak    

def trigonometric_interpolant(x, coeffs):
    n = len(coeffs)
    res = np.real(coeffs[0])
    for i in range(1,n-1):
        res += 2 * np.real(coeffs[i]) * cos(i * x) - 2 * np.imag(coeffs[i]) * sin(i * x)
    res += np.real(coeffs[n - 1]) * cos((n - 1) * x)
    return res

# ---------------------

m = 2 ** 8
x = np.arange(-pi, pi, pi / m)
y1 = [f1(i) for i in x]
y2 = [f2(i) for i in x]
y3 = [f3(i) for i in x]
x = np.arange(0, m + 1, 1)
coeffs1 = [fft_coeff(i,y1) * (((-1) ** i) / (2 * m)) for i in x]
coeffs2 = [fft_coeff(i,y2) * (((-1) ** i) / (2 * m)) for i in x]
coeffs3 = [fft_coeff(i,y3) * (((-1) ** i) / (2 * m)) for i in x]

yReal = [2 * np.real(coeffs1[i]) for i in x]
yReal[0] /= 2
yReal[-1] /= 2
yImage = [-2 * np.imag(coeffs1[i]) for i in x]

xInter = np.linspace(-pi, pi, 200)
y2Origin = [f2(i) for i in xInter]
y2Inter = [trigonometric_interpolant(i, coeffs2) for i in xInter]
y3Origin = [f3(i) for i in xInter]
y3Inter = [trigonometric_interpolant(i, coeffs3) for i in xInter]

# ---------------------

fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(12, 7))
axes[0].plot(x, yReal)
axes[0].grid()
axes[0].set_xlabel('k')
axes[0].set_ylabel('2|a_k|')

axes[1].plot(x,yImage)
axes[1].grid()
axes[1].set_xlabel('k')
axes[1].set_ylabel('2|a_k|')

fig.tight_layout() 
plt.show()


fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(12, 7))


axes[0].plot(xInter, y2Origin)
axes[0].plot(xInter, y2Inter, 'r')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[0].grid()

axes[1].plot(xInter, y3Origin)
axes[1].plot(xInter, y3Inter, 'r')
axes[1].set_xlabel('x')
axes[1].set_ylabel('y')
axes[1].grid()

fig.tight_layout() 
plt.show()