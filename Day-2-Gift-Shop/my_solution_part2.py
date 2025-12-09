
def is_repetition(s: str) -> bool:
    return s in (s + s)[1:-1]

print(f"Empezamos")
res = 0
with open("ids_input.txt", "r", encoding="utf-8") as f:
    ranges = f.read().split(",")
    for range_str in ranges:
        start_str, end_str = range_str.split("-")
        start  = int(start_str)
        end = int(end_str)
        print(start, end)
        for num in range(start, end + 1):
            s = str(num)
            if is_repetition(s):  
                res += int(s)
                
print(f"Fin del verano: Solución: {res}")        