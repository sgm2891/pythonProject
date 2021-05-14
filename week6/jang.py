# Planet simulator
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
color = ['#eb4034', '#383636', '#dae632', '#1d79cf', '#b53921', '#cc7f02', '#ad7417', '#0786b0', '#08c9b0']
ax.scatter([0, 0.39, 0.7, 1, 1.52, 5, 10, 20, 30], [0, 0, 0, 0, 0, 0, 0, 0, 0], color=color)
x = [0, 0.39, 0.7, 1, 1.52, 5, 10, 20, 30]
y = [0, 0, 0, 0, 0, 0, 0, 0, 0]
vx = [0, 0, 0, 0, 0, 0, 0, 0, 0]
vy = [0, 4.8, 3.59, 3, 2.43, 1.34, 0.95, 0.67, 0.55]
Ax = [0, 0, 0, 0, 0, 0, 0, 0, 0]
Ay = [0, 0, 0, 0, 0, 0, 0, 0, 0]
m = [1, 1.66e-07, 2.647e-06, 3.00e-06, 3.22e-07, 0.001, 0.0003, 4.367e-05, 5.15e-05]

dt = 0.1

plt.xlim(-50, 50)
plt.ylim(-50, 50)
k = 100


def acc(i, j):
    l = 9 # GM, M은 태양질량
    value = l / (i ** 2 + j ** 2)
    len = (i ** 2 + j ** 2) ** (1 / 2)
    vector = (-i, -j)
    Ax, Ay = (-i * value / len, -j * value / len)
    return (Ax, Ay)

def allacc(i):
    SAx = 0
    SAy = 0
    for j in range(1,8):
        if i == j:
            continue
        else:
            xx = x[j] - x[i]
            yy = y[j] - y[i]
            l = 9*m[j] #Gm m은 j번째 행성 
            value = l / (xx ** 2 + yy ** 2)
            len = (xx ** 2 + yy ** 2) ** (1 / 2)
            Ax, Ay = (-xx * value / len, -yy * value / len)
            SAx += Ax
            SAy += Ay
    return (SAx, SAy)


def animation(i):
    for i in range(1, 9):
        a, b = acc(x[i], y[i])
        c, d = allacc(i)
        Ax[i] = a + c
        Ay[i] = b + d
        vx[i] += Ax[i] * dt
        vy[i] += Ay[i] * dt
        x[i] += vx[i] * dt
        y[i] += vy[i] * dt

    plt.cla()
    plt.xlim(-50, 50)
    plt.ylim(-50, 50)
    ax.scatter(x, y, color=color)  # ax.scatter(x,y, color = color) 지동설


animation1 = FuncAnimation(fig, func=animation, interval=1, blit=False)

plt.show()