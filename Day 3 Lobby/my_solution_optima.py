

def best_two_digit(line: str) -> int:
    digits = [int(c) for c in line.strip()]
    max_right = digits[-1]
    best = -1
    for i in range(len(digits) - 2, -1, -1):
        d = digits[i]
        candidate = d * 10 + max_right

        if candidate > best:
            best = candidate

        if d > max_right:
            max_right = d

    return best


print(f"Empezamos")
res = 0
with open("input.txt", "r", encoding="utf-8") as f:
    for line in (l.strip() for l in f):
        if not line:
            continue
        best = best_two_digit(line)
        res += best
print(f"Solución y valor del Joytalge: {res}")                  



    
