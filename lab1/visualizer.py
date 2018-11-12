import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
import lagranz as l

#Количество узлов
N=20

#Функция вычисления значения ординаты
func=lambda x: 1/(1+25*x*x)

#Генерация узлов 
x=np.linspace(-1, 1, N,endpoint=True)
y=func(x)
x1=np.linspace(-1, 1, 200,endpoint=True)
y1=func(x1)
y2=[l.L(i,x,y) for i in x1]

#визуализация
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 6), dpi=100)
axes[0].plot(x1, y1, color="blue", linewidth=1.0, linestyle="-",label="f(x)")
axes[0].plot(x1, y2, color="green", linewidth=1.0, linestyle="-",label="L(x), равномерные узлы")
axes[0].plot(x, y, 'ro', color="red")
axes[0].legend(loc='upper right')
axes[0].set_title('Равномерные узлы (N=20)')
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].grid()

#Вычисление узлов Чебышева
x_cheb=np.array([np.cos((2*k-1)*np.pi/(2*N)) for k in np.linspace(1,N,N,endpoint=True)])
y_cheb = func(x_cheb)
y2 = [ l.L(i,x_cheb,y_cheb) for i in x1]

#визуализация узлов Чебышева
axes[1].plot(x1, y1, color="blue", linewidth=1.0, linestyle="solid",label="f(x)")
axes[1].plot(x1, y2, color="green", linewidth=1.0, linestyle="-",label="L(x), Чебышёвские узлы")
axes[1].plot(x_cheb, y_cheb, 'ro', color="red")
axes[1].legend(loc='upper right')
axes[1].set_title('Чебышёвские узлы (N=20)')
axes[1].set_xlabel('x')
axes[1].set_ylabel('f(x)')

axes[1].grid()

plt.show()