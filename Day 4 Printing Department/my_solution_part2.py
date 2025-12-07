
from typing import List


Matrix = List[List[str]]

DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
]

def load_matrix(path: str) -> Matrix:
    with open(path, "r", encoding="utf-8") as f:
        return [list(line.strip()) for line in f if line.strip()]


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
matrix = load_matrix("input.txt")
rows = len(matrix)
cols = len(matrix[0])

removedRolls = True

while removedRolls:
    countRemovedRolls = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "@":
                row_start = max(0, i - 1)
                row_end   = min(rows, i + 2)
                col_start = max(0, j - 1)
                col_end   = min(cols, j + 2)
                sub_matrix = []
                for r in range(row_start, row_end):
                    row_slice = matrix[r][col_start:col_end]
                    sub_matrix.append(row_slice)
                if can_access(sub_matrix) == 1:
                    matrix[i][j] = "."
                    res += 1
                    countRemovedRolls += 1
    print(f"RemovedRolls: {countRemovedRolls}")
    removedRolls = countRemovedRolls != 0
                    

print(f"Solución y valor del Printing Department: {res}")        