def setZeroes(matrix):
    rows,cols = len(matrix),len(matrix[0])
    first_row_zero = False
    first_col_zero = False

    # Check first row
    for c in range(cols):
        if matrix[0][c]==0:
            first_row_zero = True
    
    # check first col
    for r in range(rows):
        if matrix[r][0] == 0:
            first_col_zero = True
    
    # Mark rows and cols
    for r in range(1,rows):
        for c in range(1,cols):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0
    
    # Zer cells based on markers
    for r in range(1,rows):
        for c in range(1,cols):
            if matrix[r][0] == 0 or matrix[0][c]==0:
                matrix[r][c] = 0
    
    if first_col_zero:
        for r in range(rows):
            matrix[r][0] = 0
    if first_row_zero:
        for c in range(cols):
            matrix[0][c] = 0

rows,cols = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(rows)]
setZeroes(matrix)
for row in matrix:
    print(*row)
