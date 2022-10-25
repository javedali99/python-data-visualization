# determine axis limits using min and max values from corresponding dimension

# x-axis limit
ax.set_xlim3d(min(state_history[:, 0]) - 0.05, max(state_history[:, 0]) + 0.05)

# y-axis limit
ax.set_ylim3d(min(state_history[:, 1]) - 0.05, max(state_history[:, 1]) + 0.05)

# z-axis limit
ax.set_zlim3d(min(state_history[:, 2]) - 0.05, max(state_history[:, 2]) + 0.05)
