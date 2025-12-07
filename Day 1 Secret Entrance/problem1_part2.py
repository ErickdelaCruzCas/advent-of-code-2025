abs_pos = 50
crossings = 0

with open("puzzle_input.txt", "r") as f:
    for line in f:
        line = line.strip()
        direction = line[0]
        shift = int(line[1:])

        old = abs_pos

        if direction == "L":
            abs_pos = abs_pos - shift
        else:
            abs_pos = abs_pos + shift

        # cuántas veces cruzamos un múltiplo de 100
        crossings += abs(abs_pos // 100 - old // 100)


final_pointer = abs_pos % 100

print("Cruces por 0:", crossings)
