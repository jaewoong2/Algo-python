# 스택
# 먼저 들어 온 데이터가 나중에 나가는 형식의 자료구조 (선입후출)

# 큐
# 선입선출 자료 구조

# 재귀함수
# 스택에 쌓여서 먼저 들어온 데이터가 가장 나중에 나가는 형식으로 함수가 호출된다


# 팩토리얼 구현 예제
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


# 최대공약수 계산 (유클리도 호제법) 예제
def gcd_recursive(a, b):
    if a % b == 0:
        return b
    else:
        return gcd_recursive(b, a % b)

# dfs
# 깊이 우선 탐색
# 스택자료구조(재귀함수를 이용)
# 탐색 시작 노드를 스택에 삽입하고 방문 처리를 합니다.
# 2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고
# 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 더이상 2번의 과정을 수행 할 수 없을때 까지 반복한다.
def dfs_while(graph, start):
    stack = []
    visited = []
    stack.append(start)
    while len(stack) > 0:
        top = stack.pop()
        if top not in visited:
            visited.append(top)
            stack += graph[top]
    print((visited))

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end= ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
# dfs(graph, 1, visited)
dfs_while(graph, 1)

# BFS (너비 우선 탐색)
# 큐 자료구조를 이용

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    print(queue)
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# bfs(graph, 1, visited)

def ice_beverage():
    def dfs(x, y):
        if x <= -1 or x >= n or y <= -1 or y >=m:
            return False
        if graph[x][y] == 0:
            graph[x][y] = 1
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
        return False

    n, m = map(int, input().split())

    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1

    print(result)

ice_beverage()

def exit_room():
    def bfs(x, y):
        queue = deque()
        queue.append(x, y)

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.appned((nx, ny))

        return graph[n - 1][m - 1]
    n, m = map(int, input.split())

    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    print(bfs(0, 0))