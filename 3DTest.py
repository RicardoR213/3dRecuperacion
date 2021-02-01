"""
RICARDO REYES BENIGNO
Examen complementario 3D

"""
import numpy as np
import matplotlib.pyplot as plt
import tools3d as Tools
from math import ceil

xg=[]
yg=[]
zg=[]

xc = 80;    yc = 40;    zc = 40

def plotPlano(xg,yg,zg):
    plt.axis([90,280,140,30])
    plt.axis()
    plt.grid()
    #Plot plane
    plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='k')
    plt.plot([xg[1],xg[2]],[yg[1],yg[2]],color='k')
    plt.plot([xg[2],xg[0]],[yg[2],yg[0]],color='k')
    #Punto 3
    plt.scatter(xg[3],yg[3],s=20,color='r')
   
    plt.plot([xg[0],xg[3]],[yg[0],yg[3]],color='r',linestyle=':')
    plt.plot([xg[1],xg[3]],[yg[1],yg[3]],color='r',linestyle=':')
    plt.plot([xg[2],xg[3]],[yg[2],yg[3]],color='r',linestyle=':')

    plt.show()

def hitPoint(x,y,z):
    
    a=x[1]-x[0]
    b=y[1]-y[0]
    c=z[1]-z[0]
    Q01=np.sqrt(a*a+b*b+c*c)
    
    a=x[2]-x[1]
    b=y[2]-y[1]
    c=z[2]-z[1]
    Q12=np.sqrt(a*a+b*b+c*c)
    
    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    Q02=np.sqrt(a*a+b*b+c*c)
    
    a=x[3]-x[1]
    b=y[3]-y[1]
    c=z[3]-z[1]
    Q13=np.sqrt(a*a+b*b+c*c)
    #Distancia del punto(2,3)
    a=x[2]-x[3]
    b=y[2]-y[3]
    c=z[2]-z[3]
    Q23=np.sqrt(a*a+b*b+c*c)
    #Distancia del punto(0,3)
    a=x[0]-x[3]
    b=y[0]-y[3]
    c=z[0]-z[3]
    Q03=np.sqrt(a*a+b*b+c*c)
    #Area  del triangule A
    s=(Q01+Q12+Q02)/2
    A=np.sqrt(s*(s-Q01)*(s-Q12)*(s-Q02))
    #Area  del triangule A1
    s1=(Q01+Q03+Q13)/2
    A1=np.sqrt(s1*(s1-Q01)*(s1-Q03)*(s1-Q13))
    #Area  del triangule A2
    s2=(Q02+Q23+Q03)/2
    A2=np.sqrt(s2*(s2-Q02)*(s2-Q23)*(s2-Q03))


    return A,A1,A2
    

def plotTriangulo(xc,yc,zc):
    

    [A,A1,A2]=hitPoint(x,y,z)
    if((A1+A2)>A):
        plt.text(200,85,'Fuera del triangulo')
    elif((A1+A2)<A):
        plt.text(200,85,'Esta Dentro del triangulo1')
    A=ceil(A)
    A1=ceil(A1)
    A2=ceil(A2)
    A3=ceil(A1+A2)
    plt.text(215,60,'A=',color='g')
    plt.text(225,60,A,color='g')
    plt.text(215,65,'A1=',color='g')
    plt.text(225,65,A1,color='g')
    plt.text(215,70,'A2=',color='g')
    plt.text(225,70,A2,color='g')
    if((A1+A2)>A):
        plt.text(202,75,'A1+A2=',color=(.5,.2,.8))
        plt.text(225,75,A3,color=(.5,.2,.8))
    elif((A1+A2)<A):
        plt.text(202,75,'A1+A2=',color='BLUE')
        plt.text(225,75,A3,color='BLUE')

    plotPlano(xg,yg,zg)
x=[40,30,80,0]
y=[60,10,60,0]
z=[0,0,0,0]

while True:
    HPX=input('Coordenadas del hit point X? Pulse esc para salir: ')
    if HPX=='esc':
        break
    else:
        x[3]=int(HPX)
        HPY=input('Coordenadas del hit point Y?: Pulse esc para salir: ')
        if HPY=='esc':
            break
        else:
            y[3]=int(HPY)

            for i in range(len(x)):
                xg.append( x[i]+xc )
                yg.append( y[i]+yc )
                zg.append( z[i]+zc )

            plotTriangulo(xc,yc,zc);

 