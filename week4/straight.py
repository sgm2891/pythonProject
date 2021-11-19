
import matplotlib.pyplot as plt #matplotlib 에 있는 pyplot (클래스) 를 불러오되 plt라는 이름으로 불러온다.
from matplotlib.animation import FuncAnimation #matplotlib 에서 animation 이라는 클래스에서 FuncAnimation 이라는 함수를 불러온다
import numpy as np #numpy 를 np라는 이름으로 불러온다.

fig, ax = plt.subplots()
ax.scatter([0],[0], color = 'b')

def animation_straight(i):
    
    plt.cla()
    plt.xlim(0,1000)
    plt.ylim(0,1000)
    ax.scatter([i],[i])


animation1 = FuncAnimation(fig, func = animation_straight, frames = np.arange(0,1000,0.1),  interval= 1, blit=False)

plt.show()