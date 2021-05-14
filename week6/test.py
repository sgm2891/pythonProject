import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math

fig, ax = plt.subplots()
color = ['#eb4034','#383636','#dae632','#1d79cf','#b53921','#cc7f02','#ad7417', '#0786b0', '#08c9b0']

x = [0,4.49e2,10.5e2,15e2,22.7e2,74.8e2,150e2,299e2,499e2]
ax.scatter(x,[0,0,0,0,0,0,0,0,0], color = color)
y = [0,0,0,0,0,0,0,0,0]
vy = [0,.000478725,.000350214,.000297859,.000241309,.000130697,.000096724,.000068352,.000054778]
vx = [0,0,0,0,0,0,0,0,0]
GM = 2.3271244e-4
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

lim = 8e3

plt.xlim(-lim,lim)
plt.ylim(-lim,lim)

dt = 1e6

def animation(i):
    for i in range(1,9):
        acc = gravity_acc(x[i], y[i]) 
        vx[i] += acc[0]* dt
        vy[i] += acc[1]* dt

        x[i] += vx[i] *dt
        y[i] += vy[i] *dt
    
    
    plt.cla()
    plt.xlim(-lim,lim)
    plt.ylim(-lim,lim)  
    ax.scatter(x,y, color = color)
        


animation1 = FuncAnimation(fig, func = animation, interval = 1, blit=False)

plt.show()


사실 찾아보니까 헤밀토니안 풀어