import lagranz_basis as lb
import numpy as np

# функция нахождения интерполяционного полинома Лагранжа
# Передаваемые параметры: x - точка, в которой задан полином
# x_nodes, y_nodes - абсциссы и ординаты узлов

def L(x,x_nodes,y_nodes): 
    L=0
    for i in range(0,len(x_nodes)):
        L=lb.l_i(i,x,x_nodes)*y_nodes[i]+L; 
    return L