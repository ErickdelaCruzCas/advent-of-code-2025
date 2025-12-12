from functools import lru_cache

def count_paths(adjList):
    START = 'svr'
    TARGET = 'out'

    @lru_cache(maxsize=None)
    def dfs(node: str, have_dac: bool, have_fft: bool) -> int:
        # Actualizamos flags si estamos en uno de los nodos especiales
        if node == 'dac':
            have_dac = True
        if node == 'fft':
            have_fft = True

        # Caso base: hemos llegado al destino
        if node == TARGET:
            return int(have_dac and have_fft)

        total = 0
        for neighbor in adjList.get(node, []):  # get(...) evita KeyError
            total += dfs(neighbor, have_dac, have_fft)
        return total

    return dfs(START, False, False)



print(f"Empezamos")
res = 0
adjacents = {}
with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
       right, left = line.split(":")
       adjacents[right] = left.split()
# print(f"{adjacents}")
res = count_paths(adjacents)

print(f"Solución y valor de Factory: {res}") 
# Este es facil, parece que lo primero es construir un arbol binario, y luego recorrerlo y obtener todos sus caminos
# Me puede servir el arbol binario, pero quiza sea mas correcto el priority heap
# En este arbol you es la raiz, y el final OUT

