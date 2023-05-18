import queue

with open('input.txt', 'r') as f:
    lineas = f.readlines()

filas = int(lineas[0])
columnas = int(lineas[1])
inicio = tuple(map(int, lineas[2].split()))
fin = tuple(map(int, lineas[3].split()))
laberinto = []
for i in range(4, filas+4):
    fila = []
    for j in range(columnas):
        if lineas[i][j] == '0':
            fila.append(0)
        elif lineas[i][j] == '+':
            fila.append(1)
    laberinto.append(fila)

grafo = {}
for i in range(filas):
    for j in range(columnas):
        if laberinto[i][j] == 1:
            continue
        actual = (i, j)
        vecinos = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        adyacentes = []
        for v in vecinos:
            if v[0] < 0 or v[0] >= filas or v[1] < 0 or v[1] >= columnas:
                continue
            if laberinto[v[0]][v[1]] == 1:
                continue
            adyacentes.append(v)
        grafo[actual] = adyacentes

q = queue.Queue()
q.put(inicio)
visitados = set()
previo = {}
while not q.empty():
    actual = q.get()
    if actual == fin:
        break
    for n in grafo[actual]:
        if n in visitados:
            continue
        visitados.add(n)
        previo[n] = actual
        q.put(n)

with open('solucion.txt', 'w') as f:
    for i in range(filas):
        for j in range(columnas):
            if (i, j) == inicio:
                f.write('I')
            elif (i, j) == fin:
                f.write('F')
            elif (i, j) in previo:
                f.write('.')
            elif laberinto[i][j] == 0:
                f.write(' ')
            else:
                f.write('+')
        f.write('\n')
