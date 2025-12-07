
from typing import List

def can_access(submatrix: List[List[str]]) -> int:
    rows = len(submatrix)
    cols = len(submatrix[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if submatrix[r][c] == "@":
                count += 1
    if count < 5:
        return 1
    else:
        return 0

print(f"Empezamos")
res = 0
matrix = []
with open("input.txt") as f:
    matrix = [list(line.strip()) for line in f]
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "@":
                row_start = max(0, i - 1)
                row_end   = min(rows, i + 2)
                col_start = max(0, j - 1)
                col_end   = min(cols, j + 2)
                # print(f"Center=({i},{j}) rows=[{row_start}:{row_end}) cols=[{col_start}:{col_end})")
                sub_matrix = []
                for r in range(row_start, row_end):
                    row_slice = matrix[r][col_start:col_end]
                    # print(f"  row {r} -> slice cols[{col_start}:{col_end}) = {row_slice}")
                    sub_matrix.append(row_slice)
                
                # print(f"My SubMatrix -> {sub_matrix}")
                res += can_access(sub_matrix)
                
                
             

print(f"Solución y valor del Printing Department: {res}")        