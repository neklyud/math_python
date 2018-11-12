import numpy as np

#Функция нахождения i-го базисного полинома Лагранжа
#Передаваемые параметры - i_n - номер полинома, x - точка, x_nodes - узлы
#Возвращаемое значение - число с плавающей точкой 

def l_i(i_n,x,x_nodes):
    P=1
    for i in range(0,len(x_nodes)):
        if (i_n==i):
            continue
        delta=x_nodes[i_n]-x_nodes[i]
        if(delta!=0):
            l_iter=(x-x_nodes[i])/(delta)
        else: 
            l_iter=1
        P=P*l_iter
    return P
            