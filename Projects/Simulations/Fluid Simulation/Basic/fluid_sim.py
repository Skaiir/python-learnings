from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np

# CONSTANTS
FPS = 20
N_SECONDS = 5
RESOLUTION = 20
MID_POINT = RESOLUTION // 2
SQUARE_SIZE = 6
SQUARE_SIZE_DARK = 4
LS_BOUND = RESOLUTION // 2 - SQUARE_SIZE // 2
US_BOUND = RESOLUTION // 2 + SQUARE_SIZE // 2 + (1 if SQUARE_SIZE &1 else 0)
LS_BOUND_DARK = 2
US_BOUND_DARK = SQUARE_SIZE_DARK + 2
HEAT_ELEMENT_MATRIX = np.zeros((RESOLUTION, RESOLUTION))
HEAT_ELEMENT_MATRIX[LS_BOUND: US_BOUND, LS_BOUND: US_BOUND] = 1 
COOLING_ELEMENT_MATRIX = np.zeros((RESOLUTION, RESOLUTION))
COOLING_ELEMENT_MATRIX[LS_BOUND_DARK: US_BOUND_DARK, LS_BOUND_DARK: US_BOUND_DARK] = 1 

def heat_elements(strength):
    global img_data
    img_data += strength * HEAT_ELEMENT_MATRIX 

def cooling_elements(strength):
    global img_data
    img_data -= strength * COOLING_ELEMENT_MATRIX

def animate_func(i):
    heat_elements(0.2)
    cooling_elements(0.2)
    solve_diffusion_naive(0.5)
    im.set_array(img_data)
    return [im]

def solve_diffusion_naive(k):
    global img_data
    new_data = np.zeros((RESOLUTION, RESOLUTION))

    for x in range(RESOLUTION):
        for y in range(RESOLUTION):
            count = 0
            for offset_x in [-1, 1]:
                for offset_y in [-1, 1]:
                    if 0 <= x + offset_x < RESOLUTION and 0 <= y + offset_y < RESOLUTION:
                        count += 1
                        new_data[x, y] += img_data[x + offset_x, y + offset_y]
            new_data[x, y] /= count

    # Linear interpolation
    img_data = (1-k) * img_data  + k * new_data

img_data = np.zeros((RESOLUTION, RESOLUTION))
fig, ax = plt.subplots(figsize=plt.figaspect(img_data))
plt.tight_layout()
plt.axis('off')
fig.subplots_adjust(0,0,1,1)
im = plt.imshow(img_data, interpolation='bicubic', vmin=-3, vmax=3, cmap='jet')

anim = animation.FuncAnimation(
                               fig,
                               animate_func,
                               frames = N_SECONDS * FPS,
                               interval = 1000 / FPS,
                               )

plt.show()

write_path = "D:/. Dev/VS Code/Python Learnings/python-learnings/Projects/Simulations/Fluid Simulation/Basic/test.mp4"

# writer = animation.PillowWriter(fps=FPS)
# anim.save(write_path, writer=writer)

writervideo = animation.FFMpegWriter(fps=FPS, codec="libx264", extra_args=['-pix_fmt', 'yuv420p']) 
anim.save(write_path, writer=writervideo)