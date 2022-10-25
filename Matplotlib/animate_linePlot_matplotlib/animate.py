def animate(i):
    # update axis view angle
    ax.view_init(vertical_rotation_angles[i], horizontal_rotation_angles[i])

    # update trajectory for current time step with x, y data
    trajectory.set_data(state_history[:i, 0], state_history[:i, 1])\
    
    # update z-dimension data
    trajectory.set_3d_properties(state_history[:i, 2])
    
    # return trajectory, _
    return trajectory,
