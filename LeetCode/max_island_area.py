from typing import List

def maxAreaOfIsland(grid: List[List[int]]) -> int:
    visited = set()
    width = len(grid)
    height = len(grid[0]) 
    
    def island_area(x, y) -> int:
        if grid[x][y] == 0 or (x, y) in visited:
            return 0
        visited.add((x, y))
        area = 1
        if x > 0:
            area += island_area(x - 1, y)
        if x < width - 1:
            area += island_area(x + 1, y)
        if y > 0:
            area += island_area(x, y - 1)
        if y < height - 1:
            area += island_area(x, y + 1)
        return area
            
    largest_island_area = 0
    
    for x in range(width):
        for y in range(height):
            if grid[x][y] == 1 and not (x,y) in visited:
                largest_island_area = max(largest_island_area, island_area(x, y))
                
    return largest_island_area