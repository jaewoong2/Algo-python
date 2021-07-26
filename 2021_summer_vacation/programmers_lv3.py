
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

print(shopping_gems(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))