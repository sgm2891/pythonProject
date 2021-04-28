import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()
ax.scatter([0],[0], color = 'b')

def animation_straight(i):
    
    plt.cla()
    plt.xlim(0,10)
    plt.ylim(0,10)
    ax.scatter([i],[i])


animation1 = FuncAnimation(fig, func = animation_straight, frames = np.arange(0,1000,0.1), interval = 1, blit=False)

plt.show()