# used only to get current working directory
import os

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

# load pre-calculated lorenz attractor
state_history = np.loadtxt(f'{os.getcwd()}/lorenz_state_history.txt', dtype=float)

# change plot background to dark
plt.style.use('dark_background')

# create figure
fig = plt.figure()  # figsize=(10, 8)

# data is 3-d so set projection property
ax = plt.axes(projection='3d')

# set title
ax.set(xlabel='X', ylabel='Y', zlabel='Z', title='The Lorenz Equations\n"Lorenz Attractor Simulation"')

# set background pane colours (RGBA values)
ax.w_xaxis.set_pane_color((0.25, 0.25, 0.2, 0.4))
ax.w_yaxis.set_pane_color((0.25, 0.25, 0.2, 0.4))
ax.w_zaxis.set_pane_color((0.25, 0.25, 0.2, 0.4))

# enable grid
ax.grid()

# determine axis limits using min and max values from corresponding dimension
ax.set_xlim3d(min(state_history[:, 0]) - 0.05, max(state_history[:, 0]) + 0.05)
ax.set_ylim3d(min(state_history[:, 1]) - 0.05, max(state_history[:, 1]) + 0.05)
ax.set_zlim3d(min(state_history[:, 2]) - 0.05, max(state_history[:, 2]) + 0.05)

# trajectory data to plot
trajectory, = ax.plot([], [], [])

# rotate matplotlib axes from 30 to 360
vertical_rotation_angles = np.linspace(0, 30, len(state_history[:, 0]))
horizontal_rotation_angles = np.linspace(0, 360, len(state_history[:, 0]))


def animate(i):
    # update axis view angle
    ax.view_init(vertical_rotation_angles[i], horizontal_rotation_angles[i])

    # update trajectory for current time step
    trajectory.set_data(state_history[:i, 0], state_history[:i, 1])
    trajectory.set_3d_properties(state_history[:i, 2])
    return trajectory,


# show animation
animation = anim.FuncAnimation(fig, animate, frames=len(state_history[:, 0]))
plt.show()

# save animation as gif
os.makedirs('./animations', exist_ok=True)

writer = anim.PillowWriter(fps=120)
animation.save('./animations/lorenz_attractor.gif', writer=writer)
