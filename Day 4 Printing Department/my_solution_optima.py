from typing import List

Grid = List[List[str]]

DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
]

def load_grid(path: str) -> Grid:
    with open(path, "r", encoding="utf-8") as f:
        return [list(line.strip()) for line in f if line.strip()]

def is_accessible(grid: Grid, i: int, j: int) -> bool:
    # si no es un rollo, no tiene sentido evaluarlo
    if grid[i][j] != "@":
        return False

    rows = len(grid)
    cols = len(grid[0])

    neighbors = 0
    for dx, dy in DIRECTIONS:
        x = i + dx
        y = j + dy
        if 0 <= x < rows and 0 <= y < cols and grid[x][y] == "@":
            neighbors += 1
            if neighbors >= 4:
                # ya sabemos que NO es accesible, podemos cortar
                return False

    # si hemos llegado aquí, tiene menos de 4 vecinos '@'
    return True

def count_accessible_rolls(grid: Grid) -> int:
    rows = len(grid)
    cols = len(grid[0])
    total = 0

    for i in range(rows):
        for j in range(cols):
            if is_accessible(grid, i, j):
                total += 1

    return total


if __name__ == "__main__":
    grid = load_grid("input.txt")
    result = count_accessible_rolls(grid)
    print(result)
