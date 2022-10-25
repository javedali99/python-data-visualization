# show animation
animation = anim.FuncAnimation(fig, animate, frames=len(state_history[:, 0]))
plt.show()
