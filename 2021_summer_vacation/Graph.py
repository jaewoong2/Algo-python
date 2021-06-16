graph = {
    1: {3, 4},
    2: {3, 4, 5},
    3: {1, 5},
    4: {1},
    5: {2, 6},
    6: {3, 5}
}

def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        v = stack.pop()
        if v not in visited:
            stack.extend(graph[v])
            visited.append(v)

    return visited

def recursive_dfs(graph, root, visited):
    for n in graph[root]:
        if n not in visited:
            visited.append(n)
            recursive_dfs(graph, n, visited)

    return visited

def bfs(graph, root):
    import collections
    queue = collections.deque([root])
    visited = []

    while queue:
        v = queue.popleft()

        if v not in visited:
            visited.append(v)
            queue.extend(graph[v])


    return visited

print(dfs(graph, 1))
print(recursive_dfs(graph, 1, [1]))
print(bfs(graph, 1))
