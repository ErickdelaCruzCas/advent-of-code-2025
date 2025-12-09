print(f"Empezamos")
res = 0
with open("input.txt", "r", encoding="utf-8") as f:
    intervals = list()
    phase = 1
    for line in (l.strip() for l in f):
        
        # print(f"Line Processing: {line}")
  
        
        if phase == 2:       
            ingredient = int(line)
            fresh = False
            i = 0
            while not fresh and i < len(intervals): 
                if intervals[i][0] <= ingredient <= intervals[i][1]:
                    res += 1 
                    fresh = True   
                i+=1
              
        if phase == 1:
            if line != "":
                a, b = line.split("-")
                intervals.append((int(a), int(b)))
            else:
                phase = 2              
        

    
print(f"Solución y valor de Cafeteria: {res}")        