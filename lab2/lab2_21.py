import numpy as np
import matplotlib
import matplotlib.pyplot as plt
func = lambda x: x*x*np.sin(3*x)

def composite_simpson(a,b,n,f):
    h=(b-a)/n
    f1=0
    f2=0
    for i in range(1,n):
        if i%2==0:
            f1+=f(a+i*h)
        else:
            f2+=f(a+i*h)
    return h/3*(f(a)+2*f1+4*f2+f(b))

n = np.arange(3, 9999, 100)
s = (9 * np.pi ** 2 - 4) / 27
eS = [abs(s - composite_simpson(0, np.pi, i+1, func)) for i in n]
h = np.pi / (n + 1)

# ---------------------

fig, axes = plt.subplots(nrows = 1, ncols = 1, figsize = (6,6))

axes.loglog(h, eS, 'o',label="E")
axes.legend(loc='upper left')
axes.grid()
axes.set_xlabel('h')
axes.set_ylabel('E')

#fig.tight_layout()
plt.show()


