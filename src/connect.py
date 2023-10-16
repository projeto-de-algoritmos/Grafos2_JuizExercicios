from collections import deque

def count_districts(city):
    def bfs(start_node):
        visited.add(start_node)
        queue = deque([start_node])

        while queue:
            current_node = queue.popleft()
            for neighbor in city[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    districts = 0
    visited = set()

    for location in city:
        if location not in visited:
            bfs(location)
            districts += 1

    return districts

city = {
    'p0': ['p1', 'p2'],
    'p1': ['p0'],
    'p2': ['p0'],
    'p3': []
}

num_districts = count_districts(city)
print(f'O número de distritos na cidade é: {num_districts}')

