import numpy as np
import numpy.typing as npt

class heat_sim_square:

    size: int
    timestep: float
    diffusion_factor: float
    viscosity: float
    initial_velocities: npt.ArrayLike
    velocities: npt.ArrayLike
    temperatures: npt.ArrayLike

    def __init__(self, size: int, timestep: float, viscosity: float, diffusion_factor:float) -> None:
        self.size = size
        self.timestep = timestep
        self.viscosity = viscosity
        self.diffusion_factor = diffusion_factor
        self.initial_velocities = np.zeros((size, size))
        self.velocities = np.zeros((size, size))
        self.temperatures = np.zeros((size, size))

    def apply_temperature_change(self, temperature_change: float, mask: npt.ArrayLike):
        self.temperatures += temperature_change * mask

    def apply_diffusion_naive(self):
        diffusion_temperature = np.zeros((self.size, self.size))
        for x in range(self.size):
            for y in range(self.size):
                count = 0
                for x_offset in [-1, 1]:
                    for y_offset in [-1, 1]:
                        # This could be speeded up with a more bespoke solution I reckon...
                        if 0 <= x + x_offset < self.size and 0 <= y + y_offset < self.size:
                            diffusion_temperature[x, y] += self.temperatures[x + x_offset, y + y_offset] 
                            count += 1
                diffusion_temperature[x, y] /= count
        self.temperatures = (1 - self.diffusion_factor) * self.temperatures + self.diffusion_factor * diffusion_temperature 