from typing import List


def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    height = len(mat)
    width = len(mat[0])
    dp = [[None]*width for i in range(height)]
    
    def distance(x, y):
        if (x, y) in visited:
            return None
        
        visited.add((x, y))
        
        if dp[y][x]:
            return dp[y][x]
        if mat[y][x] == 0:
            dp[y][x] = 0
            return 0
        
        distances = []
        
        if x > 0:
            distances.append(distance(x - 1, y))
        if x < width - 1:
            distances.append(distance(x + 1, y))
        if y > 0:
            distances.append(distance(x, y - 1))
        if y < height - 1:
            distances.append(distance(x, y + 1))
            
        print()
        distances = [i for i in distances if i != None]
        if len(distances) > 0:
            dp[y][x] = min(distances) + 1
            
    for y in range(height):
        for x in range(width):
            if not dp[y][x]:
                visited = set()
                distance(x, y)
        
    return dp


updateMatrix([[0,0,0],[0,1,0],[1,1,1]])