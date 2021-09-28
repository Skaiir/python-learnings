def floodFill(image, sr, sc, newColor):
    old_color = image[sr][sc] 
    r_max = len(image)
    c_max = len(image[0])
    def fill(sr, sc):
        if old_color == image[sr][sc]:
            image[sr][sc] = newColor
            if sr + 1 < r_max:
                fill(sr + 1, sc)
            if sr - 1 >= 0:
                fill(sr - 1, sc)
            if sc + 1 < c_max:
                fill(sr, sc + 1)
            if sc - 1 >= 0:
                fill(sr, sc - 1)
    fill(sr, sc)
    []]
    return image

floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)