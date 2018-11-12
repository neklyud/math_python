import numpy as np

#Функция вычисления коэфицентов кубического сплайна

def qubic_spline_coeff(x_nodes,y_nodes):
    length=len(y_nodes)
    A=np.diag([1]*length,0)
    b=np.zeros(length)
    h=[x_nodes[i+1]-x_nodes[i] for i in range(length-1)]
    for i in range(1,length-1):#Формирование матриц для нахождения матрицы коэфицентов C
        A[i][i]=2*(h[i]+h[i-1])
        A[i][i-1]=h[i]
        A[i][i+1]=h[i]
        b[i]=3./h[i]*(y_nodes[i+1]-y_nodes[i])-3./(h[i-1])*(y_nodes[i]-y_nodes[i-1])
    C=np.linalg.inv(A).dot(b)#Нахождение коэфицентов C
    a_res=y_nodes
    b_res=np.zeros(length)
    d_res=np.zeros(length)
    for i in range(length-1):
        b_res[i]=1./h[i]*(a_res[i+1]-a_res[i])-h[i]/3.*(C[i+1]+2*C[i])
        d_res[i]=(C[i+1]-C[i])/(3.*h[i])
    res=np.vstack((a_res[:-1],b_res[:-1]))
    res=np.vstack((res,C[:-1]))
    res=np.vstack((res,d_res[:-1]))
    return res.T

#Функция вычисления кубического сплайна S(x)

def qubic_spline(x,qs_coeff,x_nodes,y_nodes):
    indx=0
    xi=0
    for i in range(0,len(x_nodes)-1):
        if(x_nodes[i]<=x and x<=x_nodes[i+1]):
            xi=x_nodes[i]
            indx=i
            break
    if(x<x_nodes[0]):
        indx=0
        xi=x_nodes[0]
    if(x>x_nodes[len(x_nodes)-1]):
        indx=len(x_nodes)-2
        xi=x_nodes[len(x_nodes)-1]
    s=qs_coeff[indx][0]+qs_coeff[indx][1]*(x-xi)+qs_coeff[indx][2]*((x-xi)**2)+qs_coeff[indx][3]*((x-xi)**3)
    return s

#Функция вычисления производной S'(x)
def d_qubic_spline(x,qs_coeff,x_nodes,y_nodes):
    indx=0
    xi=0
    for i in range(0,len(x_nodes)-1):
        if(x_nodes[i]<=x and x<=x_nodes[i+1]):
            xi=x_nodes[i]
            indx=i
            break
    if(x<x_nodes[0]):
        indx=0
        xi=x_nodes[0]
    if(x>x_nodes[len(x_nodes)-1]):
        indx=len(x_nodes)-2
        xi=x_nodes[len(x_nodes)-1]
    ds=qs_coeff[indx][1]+2*qs_coeff[indx][2]*((x-xi))+3*qs_coeff[indx][3]*((x-xi)**2)
    return ds
