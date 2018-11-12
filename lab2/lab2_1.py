import numpy as np
import matplotlib
import matplotlib.pyplot as plt

func = lambda x: x*np.exp(x)
x_0 = 2
h=0.0001
arr=np.logspace(-16,0,30)


def diff2(x_0,h,f):
    A=-1/(2*h)
    C=1/(2*h)
    return A*f(x_0-h)+C*f(x_0+h)

def diff4(x_0,h,f):
    A=1/(12*h)
    B=-2/(3*h)
    D=-B
    E=-A
    return A*f(x_0-2*h)+B*f(x_0-h)+D*f(x_0+h)+E*f(x_0+2*h)

def calculate(x_0,h,f,diff):
    fx=np.copy(h)
    for i in range(len(fx)-1):
        fx[i]=diff(x_0,h[i],f)
    return fx

f=np.exp(x_0)*(1+x_0)
f2=calculate(x_0,arr,func,diff2)
f4=calculate(x_0,arr,func,diff4)
err1=np.abs(f-f2)
err2=np.abs(f-f4)


fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(8, 6), dpi=100)
axes.loglog(arr, err1,linestyle = 'solid')
axes.loglog(arr, err2,linestyle = 'solid')
axes.grid(True)
fig.tight_layout() 
plt.show()
    
