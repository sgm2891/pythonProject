import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math

fig, ax = plt.subplots()
color = ['#eb4034','#383636','#dae632','#1d79cf','#b53921','#cc7f02','#ad7417', '#0786b0', '#08c9b0']
ax.scatter([0,0.39,0.7,1,1.52,5,10,20,30],[0,0,0,0,0,0,0,0,0], color = color)
x = [0,0.39,0.7,1,1.52,5,10,20,30]
y = [0,0,0,0,0,0,0,0,0]
r = [0,0.39,0.7,1,1.52,5,10,20,30]
x_ = [0,0,0,0,0,0,0,0,0]
y_ = [0,0,0,0,0,0,0,0,0]

def x_y_(x,y):
    for i in range(9):
        x_[i] = x[i]-x[3]
        y_[i] = y[i]-y[3]
    



theta = [0,0,0,0,0,0,0,0,0]

plt.xlim(-15,15)
plt.ylim(-15,15)
k = 100

def frequncy(r):
    return (k*r**3)**0.5



def animation(i):
    for i in range(1,9):
        theta[i] += 1/frequncy(r[i])
        x[i] = math.cos(theta[i])*r[i]
        y[i] = math.sin(theta[i])*r[i]
    
    x_y_(x,y)

    
    plt.cla()
    plt.xlim(-15,15)
    plt.ylim(-15,15)
    ax.scatter(x_,y_, color = color) #ax.scatter(x,y, color = color) 지동설
        


animation1 = FuncAnimation(fig, func = animation, frames = t,interval = 1, blit=False)

plt.show()
