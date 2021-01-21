# import matplotlib.animation as animation
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.animation import FuncAnimation

# fig, ax = plt.subplots()
# ball1, = plt.plot([], [], 'o', color='r', label='Ball')
# ball2, = plt.plot([], [], 'o', color='b', label='Ball')
# xdata, ydata = [], []

# def circle_move(R, vx0, vy0, time, angle_vel):
#     x0 = vx0 * time
#     y0 = vy0 * time
#     alpha = np.arange(0, 2*np.pi, 0.1)
#     alpha = angle_vel * (np.pi/180) * time
    
#     x = x0 + R*np.cos(alpha)
#     y = y0 + R*np.sin(alpha)

#     x0 = vx0 * time
#     y0 = vy0 * time
        
#     x = R*np.cos(alpha)
#     y = R*np.sin(alpha)
    
#     return x, y


# edge = 40
# plt.axis('equal')
# ax.set_xlim(-edge, edge)
# ax.set_ylim(-edge, edge)

# def animate(i):
#      ball1.set_data(circle_move(R=0.5, vx0=0.01, vy0=0.01, time=i, angle_vel = 1))
#      ball2.set_data(circle_move(R=0.5, vx0=0.01, vy0=0.01, time=i, angle_vel = 2))

# ani = animation.FuncAnimation(fig,
#                                 animate,
#                                 frames=100,
#                                 interval=30
#                                 )

# ani.save('lec_7_complex_animation.gif')

  
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ball1, = plt.plot([], [], 'o', color='r', label='Ball1')
ball2, = plt.plot([], [], 'o', color='b', label='Ball2')

def telo1(R1, v1x0, v1y0, time):
    x01 = 10+v1x0*time
    y01 = 5 + v1x0*time

    alpha = np.arange(0,2*np.pi, 0.01)
    x1_1 = x01 + R1*np.cos(alpha)
    y1_1 = y01 + R1*np.sin(alpha)

    return x1_1, y1_1

def telo2(R2, v2x0, v2y0, time):
    x02 = -10+v2x0*time
    y02 = 0 #5+v2x0*time

    alpha = np.arange(0,2*np.pi, 0.01)
    x1_2 = x02 + R2*np.cos(alpha)
    y1_2 = y02 + R2*np.sin(alpha)

    return x1_2, y1_2

edge = 50
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    ball1.set_data(telo1(R1=0.5, v1x0=0.2, v1y0=1, time=i))
    ball2.set_data(telo2(R2=0.5, v2x0=0.2, v2y0=1, time=i))

ani = animation.FuncAnimation(fig,
                            animate,
                            frames=100,
                            interval=5
                            )


ani.save('proekt.gif')