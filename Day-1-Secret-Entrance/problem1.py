

pointer = 50
res = 0
print(f"Empezamos en: {pointer}")
with open("puzzle_input.txt", "r", encoding="utf-8") as f:
    
    for line in f:
        line = line.strip()
        direction = line[0]
        shift = int(line[1:])
        print(f"Dir: {direction}, {shift}")
        if direction == "L":
            pointer = pointer - shift
            if pointer < 0:
                pointer =  pointer % 100
            print(f"Resultado: {pointer}")
        elif direction == "R":
            # print("hacia la derecha")
            pointer = pointer + shift
            if pointer > 99:
                pointer = pointer % 100           
            print(f"Resultado: {pointer}")
    
        if pointer == 0:
            res += 1
            print(f"Parado en 0, el contador sube a: {res}")

        
        
        
print(f"Tu poderoso y resultado es: -> {res} <- : !")
        