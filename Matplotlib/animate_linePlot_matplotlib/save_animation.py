# save animation as gif
os.makedirs('./animations', exist_ok=True)

# multiple writers are available - PillowWriter is already installed
writer = anim.PillowWriter(fps=120)
animation.save('./animations/lorenz_attractor.gif', writer=writer)
