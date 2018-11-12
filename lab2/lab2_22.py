import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 2
coeffs = np.array([np.random.randn() for i in range(0,28)])
gauss = np.zeros(7)
    

def gauss_quad5(a, b, f):
    c1=8/9
    c2=c3=5/9
    x1=(a+b)/2
    x2=(a+b+(b-a)*(np.sqrt(3/5)))/2
    x3=(a+b+(a-b)*(np.sqrt(3/5)))/2
    res=c1*f(x1)+c2*f(x2)+c3*f(x3)
    return res

def P0(x):
    return coeffs[0]

def P1(x):
    return coeffs[1] + coeffs[2] * x 

def P2(x):
    return coeffs[3] + coeffs[4] * x + coeffs[5] * x**2

def P3(x):
    return coeffs[6] + coeffs[7] * x + coeffs[8] * x**2 + coeffs[9] * x**3

def P4(x):
    return coeffs[10] + coeffs[11] * x + coeffs[12] * x**2 + coeffs[13] * x**3 + coeffs[14] * x**4

def P5(x):
    return coeffs[15] + coeffs[16] * x + coeffs[17] * x**2 + coeffs[18] * x **3 + coeffs[19] * x**4 + coeffs[20] * x**5

def P6(x):
    return coeffs[21] + coeffs[22] * x + coeffs[23] * x**2 + coeffs[24] * x**3 + coeffs[25] * x**4 + coeffs[26] * x**5 + coeffs[27] * x**6

ex0 = coeffs[0] * (b-a)
ex1 = coeffs[2] * (b**2 - a**2)/2 + coeffs[1] * (b-a)
ex2 = coeffs[5] * (b**3 - a**3)/3 + coeffs[4] * (b**2 - a**2)/2 + coeffs[3] * (b-a)
ex3 = coeffs[9] * (b**4 - a**4)/4 + coeffs[8] * (b**3 - a**3)/3 + coeffs[7] * (b**2 - a**2)/2 + coeffs[6] * (b-a)
ex4 = coeffs[14] * (b**5 - a**5)/5 + coeffs[13] * (b**4 - a**4)/4 + coeffs[12] * (b**3 - a**3)/3 + coeffs[11] * (b**2 - a**2)/2 + coeffs[10] * (b-a)   
ex5 = coeffs[20] * (b**6 - a**6)/6 + coeffs[19] * (b**5 - a**5)/5 + coeffs[18] * (b**4 - a**4)/4 + coeffs[17] * (b**3 - a**3)/3 + coeffs[16] * (b**2 - a**2)/2 + coeffs[15] * (b-a)
ex6 = coeffs[27] * (b**7 - a**7)/7 + coeffs[26] * (b**6 - a**6)/6 + coeffs[25] * (b**5 - a**5)/5 + coeffs[24] * (b**4 - a**4)/4 + coeffs[23] * (b**3 - a**3)/3 + coeffs[22] * (b**2 - a**2)/2 + coeffs[21] * (b-a)

L_func = [P0, P1, P2, P3, P4, P5, P6]      
L_ex = [ex0, ex1, ex2, ex3, ex4, ex5, ex6]
for i in range(0,7):
    gauss[i] =  gauss_quad5(a, b, L_func[i])
    print('i = ',i,' ',np.abs(L_ex[i] - gauss[i]))