from typing import List
import numpy as np
import numpy.typing as npt

class heat_sim_square:

    size: int
    iterations: int
    timestep: float
    diffusion_factor: float
    viscosity: float

    velocities_backup: List[npt.ArrayLike]
    velocities_x: npt.ArrayLike
    velocities_y: npt.ArrayLike
    temperatures: npt.ArrayLike

    def __init__(self, size: int, timestep: float, viscosity: float, diffusion_factor:float, iterations: int) -> None:
        self.size = size
        self.timestep = timestep
        self.viscosity = viscosity
        self.diffusion_factor = diffusion_factor
        self.velocities_x = np.zeros((size, size))
        self.velocities_y = np.zeros((size, size))
        self.velocities_z = np.zeros((size, size))
        self.temperatures = np.zeros((size, size))
        self.iterations = iterations

    def sim_step(self):
        # self.velocities_backup = [np.copy(self.velocities_x), np.copy(self.velocities_y), np.copy(self.velocities_z)]
        # self.velocities_x = self.get_diffusion_naive(self.velocities_x)
        # self.velocities_y = self.get_diffusion_naive(self.velocities_y)
        # self.fix_velocities(self.velocities_backup, self.velocities_x, self.velocities_y, self.velocities_z)

        # self.temperatures = self.get_diffusion_naive(self.temperatures)
        self.temperatures = self.get_linear_solve(self.temperatures, 0.5, self.iterations, False, True, True)

    def apply_temperature_change(self, temperature_change: float, mask: npt.ArrayLike):
        self.temperatures += temperature_change * mask


    # This 1_ doesn't do linear solving, so not realistic 2_ doesn't handle arrays
    def get_diffusion_naive(self, array: npt.ArrayLike) -> npt.ArrayLike:
        diffusion_array = np.zeros((self.size, self.size))
        for x in range(self.size):
            for y in range(self.size):
                count = 0
                for x_offset in [-1, 1]:
                    for y_offset in [-1, 1]:
                        # This could be speeded up with a more bespoke solution I reckon...
                        if 0 <= x + x_offset < self.size and 0 <= y + y_offset < self.size:
                            diffusion_array[x, y] += array[x + x_offset, y + y_offset] 
                            count += 1
                diffusion_array[x, y] /= count
        return (1 - self.diffusion_factor) * array + self.diffusion_factor * diffusion_array
    
    # For the maths to actually work, we need to make sure the boundaries of the area are always the opposite of their neighbours
    # The corners are set to the average of their neighbours
    def fix_boundaries(self, arr, is_mirror: bool, fix_horizontal: bool, fix_vertical: bool):
        i_max = self.size - 1
        mir = -1 if is_mirror else 1
        for i in range(1, i_max):
            if fix_horizontal:
                arr[i_max, i] = mir * arr[i_max - 1, i]
                arr[0, i] = mir * arr[1, i]
            if fix_vertical:
                arr[i, i_max] = mir * arr[i, i_max - 1]
                arr[i, 0] = mir * arr[i, 1]

    # Averages corners of array to adjacents        
    def fix_corners(self, arr: npt.ArrayLike):
        i_max = self.size - 1
        arr[0, 0] = (arr[0,1] + arr[1,0]) / 2
        arr[0, i_max] = (arr[0, i_max - 1] + arr[1, i_max]) / 2
        arr[i_max, 0] = (arr[i_max - 1, 0] + arr[i_max, 1]) / 2
        arr[i_max, i_max] = (arr[i_max, i_max - 1] + arr[i_max - 1, i_max]) / 2

    # Fix velocities to remove compressability
    def fix_velocities(backup_velocities, velocities_x, velocities_y):
        return

    # GAUSS-SEIDEL resolution of array
    def get_linear_solve(self, array: npt.ArrayLike, k, iterations, is_mirror: bool, fix_horizontal: bool, fix_vertical: bool):
        start_array = np.copy(array)
        iteration_array = np.copy(array)
        i_max = self.size - 1
        for _ in range(iterations):
            for x in range(1, i_max):
                for y in range(1, i_max):
                    neighbour_avg = sum(iteration_array[x + ofst_x, y + ofst_y] for ofst_x in [-1, 1] for ofst_y in [-1, 1]) / 4
                    iteration_array[x, y] = (start_array[x, y] + k * neighbour_avg) / (k + 1)
            self.fix_boundaries(iteration_array, is_mirror, fix_horizontal, fix_vertical)
            self.fix_corners(iteration_array)
        return iteration_array