# import math


def rectangle_tile_area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    width  = abs(x2 - x1) + 1
    height = abs(y2 - y1) + 1
    return width * height

# def distance(p1, p2):
#     x1, y1 = p1
#     x2, y2 = p2
#     return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# def manhattan(p1, p2):
#     x1, y1 = p1
#     x2, y2 = p2
#     return abs(x2 - x1) + abs(y2 - y1)

print(f"Empezamos")
res = 0
coords = []
with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        right, left = line.split(',')
        coords.append((int(right), int(left)))


    # coords = [(int(right), int(left)) for line in f for right, left in [line.strip().split(',')]]
    print(f"Coordenads -> {coords}")
    # coords.sort()
    # print(coords)

    best_area = 0
    best_pair = None
    n = len(coords)

    for i in range(n):
        x1, y1 = coords[i]
        for j in range(i + 1, n):
            x2, y2 = coords[j]
            area = rectangle_tile_area((x1, y1), (x2, y2))
            if area > best_area:
                best_area = area
                best_pair = (coords[i], coords[j])

    # ini = 0
    # end = len(coords) - 1
    # while ini < end:
    #     area = rectangle_tile_area(coords[ini], coords[end])
    #     print(f"Area entre {coords[ini]} y {coords[end]} = {area}")
    #     if area > res:
    #         res = area
    #     ini += 1
    #     end -= 1




print(f"Solución y valor de Movie Theather: {best_area}") 