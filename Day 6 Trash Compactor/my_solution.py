from functools import reduce


print(f"Empezamos")
res = 0
matrix = []
with open("input.txt", "r", encoding="utf-8") as f:
    matrix = [line.split() for line in f]
    for i, operator in enumerate(matrix[-1]):
        res += reduce(
            lambda a, b: eval(f"{a}{operator}{b}"), 
            [matrix[j][i] for j in range(len(matrix) - 1)])
print(f"Solución y valor de Trash Compactor: {res}")        