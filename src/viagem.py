import heapq

def dijkstra(grafo, inicio):
    # Inicializando o dicionário de distâncias com infinito para todas as localizações, exceto o início.
    distancias = {loc: float('inf') for loc in grafo}
    distancias[inicio] = 0

    # Fila de prioridade para armazenar as localizações com suas distâncias.
    pq = [(0, inicio)]

    while pq:
        dist_atual, loc_atual = heapq.heappop(pq)

        if dist_atual > distancias[loc_atual]:
            continue

        for vizinho, custo in grafo[loc_atual]:
            if dist_atual + custo < distancias[vizinho]:
                distancias[vizinho] = dist_atual + custo
                heapq.heappush(pq, (distancias[vizinho], vizinho))

    return distancias

n = int(input())
grafo = {}
for _ in range(n):
    a, b, w = map(int, input().split())
    if a not in grafo:
        grafo[a] = []
    if b not in grafo:
        grafo[b] = []
    grafo[a].append((b, w))
    grafo[b].append((a, w))

origem = int(input())
q = int(input())

# Calcular e imprimir o custo mínimo para cada consulta
for _ in range(q):
    destino = int(input())
    if origem not in grafo or destino not in grafo:
        print('SEM CAMINHO')
    else:
        distancias = dijkstra(grafo, origem)
        if distancias[destino] == float('inf'):
            print('SEM CAMINHO')
        else:
            print(distancias[destino])
