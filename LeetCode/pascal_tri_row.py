def getRow(rowIndex: int):
    row = [1]
    for x in range(rowIndex):
        new_row = []
        for y in range(x + 1):
            if y == 0 or y == x:
                new_row.append(1)
            else:
                new_row.append(row[y - 1] + row[y])
        row = new_row
    return row

getRow(5)