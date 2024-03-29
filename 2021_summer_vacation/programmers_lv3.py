
def n_queen(n):
    answer = []
    def is_promising(row, col, result):
        # result = [row, col][]
        flag = True
        for v in result:
            pre_row, pre_col = v
            if flag:
                if row == pre_row or col == pre_col or abs(col - pre_col) == abs(row - pre_row):
                    # 같은 열, 같은 행, 대각선
                    flag = False
        return flag

    def dfs(result, row):
        if len(result) == n:
            answer.append(1)
        else:
            for col in range(n):
                if is_promising(row, col, result):
                    dfs(result + [[row, col]], row + 1)

    dfs([], 0)

    return len(answer)

# print(n_queen(4))

def sticker_attach(sticker):
    if len(sticker) > 1:
        length = len(sticker)
        # dp[index] = index 번 째까지 스티커를 붙혔을 때 최대 값
        dp = [0] * length
        dp_ = [0] * length

        # 0번째 스티커를 붙이는 경우 (맨 마지막 스티커를 버리는 경우)
        dp[0] = sticker[0]
        dp[1] = dp[0]
        for i in range(2, length - 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])

        # 0번째 스티커를 안 붙이는 경우 (맨 마지막 스티커를 붙이는 경우)
        dp_[0] = 0
        dp_[1] = sticker[1]
        for i in range(2, length):
            dp_[i] = max(dp_[i - 1], dp_[i - 2] + sticker[i])


        return max(max(dp), max(dp_))
    return max(sticker)

# print(sticker_attach([14, 6, 5, 11, 3, 9, 2, 10]))

def very_far_node(n, vertex):
    from collections import deque
    graph = {i: [] for i in range(1, n + 1)}
    queue = deque([[1, 0]])
    visited = [False for _ in range(0, n + 1)]
    visited[1] = True
    result = [1, 0]

    for v in vertex:
        a, b = v
        graph[a].append(b)
        graph[b].append(a)

    while queue:
        v, depth = queue.popleft()

        for node in graph[v]:
            if not visited[node]:
                queue += [[node, depth + 1]]
                visited[node] = True


        if result[1] == depth:
            result = [result[0] + 1, depth]

        elif result[1] < depth:
            result = [1, depth]

    return result[0]

# print(very_far_node(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

def goto_school(m, n, puddles):
    board = [[0 for _ in range(m)] for _ in range(n)]
    puddles = [[puddle[1] - 1, puddle[0] - 1] for puddle in puddles]

    for col in range(m):
        if [0, col] not in puddles:
            board[0][col] = 1
        else:
            break

    for row in range(n):
        if [row, 0] not in puddles:
            board[row][0] = 1
        else:
            break

    for row in range(1, len(board)):
        for col in range(1, len(board[row])):
            if [row, col] not in puddles:
                if [row - 1 , col] in puddles and [row, col - 1] in puddles:
                    board[row][col] = 0
                elif [row - 1, col] in puddles:
                    board[row][col] = (board[row][col - 1]) % 1000000007
                elif [row, col - 1] in puddles:
                    board[row][col] = (board[row - 1][col]) % 1000000007
                else:
                    board[row][col] = (board[row - 1][col] + board[row][col - 1]) % 1000000007

    return board[n - 1][m - 1]

# print(goto_school(4, 3, [[2, 2]]))

# 투 포인트 사용
def shopping_gems(gems):
    length = len(gems)
    gems_kinds = set(gems)
    counts = {gem: 0 for gem in gems}
    curr = {gems[0]}
    counts[gems[0]] = 1
    answer = [0, length - 1]
    start = 0
    end = 0

    if len(gems_kinds) == 1:
        return [1, 1]

    while start < length and end < length:
        if len(curr) < len(gems_kinds):
            end += 1
            if end == length:
                break
            counts[gems[end]] += 1
            curr.add(gems[end])
        else:
            if answer[1] - answer[0] > end - start:
                answer = [start, end]
            start += 1
            if counts[gems[start - 1]] > 1:
                counts[gems[start - 1]] -= 1
            else:
                counts[gems[start - 1]] = 0
                curr.remove(gems[start - 1])

    return [answer[0] + 1, answer[1] + 1]

# print(shopping_gems(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))

# 택시 합승 요금
def taxi_together(n, s, a, b, fares):
    import heapq
    graph = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
    minimum = float('inf')

    for fare in fares:
        x, y, cost = fare
        graph[x][y] = cost
        graph[y][x] = cost

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != j:
                    graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
                else:
                    graph[i][j] = 0

    queue = [[cost, i] for i, cost in enumerate(graph[s])]

    while queue:
        cost, node = heapq.heappop(queue)
        minimum = min(minimum, cost + graph[node][a] + graph[node][b])

    return minimum

# print(taxi_together(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))

# 야근지수
def night_work(works, n):
    if sum(works) <= n:
        return 0

    import heapq
    values = [-1 * x for x in works]
    heapq.heapify(values)

    while n > 0:
        v = heapq.heappop(values)
        n -= 1
        heapq.heappush(values, v + 1)

    return sum([x * x for x in values])

# print(night_work([4, 3, 3], 4))

