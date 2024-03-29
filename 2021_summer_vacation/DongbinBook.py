# 동빈북

# 1. 큰 수의 법칙 p92

# 개인 풀이
def rules_of_big_number(N, M, K, numbers):
    result = 0
    maxes = [x for x in numbers if x == max(numbers)]

    if len(maxes) > 1:
        return maxes[0] * M

    else:
        max_f = maxes[0]
        max_s = sorted([x for x in numbers if x < max(numbers)], reverse= True)[0]
        i = 0
        while i < M:
            j = 0
            while j < K:
                result += max_f
                j +=1
                i +=1
            result += max_s
            i += 1

        return result

# print(rules_of_big_number(5, 7, 2, [3, 4, 3, 4, 3]))

# 풀이 (수정)

def rules_of_big_number_2(N, M, K, numbers):
    numbers.sort()
    result = 0
    first = numbers[-1]
    second = numbers[-2]
    i = 0
    while i < M:
        j = 0
        while j < K and i < M:
            result += first
            j += 1
            i += 1
        if i < M:
            result += second
            i += 1

    return result

# print(rules_of_big_number_2(5, 7, 2, [3, 4, 3, 4, 3]))

# 숫자 카드 게임 p. 96

# 개인 풀이

def game_of_number_card(N, M, cards):
    newCards = []
    for row in range(N):
        temp = []
        for col in range(M):
            temp.append(cards.pop(0))
        newCards.append(temp)

    mines = 0
    for row in range(N):
        mines = max(mines, min(newCards[row]))
    return mines

# print(game_of_number_card(2, 4, [7, 3, 1, 8, 3, 3, 3, 4]))


# 1이 될 때 까지
def until_one(N, K):
    count = 0

    while N > K:
        while N % K != 0:
            N -= 1
            count += 1

        N = N // K
        count += 1

    if N > 1:
        count += 1
        N -= 1

    return count

# print(until_one(25, 3))


def until_one_2(N, K):
    result = 0

    while N >= K:
        while N % K != 0:
            N -= 1
            result += 1
        N //= K
        result += 1


    while N > 1:
        N -= 1
        result += 1

    return result

# print(until_one_2(27, 3))

# 상하좌우 p.110

def LRUD(n, moves):
    now = [1, 1]
    for move in moves:
        if move == 'L':
            if now[0] != 1:
                now = [now[0] - 1, now[1]]
        elif move == 'R':
            if now[0] != n:
                now = [now[0] + 1, now[1]]
        elif move == 'U':
            if now[1] != 1:
                now = [now[0], now[1] - 1]
        elif move == 'D':
            if now[1] != n:
                now = [now[0], now[1] + 1]

    return list(reversed(now))

# print(LRUD(5, ['R','R','R','U','D','D']))

# 왕실의 나이트 p.115
def knight_of_kingdom(position):
    n = 8
    col = {x: i + 1 for i, x in enumerate('abcdefgh')}
    now = [int(position[1]), col[position[0]]]
    count = 8
    moves = [[-2, +1], [-2, -1], [2, 1], [2, -1]]

    for move in moves:
        reversedMove = list(reversed(move))
        if now[0] + move[0] < 1 or now[1] + move[1] > n or now[0] + move[0] > n or now[1] + move[1] < 1:
            count -= 1

        if now[0] + reversedMove[0] < 1 or now[1] + reversedMove[1] > n or now[0] + reversedMove[0] > n or now[1] + reversedMove[1] < 1:
            count -= 1

    return count

# print(knight_of_kingdom('a1'))

