
def max_value(s) -> int:
    size = len(s)
    L = 12
    to_pick = L
    start = 0
    result = []

    while to_pick > 0:
        # último índice donde puedo empezar a elegir
        end = size - to_pick  # inclusive

        max_digit = '0'
        max_pos = start

        # busco el dígito más grande entre start y end
        for i in range(start, end + 1):
            if s[i] > max_digit:
                max_digit = s[i]
                max_pos = i
                # si veo un 9 ya no hay nada mejor

        result.append(max_digit)
        start = max_pos + 1
        to_pick -= 1

    return int("".join(result))


print(f"Empezamos")
res = 0
with open("input.txt", "r", encoding="utf-8") as f:
        for line in (l.strip() for l in f):
            res += max_value(line)
    
print(f"Solución y valor del Joytalge: {res}")        