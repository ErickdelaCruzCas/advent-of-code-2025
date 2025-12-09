print(f"Empezamos")
res = 0
matrix = []
with open("input.txt", "r", encoding="utf-8") as f:
    matrix = (line.split() for line in f)
    print(f"Matrix -> {matrix}")
    
print(f"Solución y valor de Trash Compactor: {res}") 