from math import prod



print(f"Empezamos")
res = 0
with open("input.txt", "r", encoding="utf-8") as f:
    lines = [line.rstrip("\n") for line in f]


problems = lines[:-1]          # todas menos la última
op_row_raw   = lines[-1]       # última fila: operadores
    
    # Extraemos operadores en orden de izquierda a derecha
operations = [ch for ch in op_row_raw if ch in "+*"]     
       
numbers = []

for i in range(len(problems[0]) - 1, -1, -1):
    if all(problem[i] == ' ' for problem in problems):
        if numbers:
            operation = operations.pop()
            if operation == '+':
                res += sum(numbers)
            elif operation == '*':
                res += prod(numbers)
            numbers = []
    else:
        column = ''.join(problem[i] for problem in problems).strip()
        numbers.append(int(column))

# Por si el último bloque no terminaba en columna vacía
if numbers:
    operation = operations.pop()
    if operation == '+':
        res += sum(numbers)
    elif operation == '*':
        res += prod(numbers)
     
print(f"Solución y valor de Trash Compactor: {res}")