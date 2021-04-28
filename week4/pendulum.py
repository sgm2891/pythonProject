import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math

fig, ax = plt.subplots()
ax.scatter([0],[0], color = 'b')

angle = -1
a_vel = 0
a_acc = 0



def animation_gravity(i):
    global angle, a_vel, a_acc

    x = 10 * math.sin(angle)
    y = - 10*math.cos(angle)
    a_acc = - 9.8 * math.sin(angle) / 10 * 0.2
    a_vel += a_acc * 0.2
    angle += a_vel * 0.2
    
    plt.cla()
    plt.xlim(-10,10)
    plt.ylim(-11,0)
    ax.scatter([x],[y])




animation2 = FuncAnimation(fig, func = animation_gravity, interval = 1, blit=False)

plt.show()
