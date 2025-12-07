from functools import cache


f = open("input.txt", "r")
filas = []
for line in f:
  filas.append(line.strip())
f.close()
anchoDatos = len(filas[0])
altoDatos = len(filas)

# ramasCalculadas = {}

@cache
def laserPath(y, x):
  if(y == altoDatos-1):
    # caso base, fin del camino
    return 1
  # elif((y,x) in ramasCalculadas):
  #   # usa el número de caminos previamente calculado desde este divisor
  #   return ramasCalculadas[(y,x)]
  elif(filas[y][x] == "^"):
    # calcula los caminos desde este divisor
    output = 0
    output += laserPath(y+1, x-1)
    output += laserPath(y+1, x+1)
    # ramasCalculadas[(y,x)] = output
    return output
  else:
    # el láser pasó por espacio vacío
    return laserPath(y+1, x)
    

for y in range(altoDatos):
  for x in range(anchoDatos):
    if(filas[y][x] == "S"):
      # inicio del láser
      output = laserPath(y+1, x)
      break

print(output)