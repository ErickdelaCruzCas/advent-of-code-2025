from functools import reduce


print(f"Empezamos")
res = 0
matrix = []
with open("input.txt", "r", encoding="utf-8") as f:
    matrix = [line.split() for line in f]
    # print(f"Matrix -> {matrix}")

    operators = matrix[-1]
    # print(f"Operators -> {operators}")
    
    for i, operator in enumerate(operators):
                
        nums = [matrix[j][i] for j in range(len(matrix) - 1)]
        print(nums)    
        acum = reduce(lambda a, b: eval(f"{a}{operator}{b}"), nums)
        print(acum)    
            # print(f"Operator: {operator}, matrix value: {matrix[j][i]}")
            # print(f"iterator of operator: {i}, iterator of matrix col: {j}")
    
        res += acum
        # Without Variables 
        # res += reduce(
        #     lambda a, b: eval(f"{a}{operator}{b}"), 
        #     [matrix[j][i] for j in range(len(matrix) - 1)])
print(f"Solución y valor de Trash Compactor: {res}")        