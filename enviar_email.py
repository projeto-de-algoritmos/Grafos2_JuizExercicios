import heapq

def shortest_time(n, m, S, T, connections):
    # Cria um grafo representado como um dicionário de adjacência
    graph = {i: [] for i in range(n)}
    for i in range(m):
        u, v, w = connections[i]
        graph[u].append((v, w))
        graph[v].append((u, w))

    # Inicializa as distâncias como infinito, exceto para o nó de origem
    dist = [float('inf')] * n
    dist[S] = 0

    # Usa Dijkstra para encontrar o caminho mais curto
    pq = [(0, S)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    # Verifica se é possível alcançar o nó de destino
    if dist[T] == float('inf'):
        return 'unreachable'
    else:
        return dist[T]

try:
    N = int(input())
except EOFError:
    N = 0  

for case in range(1, N + 1):
    try:
        n, m, S, T = map(int, input().split())
        connections = [list(map(int, input().split())) for _ in range(m)]
        result = shortest_time(n, m, S, T, connections)
        print(f'Case #{case}: {result}')
    except EOFError:
        break  # Encerra o loop se ocorrer EOFError
