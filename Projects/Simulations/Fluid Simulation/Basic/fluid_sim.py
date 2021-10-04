from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np
from simsquarelib import heat_sim_square as sim

FRAMERATE = 20
N_SECONDS = 5
RESOLUTION = 20
MID_POINT = RESOLUTION // 2
SQUARE_SIZE = 6
SQUARE_SIZE_DARK = 4
LS_BOUND = RESOLUTION // 2 - SQUARE_SIZE // 2
US_BOUND = RESOLUTION // 2 + SQUARE_SIZE // 2 + (1 if SQUARE_SIZE &1 else 0)
LS_BOUND_DARK = 2
US_BOUND_DARK = SQUARE_SIZE_DARK + 2
HEAT_MASK = np.zeros((RESOLUTION, RESOLUTION))
HEAT_MASK[LS_BOUND: US_BOUND, LS_BOUND: US_BOUND] = 1 
COOL_MASK = np.zeros((RESOLUTION, RESOLUTION))
COOL_MASK[LS_BOUND_DARK: US_BOUND_DARK, LS_BOUND_DARK: US_BOUND_DARK] = 1 

def animate_func(i):
    fluid_sim.apply_temperature_change(0.2, HEAT_MASK)
    fluid_sim.apply_temperature_change(-0.2, COOL_MASK)
    fluid_sim.apply_diffusion_naive()
    im.set_array(fluid_sim.temperatures)
    return [im]

fluid_sim = sim(size = RESOLUTION, timestep = 1 / FRAMERATE, viscosity = 1, diffusion_factor = 0.5)
fig, ax = plt.subplots(figsize=plt.figaspect(fluid_sim.temperatures))
plt.tight_layout()
plt.axis('off')
fig.subplots_adjust(0,0,1,1)
im = plt.imshow(fluid_sim.temperatures, interpolation='bicubic', vmin=-3, vmax=3, cmap='jet')

anim = animation.FuncAnimation(
                               fig,
                               animate_func,
                               frames = N_SECONDS * FRAMERATE,
                               interval = 1000 / FRAMERATE,
                               )

plt.show()

write_path = "D:/. Dev/VS Code/Python Learnings/python-learnings/Projects/Simulations/Fluid Simulation/Basic/test.mp4"

# writer = animation.PillowWriter(fps=FPS)
# anim.save(write_path, writer=writer)

writervideo = animation.FFMpegWriter(fps=FRAMERATE, codec="libx264", extra_args=['-pix_fmt', 'yuv420p']) 
anim.save(write_path, writer=writervideo)