# 게임 개발 p.118 (다시풀기)
def development_game(n, m, position, map):
    point = { 0: 'North', 1: "East", 2: "South", 3: "West" }
    cash = []
    stop = [False]

    def view_point(view):
        if view == 0: return 3
        return view - 1

    def find_land(pos):
        row, col, view = pos
        moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        flag = ''
        for move in moves:
            if [row + move[0], col + move[1]] in cash or map[row + move[0]][col + move[1]] == 1:
                flag += '1'

        if flag == '1111':
            if point[view] == 'North':
                if [row - 1, col] not in cash and row - 1 > 0 and map[row + 1][col] == 0:
                    row += 1

                if map[row + 1][col] == 1:
                    stop[0] = True

            elif point[view] == 'East':
                if [row, col + 1] not in cash and col + 1 <= m and map[row][col - 1] == 0:
                    col -= 1
                if map[row][col - 1] == 1:
                    stop[0] = True
            elif point[view] == 'South':
                if [row + 1, col] not in cash and row + 1 <= n and map[row - 1][col] == 0:
                    row -= 1
                if map[row - 1][col] == 1:
                    stop[0] = True
            elif point[view] == 'West':
                if [row, col - 1] not in cash and col - 1 > 0 and map[row][col + 1] == 0:
                    col += 1
                if map[row][col + 1] == 1:
                    stop[0] = True


        return [row, col, view]


    def canMove(pos):
        row, col, view = find_land(pos)
        view = view_point(view)
        nextPosition = moving([row, col, view])
        if [nextPosition[0], nextPosition[1]] not in cash:
            cash.append([nextPosition[0], nextPosition[1]])
        return nextPosition


    def moving(pos):
        row, col, view = pos
        if point[view] == 'North':
            if [row - 1, col] not in cash and row - 1 > 0 and map[row - 1][col] == 0:
                row -= 1
        elif point[view] == 'East':
            if [row, col + 1] not in cash and col + 1 <= m and map[row][col + 1] == 0:
                col += 1
        elif point[view] == 'South':
            if [row + 1, col] not in cash and row + 1 <= n and map[row + 1][col] == 0:
                row += 1
        elif point[view] == 'West':
            if [row, col - 1] not in cash and col - 1 > 0 and map[row][col - 1] == 0:
                col -= 1

        return [row, col, view]

    while not stop[0]:
        position = canMove(position)
    return len(cash)

# print(development_game(4, 4, [1, 1, 0], [[1,1,1,1], [1,0,0,1], [1,1,0,1], [1,1,1,1]]))


# 떡볶이 떡 만들기 (p.201 이진탐색)

def dduckBbooki(n, m, arr):
    start = 0
    end = arr[n - 1]
    result = 0

    while start <= end:
        mid = (start + end) // 2

        total = sum([x - mid for x in arr if x > mid])

        if total > m:
            start = mid + 1

        elif total < m:
            end = mid - 1
        else:
            result += mid
            break

    return result

# print(dduckBbooki(4, 6, [19, 15, 10, 17]))


def Fibonacci_wrpaeer(n):
    dp = { 1: 1, 2: 1 }
    def Fibonacci(n):
        if n in dp:
            return dp[n]
        if n > 2:
            dp[n] =  Fibonacci(n - 1) + Fibonacci(n - 2)
        return dp[n]
    return Fibonacci(n)

# print(Fibonacci_wrpaeer(3))

def money_change(n, m, moneys):
    dp = {x: float('inf') for x in range(m + 1)}
    for money in moneys:
        dp[money] = 1

    def recursive(pay):
        if pay not in dp:
            return 0

        if dp[pay] != float('inf'):
            return dp[pay]

        for money in moneys:
            if recursive(pay - money) != 0:
                dp[pay] = min(dp[pay], recursive(pay - money) + 1)

        return dp[pay]

    return recursive(m) == float('inf') and -1 or recursive(m)


# print(money_change(3, 4, [3, 5, 7]))


def dijkstra(graph, start):
    costs = { node: float('inf') for node in graph }
    costs[start] = 0
    visited = [start]
    for node in graph[start]:
        costs[node] = graph[start][node]

    while len(visited) < len(graph):
        minimum_cost, minimum_node = min([[costs[x], x] for x in costs if x not in visited], key=lambda x: x[0])
        visited.append(minimum_node)

        for node in graph[minimum_node]:
            costs[node] = min(minimum_cost + graph[minimum_node][node], costs[node])

    return costs

graph = {
    1: {2: 2, 3: 5, 4: 1},
    2: {3: 3, 4: 2},
    3: {2: 3, 6: 5},
    4: {3: 3, 5: 1},
    5: {3: 1, 6: 2},
    6: {}
}

# print(dijkstra(graph, 1))


def Floyd(graph):
    new_graph = {x: { y: float('inf') for y in graph } for x in graph}

    for x in graph:
        for y in graph[x]:
            new_graph[x][x] = 0
            new_graph[x][y] = graph[x][y]
            new_graph[y][x] = graph[x][y]


    for k in new_graph:
        for i in new_graph:
            for j in new_graph[i]:
                new_graph[i][j] = min(new_graph[i][k] + new_graph[k][j], new_graph[i][j])

    return new_graph


# print(Floyd(graph))



def future_city(n, x, k, graph):
    table = {node + 1: {vertex + 1: float('inf') for vertex in range(n)} for node in range(n)}

    for node in range(n):
        for vertex in range(n):
            if node + 1 in graph:
                if vertex + 1 in graph[node + 1]:
                    table[node + 1][vertex + 1] = graph[node + 1][vertex + 1]
                    table[vertex + 1][node + 1] = graph[node + 1][vertex + 1]

    for k in graph:
        for i in graph:
            for j in graph:
                table[i][j] = min(table[i][j], table[i][k] + table[k][j])

    return table[1][k] + table[k][x]

