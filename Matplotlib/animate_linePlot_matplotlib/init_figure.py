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
