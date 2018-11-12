import numpy as np 
from qubic_spl import qubic_spline as qsn
from qubic_spl import qubic_spline_coeff as qsc
from qubic_spl import d_qubic_spline as dqs
import lagranz as l 
import xlrd
import matplotlib.pyplot as plt

#Данные о ВВП РФ
GPD_VVP = (506500154001.466, 516814258695.568, 517962962962.963, 460290556900.726, 435083713850.837, 395077301248.464, 395531066563.296, 391719993756.828, 404926534140.017, 270953116950.026, 195905767668.562, 259708496267.33, 306602673980.117, 345110438692.185, 430347770731.787, 591016690742.798, 764017107992.391, 989930542278.695, 1299705247685.76, 1660844408499.61, 1222643696991.85, 1524916112078.87, 2051661732059.78, 2210256976945.38, 2297128039058.21, 2063662665171.89, 1365864126832.81, 1283162985989.3)
year = np.linspace(1989, 2016,28)

qs_coeff = qsc(year, GPD_VVP)# Вычисление коэфицентов куб. сплайна
x_extrapol = np.linspace(1989., 2019., 100)
y_extrapol = [qsn(i,qs_coeff,year,GPD_VVP) for i in x_extrapol]
dy_extrapol = [dqs(i,qs_coeff,year,GPD_VVP) for i in x_extrapol]

x_interpol = np.linspace(1989., 2016., 100)
y_interpol = [qsn(i,qs_coeff,year,GPD_VVP) for i in x_interpol]
dy_interpol = [dqs(i,qs_coeff,year,GPD_VVP) for i in x_interpol]

fnew = [qsn(i,qs_coeff,year,GPD_VVP) for i in x_extrapol]
df = [dqs(i,qs_coeff,year,GPD_VVP) for i in x_extrapol]
y_lagr=[l.L(i,year,GPD_VVP) for i in x_interpol]

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 10), dpi=100)
axes[0].plot(x_interpol, y_interpol, color="red", linewidth=1.0, linestyle="solid",label="S(x)")
axes[0].plot(year, GPD_VVP, 'o', color="blue")
axes[0].legend(loc='upper right')
axes[0].set_title('Интерполяционная кривая')
axes[0].set_xlabel('Год')
axes[0].set_ylabel('ВВП')

axes[1].plot(x_interpol, dy_interpol, color="red", linewidth=1.0, linestyle="solid",label="dS")
axes[1].set_title('Производная интерполяционной кривой')
axes[1].legend(loc='upper right')
axes[1].set_xlabel('Год')
axes[1].set_ylabel('Изменение ВВП')

axes[0].grid()
axes[1].grid()

plt.show()

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 10), dpi=100)
axes[0].plot(x_extrapol, y_extrapol, color="red", linewidth=1.0, linestyle="solid",label="S(x)")
axes[0].plot(year, GPD_VVP, 'o', color="blue")
axes[0].legend(loc='upper right')
axes[0].set_title('Эктраполяционная кривая')
axes[0].set_xlabel('Год')
axes[0].set_ylabel('ВВП')

axes[1].plot(x_extrapol, dy_extrapol, color="red", linewidth=1.0, linestyle="solid",label="dS")
axes[1].set_title('Производная экстраполяционной кривой')
axes[1].legend(loc='upper right')
axes[1].set_xlabel('Год')
axes[1].set_ylabel('Изменение ВВП')

axes[0].grid()
axes[1].grid()

plt.show()


fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(8, 6), dpi=100)
axes.plot(x_interpol, y_lagr, color="red", linewidth=1.0, linestyle="solid",label="L(x)")
axes.plot(year, GPD_VVP, 'o', color="blue",label="nodes")
axes.legend(loc='upper right')
axes.set_title('Интерполяция Лагранжа')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.grid()
plt.show()

