# 1. 출발 노드를 설정한다
# 2. 최단 거리 테이블을 초기화 한다
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다

# 그리디 알고리즘에 속하게 된다.

def get_dijkstra(graph, start):
        INF = int(1e9)
        distance, visited = {}, {}
        for node in graph:
            visited[node] = False
            distance[node] = INF

        def get_smallest_node():
            min_value = INF
            index = 1
            for i in graph:
                if distance[i] < min_value and not visited[i]:
                    min_value = distance[i]
                    index = i
            return index

        def dijkstra(start):
            distance[start] = 0
            visited[start] = True

            for j in graph[start]:
                distance[j] = graph[start][j]

            for node in graph:
                now = get_smallest_node()
                visited[now] = True

                for j in graph[now]:
                    cost = distance[now] + graph[now][j]

                    if cost < distance[j]:
                        distance[j] = cost
        dijkstra(start)

        for i in range(1, len(graph) + 1):
            if distance[i] == INF:
                print("infinity")
            else:
                print(distance[i], "<------", i)


graph = {
    1: {2: 2, 3: 5, 4: 1},
    2: {3: 3, 4: 2},
    3: {2: 3, 6: 5},
    4: {3: 3, 5: 1},
    5: {3: 1, 6: 2},
    6: {},
}

get_dijkstra(graph, 1)


