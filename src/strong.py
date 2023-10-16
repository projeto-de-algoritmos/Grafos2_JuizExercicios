def strongly_connected_components(graph):
    def dfs1(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs1(neighbor)
        stack.append(node)

    def dfs2(node, component):
        visited[node] = True
        component.add(node)
        for neighbor in reversed_graph[node]:
            if not visited[neighbor]:
                dfs2(neighbor, component)

    num_nodes = len(graph)
    visited = [False] * num_nodes
    stack = []
    reversed_graph = [[] for _ in range(num_nodes)]

    for node in range(num_nodes):
        for neighbor in graph[node]:
            reversed_graph[neighbor].append(node)

    for node in range(num_nodes):
        if not visited[node]:
            dfs1(node)

    visited = [False] * num_nodes
    components = []

    while stack:
        node = stack.pop()
        if not visited[node]:
            component = set()
            dfs2(node, component)
            components.append(component)

    return components

graph = [[1], [2, 3, 4], [0, 3], [5], [5, 6], [3], [4, 7], [5, 6]]
result = strongly_connected_components(graph)
print(result)  

