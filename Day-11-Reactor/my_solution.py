
    
def dfs(node, target, adjList, visit: list):
    # print(f"node: {node}, target: {target}, visit: {visit}")
    if node in visit:
        return 0
    if node == target:
        return 1
    paths = 0
    visit.append(node)    
    for neighbor in adjList[node]:
        paths += dfs(neighbor, target, adjList, visit)
    # visit.remove(node)
    return paths



print(f"Empezamos")
res = 0
adjacents = {}
with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
       right, left = line.split(":")
       adjacents[right] = left.split()
print(f"{adjacents}")
res = dfs('you', 'out', adjacents, [])

print(f"Solución y valor de Factory: {res}") 
# Este es facil, parece que lo primero es construir un arbol binario, y luego recorrerlo y obtener todos sus caminos
# Me puede servir el arbol binario, pero quiza sea mas correcto el priority heap
# En este arbol you es la raiz, y el final OUT