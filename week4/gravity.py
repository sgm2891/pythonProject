import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()
ax.scatter([0],[0], color = 'b')

x=0
y=0
vx=10
vy=10

def animation_gravity(i):
    global x,y,vy,vx
    x += vx*0.02 #0.02 매우 짧은 순간
    y += vy*0.02
    vy -= 9.8*0.02
    
    plt.cla()
    plt.xlim(0,24)
    plt.ylim(0,10)
    ax.scatter([x],[y])

animation2 = FuncAnimation(fig, func = animation_gravity, interval = 1, blit=False)

plt.show()
