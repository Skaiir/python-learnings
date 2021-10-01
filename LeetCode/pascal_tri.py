def generate(numRows: int):
    result = []
    for x in range(numRows):
        work_arr = []
        for y in range(x + 1):
            if y == 0 or y == x:
                work_arr.append(1)
            else:
                work_arr.append(result[x - 1][y] + result[x - 1][y - 1])
        result.append(work_arr)
    return result

generate(10)