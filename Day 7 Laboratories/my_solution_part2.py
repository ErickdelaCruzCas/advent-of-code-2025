

print(f"Empezamos")
res = 0
with open("input.txt", "r", encoding="utf-8") as f:
    matrix = [line.split("\n") for line in f]
    print(matrix)
    pointers = [0]
    
    while matrix[0][pointers[0]] != 'S':
        pointers[0] +=1
    
    for i in range(1, len(matrix)):
        for pointer in pointers: 
            if matrix[i][pointers] == "^":
                pointer_splited = int(pointers.pop())
                pointers.append(pointer_splited - 1)
                pointers.append(pointer_splited + 1)
                res += 1
        
    
    print(f"Poiner: {pointers} of S: {matrix[0][1]}")
    
    
    
    
    
     
    print(f"Solución y valor de Laboratories: {res}")