# print(future_city(5, 4, 5, {1: {2: 1, 3: 1, 4: 1}, 2: {4: 1}, 3: {4: 1, 5: 1}, 4: {5: 1} }))


# 미래도시, 플로이드 워셜 알고리즘 사용
def future_city_2(n, x, k, graph):
    matrix = {i: {j: float('inf') for j in range(1, n + 1)} for i in range(1, n + 1)}

    for node in graph:
        for edge in graph[node]:
            matrix[node][edge] = 1
            matrix[edge][node] = 1

    for pivot in matrix:
        for node in matrix:
            for edge in matrix[node]:
                matrix[node][edge] = min(matrix[node][edge], matrix[node][pivot] + matrix[pivot][edge])

    return matrix[1][k] + matrix[k][x]


# print(future_city_2(5, 4, 5, {1: {2: 1, 3: 1, 4: 1}, 2: {4: 1}, 3: {4: 1, 5: 1}, 4: {5: 1} }))

# 전보
def telegram(n, m, c, graph):
    visited = []
    stack = [(c, 0)]
    max_time = 0

    while stack:
        node, cost = stack.pop()

        visited.append(node)
        max_time = max(cost, max_time)

        if node in graph:
            for v in graph[node]:
                if v not in visited:
                    stack.append((v, cost + graph[node][v]))

    return [len(visited) - 1, max_time]


# print(telegram(3, 2, 1, {1: {2: 4, 3: 2}}))

# 서로소 집합
class disjoint_set():
    def __init__(self, n):
        self.U = []
        # n개의 node 생성 (index ==> node 의 번호)
        for i in range(n + 1):
            self.U.append(i)

    # U[nodeIndex] ==> node 의 parent
    # U[nodeIndex] == nodeIndex 같으면 본인이 Root Parent
    def find(self, i):
        j = i
        while self.U[j] != j:
            j = self.U[j]
        return j

    def equal(self, p, q):
        if p == q:
            return True
        return False

    # p, q 를 Union ==> 더 작은 값이 큰 값의 부모가 됨
    def union(self, p, q):
        parent_p = self.find(p)
        parent_q = self.find(q)

        if parent_p < parent_q:
            self.U[parent_q] = parent_p
        else:
            self.U[parent_p] = parent_q


def disjointExample():
    dis_joint_set = disjoint_set(6)
    dis_joint_set.union(1, 4)
    dis_joint_set.union(2, 3)
    dis_joint_set.union(2, 4)
    dis_joint_set.union(5, 6)

    for i in range(1, 7):
        print(i, '번 의 부모 ==>', dis_joint_set.find(i))


# print(disjointExample())

# 크루스칼 알고리즘 (서로소 집합 사용)(
def kruskalAlgorithm(edges):
    disJ_set = disjoint_set(7)
    edges = sorted(edges, key=lambda x: x[2])
    total = 0

    for edge in edges:
        a, b, cost = edge
        parent_a = disJ_set.find(a)
        parent_b = disJ_set.find(b)

        if parent_a != parent_b:
            disJ_set.union(a, b)
            total += cost

    return total


# print(kruskalAlgorithm([[1, 2, 29], [1, 5, 75], [2, 3, 35], [2, 6, 34], [3, 4, 7], [4, 6, 23], [4, 7, 13], [5, 6, 53], [6, 7, 25]]))

# 위상정렬 (in edge ==> 0 and visited 추가, 해당 노드 제거 ==> 해당 노드가 접근하는 간선 제거 (in edge 1을 줄인다))
def topologySort(vertex, edge, graph):
    in_edge = [0 for _ in range(vertex + 1)]
    queue = []
    visited = []

    for n in range(1, vertex + 1):
        for v in graph:
            if n in graph[v]:
                in_edge[n] += 1

    for i in range(1, vertex + 1):
        if in_edge[i] == 0:
            visited.append(i)
            queue.append(i)

    while queue:
        node = queue.pop(0)

        if node in graph:
            for i in graph[node]:
                in_edge[i] -= 1
                if in_edge[i] == 0 and i not in visited:
                    visited.append(i)
                    queue.append(i)

    return visited

# print(topologySort(7, 8, {1: [2, 5], 2: [3, 6], 3: [4], 4: [7], 5: [6], 6: [4]}))

# 팀 결성
def team_making(n, commands):
    students = {i: i for i in range(n + 1)}
    result = []
    def find(student):
        if student != students[student]:
            return find(students[student])
        return student

    def union(a, b):
        a_team = find(a)
        b_team = find(b)

        if a_team > b_team:
            students[a_team] = b_team
        else:
            students[b_team] = a_team

    for cmd in commands:
        c, a, b = cmd
        if c == 0:
            union(a, b)
        else:
            if find(a) == find(b):
                result.append('YES')
            else:
                result.append('No')

    return result

