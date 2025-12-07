print(f"Empezamos")
res = set()
with open("input.txt", "r", encoding="utf-8") as f:
    intervals = []
    for raw in f:
        line = raw.strip()
        if not line:
            break
        a, b = line.split("-")
        intervals.append((int(a), int(b)))
    
    for (a,b) in intervals:
        # print(intervals)
        for i in range(a,b+1):
            print(i)
            res.add(i)
    
    q
print(f"Solución y valor de Cafeteria: {len(res)}")