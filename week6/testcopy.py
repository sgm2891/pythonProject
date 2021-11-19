import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math

fig, ax = plt.subplots()
color = ['#eb4034','#383636','#dae632','#1d79cf','#b53921','#cc7f02','#ad7417', '#0786b0', '#08c9b0']

x = [0,57.91,108.21,149.60,227.94,778.34,1426.67,2870.66,4498.396]
ax.scatter(x,[0,0,0,0,0,0,0,0,0], color = color)
y = [0,0,0,0,0,0,0,0,0]
vy = [0,.170503,.126074,.107218,.086677,.047002,.034701,.024477,.019566]
vx = [0,0,0,0,0,0,0,0,0]
GM = 1.7271244
x_ = [0,0,0,0,0,0,0,0,0]
y_ = [0,0,0,0,0,0,0,0,0]

def x_y_(x,y):
    for i in range(9):
        x_[i] = x[i]-x[3]
        y_[i] = y[i]-y[3]

def cosine(x,y):
    return x/(x**2 + y**2)**0.5

def sine(x,y):
    return y/(x**2 + y**2)**0.5


def gravity_acc(x,y):
    acc = GM/(x**2 + y**2)
    ax = -acc * cosine(x,y)
    ay = -acc * sine(x,y)
    return [ax, ay]


lim = 5000

plt.xlim(-lim,lim)
plt.ylim(-lim,lim)

dt = 1000

def animation(j):
    for i in range(1,9):
        acc = gravity_acc(x[i], y[i]) 
        vx[i] += acc[0]* dt
        vy[i] += acc[1]* dt
        if j > 7:
            x[(j%10)*8+i] = x[i]
            y[(j%10)*8+i] = y[i]
            color[(j%10)*8+i] = color[i]
        else:
            x.append(x[i])
            y.append(y[i])
            color.append(color[i])

        x[i] += vx[i] *dt
        y[i] += vy[i] *dt
    
    
    plt.cla()
    plt.xlim(-lim,lim)
    plt.ylim(-lim,lim)  
    ax.scatter(x,y, color = color)
    ax.set_aspect('equal', adjustable='box')
    plt.axis('off')


animation1 = FuncAnimation(fig, func = animation, interval = 1, blit=False)

plt.show()