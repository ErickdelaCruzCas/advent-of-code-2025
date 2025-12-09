

print(f"Empezamos")
res = 0
with open("input.txt", "r", encoding="utf-8") as f:
    matrix = [line.rstrip("\n") for line in f]

    pointers = []
    tachyon_beam = set()
    firstpointer = matrix[0].index('S') 
    pointers.append(firstpointer)
    
    for i in range(1, len(matrix)):
        print(f"Processing -> {matrix[i]}")
        new_pointers = []
        while pointers:
            pointer = pointers.pop()
            pos = (i, pointer)
            print(f"Pos processing -> {pos}")
            # if pointer < 0 or pointer >= len(matrix[i]):
            #     continue
            
            if matrix[i][pointer] == "^":
                # 2) Solo contamos el split una vez por splitter
                if pos not in tachyon_beam:
                    print(f"{pointer} -> {matrix[i][pointer]}")
                    tachyon_beam.add(pos)
                    res += 1

                # El haz que venía muere, pero se crean dos nuevos a izquierda y derecha
                left = pointer - 1
                right = pointer + 1

                # 3) No metemos haces fuera del manifold
                if 0 <= left < len(matrix[i]):
                    new_pointers.append(left)
                if 0 <= right < len(matrix[i]):
                    new_pointers.append(right)

            else:
                # sigue recto hacia abajo
                new_pointers.append(pointer)

        # 4) Fusionamos haces que acaban en la misma columna
        #    (si dos splitters apuntan al mismo sitio, solo hay un haz)
        pointers = list(set(new_pointers))
    
     
    print(f"Solución y valor de Laboratories: {res}")