# print(team_making(7, [[0, 1, 3], [1, 1, 7], [0, 7, 6], [1, 7, 1], [0, 3, 7], [0, 4, 2], [0, 1, 1], [1, 1, 1]]))


# 도시 분활 계획
def divide_city_plan(n, m, graph):

    def find(a, parent):
        if a != parent[a]:
            return find(parent[a], parent)
        return parent[a]

    def union(a, b, parent):
        parent_a = find(a, parent)
        parent_b = find(b, parent)

        if parent_a < parent_b:
            parent[parent_b] = parent_a
        else:
            parent[parent_a] = parent_b

    def kruskal(graph):
        max_cost = 0
        cities = {i: i for i in range(1, n + 1)}
        sorted_graph = []
        result = 0

        for node in graph:
            for vertex in graph[node]:
                sorted_graph.append([node, vertex, graph[node][vertex]])

        sorted_graph.sort(key= lambda x: x[2])

        for v in sorted_graph:
            a, b, cost = v
            if find(a, cities) != find(b, cities):
                union(a, b, cities)
                result += cost
                max_cost = cost

        return result - max_cost


    return kruskal(graph)


# print(divide_city_plan(7, 12, {
#     1: {2: 3, 3: 2, 6: 2},
#     2: {5: 2},
#     3: {2: 1, 4: 4},
#     4: {5: 3},
#     5: {1: 5},
#     6: {4: 1, 5: 3, 7: 4},
#     7: {3: 6},
# }))

def curriculum(n, lectures):
    times = {i + 1: lecture[0] for i, lecture in enumerate(lectures)}
    prerequisites = {i + 1: [x for x in lecture[1]] for i, lecture in enumerate(lectures)}
    queue = []
    results = {i + 1: 0 for i in range(n)}
    visited = []

    for i, lecture in enumerate(lectures):
        if len(prerequisites[i + 1]) == 0:
            queue.append([i + 1, times[i + 1]])
            visited.append(i + 1)

    while queue:
        v, cost = queue.pop(0)
        results[v] = cost

        for i, lecture in enumerate(lectures):
            if v in prerequisites[i + 1]:

                prerequisites[i + 1].pop(prerequisites[i + 1].index(v))
                if len(prerequisites[i + 1]) == 0 and i + 1 not in visited:
                    queue.append([i + 1, cost + times[i + 1]])
                    visited.append(i + 1)

    return results

# print(curriculum(5, [[10, []], [10, [1]], [4, [1]], [4, [3, 1]], [3, [3]]]))

# 모험가 길드 p.311
def adventure_guild(n, adventurers: list):
    groups = 0
    adventurers.sort()
    stack = []
    for adventurer in adventurers:
        stack.append(adventurer)
        if stack and len(stack) == stack[-1]:
            groups +=1
            stack = []

    return groups

# print(adventure_guild(5, [2, 3, 1, 2, 2]))

# 곱하기 혹은 더하기
def plus_or_multiple(number: str):
    temp = 0
    for n in number:
        num = int(n)
        if temp == 0 and num > 0:
            temp = num
        elif num > 0 and temp != 0:
            temp *= num

    return temp

# print(plus_or_multiple("567"))

# 문자열 뒤집기
def string_reverse(string: str):
    newString = []
    temp = [string[0]]
    numberOfOne = 0
    numberOfZero = 0

    for i in range(1, len(string)):
        if string[i] == temp[0]:
            temp.append(string[i])
        if string[i] != temp[0]:
            newString.append(temp)
            temp = [string[i]]
    newString.append(temp)

    for s in newString:
        if s[0] == '0':
            numberOfZero += 1
        else:
            numberOfOne += 1

    return min(numberOfOne, numberOfZero)

# print(string_reverse("0001100"))

def not_make_money(coins):
    dp = [[] for _ in range(sum((coins)))]

    for i, coin in enumerate(coins):
        dp[coin] = [c for j, c in enumerate(coins) if i != j]

    for _ in range(1, len(coins)):
        for key in range(len((dp))):
            for i, coin in enumerate(dp[key]):
                if key + coin < sum(coins):
                    dp[key + coin] = [c for j, c in enumerate(dp[key]) if i != j]

    for i in range(1, len(dp)):
        if not dp[i]:
            return i

# print(not_make_money([3, 2, 1, 1, 9]))

def choice_ball(n, m, balls):
    choice = []
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if balls[i] != balls[j]:
                choice.extend([i ,j])
                if len(choice) == 2:
                    choice = []
                    count += 1

    return count

# print(choice_ball(8, 5, [1, 5, 4, 3, 2, 4 , 5, 2]))