# 경주로 건설 # 틀린 풀이
def make_race_road(board):
    length = len(board)
    corners = []
    rights = []
    minimum = float('inf')
    directions = {'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}

    def dfs(position, prev):
        row, col, direction = position

        for dir in directions:
            dy, dx = directions[dir]

            if row + dy == length - 1 and col + dx == length - 1:
                corner = 0
                result = prev + [[row + dy, col + dx, dir]]
                for i in range(1, len(result)):
                    if result[i][2] != result[i - 1][2]:
                        corner += 1
                corners.append(corner)
                rights.append(len(result))

            elif 0 <= row + dy < length and 0 <= col + dx < length:
                if board[row + dy][col + dx] == 0:
                    if [row + dy, col + dx] not in [x[0: 2] for x in prev]:
                        dfs([row + dy, col + dx, dir], prev + [[row, col, direction]])

    dfs([0, 0, 'R'], [])
    dfs([0, 0, 'D'], [])

    for i in range(len(corners)):
        minimum = min(minimum, corners[i] * 500 + rights[i] * 100)


    return minimum


# print(make_race_road(	[[0, 0, 0], [0, 0, 0], [0, 0, 0]]))

def make_line(n, k):
    def factorial(num):
        value = 1
        for n in range(1, num + 1):
            value = value * n
        return value

    candidate = [i + 1 for i in range(n)]
    result = []
    number = n - 1
    while len(result) < n:
        per_num_number = factorial(number)
        p = k // per_num_number
        k = k % per_num_number
        if k == 0:
            p -= 1
        result.append(candidate.pop(p))
        number -= 1

    return result

# print(make_line(3, 5))

# 틀린 풀이(효율성)
def judge_for_entrance(n, times):
    result = 0
    # 시작, 끝
    processes = [[0, times[i]] for i in range(len(times))]
    while n > 0:
        minimum = [float('inf'), -1]
        for i, process in enumerate(processes):
            start, end = process
            if minimum[0] > end:
                minimum = [end, i]

        processes[minimum[1]][0] = minimum[0]
        processes[minimum[1]][1] = minimum[0] + times[minimum[1]]
        n -= 1
        result = [minimum[1]][0] = minimum[0]

    return result

# print(judge_for_entrance(6, [7, 10]))

# 경주로 건설
def make_load(board):
    # start = [row, col, cost, direction]
    def dfs(start):
        # table[row][col] => minimum cost
        table = [[float('inf') for _ in range(len(board))] for _ in range(len(board))]
        # 0: left 1: right 2: down
        list_dx = [-1, 0, 1, 0]
        list_dy = [0, 1, 0, -1]
        stack = [start]
        table[start[0]][start[1]] = start[2]
        while stack:
            row, col, cost, direction = stack.pop()

            for i in range(len(list_dy)):
                dx = list_dx[i]
                dy = list_dy[i]

                if (0 <= row + dy < len(board)) and (0 <= col + dx < len(board)):
                    if board[row + dy][col + dx] == 1:
                        continue

                    if direction != i:
                        if table[row + dy][col + dx] > cost + 600:
                            table[row + dy][col + dx] = cost + 600
                            stack.append([row + dy, col + dx, cost + 600, i])
                    else:
                        if table[row + dy][col + dx] > cost + 100:
                            table[row + dy][col + dx] = cost + 100
                            stack.append([row + dy, col + dx, cost + 100, i])

        return table[-1][-1]

    return(min(dfs([0, 0, 0, 1]), dfs([0, 0, 0, 2])))

# print(make_load([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))

def entrance(n, times):
    minimum = 1  # 최소 시간
    maximum = max(times) * n  # 최대시간
    answer = 0

    while minimum < maximum:
        count = 0
        middle = (minimum + maximum) // 2

        for time in times:
            count += middle // time
            if count >= n:
                break

        if count >= n:
            answer = middle
            maximum = middle - 1
        else:
            minimum = middle + 1

    return answer

# print(entrance(6, [7, 10]))

def network(n, computers):
    answer = 1
    visited = [False for _ in range(n)]
    stack = [0]
    visited[0] = True

    while stack:
        curr = stack.pop()

        for i, next in enumerate(computers[curr]):
            if i != curr and next == 1 and not visited[i]:
                stack.append(i)
                visited[i] = True

        if not stack:
            for i in range(len(visited)):
                if not visited[i]:
                    answer += 1
                    stack.append(i)
                    visited[i] = True
                    break

    return answer

# print(network(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))


def pyramid_toothbrush(enroll, referral, seller, amount):
    graph = {}
    init_incomes = {}
    result = {}

    for i in range(len(enroll)):
        graph[enroll[i]] = referral[i] == '-' and 'center' or referral[i]
        result[enroll[i]] = 0


    for i in range(len(seller)):
        init_incomes[seller[i] + str(i)] = amount[i] * 100


    for i in range(len(seller)):
        name = seller[i]
        income = amount[i] * 100
        while name in graph:
            tax = income // 10
            result[name] += (income - tax)
            name = graph[name]
            income = tax

    return [result[x] for x in result]

# print(pyramid_toothbrush(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
#                          ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
#                          ["young", "john", "tod", "emily", "mary"],
#                          [12, 4, 2, 5, 10]))







