def main_floyd():
    INF = 999
    matrix = [
        [0, 1, INF, 1, 5],
        [9, 0, 3, 2, INF],
        [INF, INF, 0, 4, INF],
        [INF, INF, 2, 0, 3],
        [3, INF, INF, INF, 0],
    ]
    def path(p, u, v):
        if (p[u][v] != -1):
            path(p, u, p[u][v])
            print('v%d'%(p[u][v]), end ="-> ")
            path(p, p[u][v], v)

    def floyd(D):
        n = len(D)
        path_node = [[-1] * n for _ in range(n)]

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if D[i][j] > D[i][k] + D[k][j]:
                        D[i][j] = D[i][k] + D[k][j]
                        path_node[i][j] = k
        return D, path_node
    floyd(matrix)

    for i in range(len(matrix)):
        print(matrix[i])

# main_floyd()


def doublexn():
    def solution(n):
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(dp)):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n]

    return solution(4)

# print(doublexn())

def tri():
    def solution(triangle):
        def df(row, i):
            if row == len(triangle):
                return 0

            temp = 0

            for col in range(len(triangle[row])):
                if col == i or col + 1 == i:
                    temp = max(temp, triangle[row][col] + df(row + 1, col))
                    print(temp, row, col)

            return temp



        return df(0, 0)

    return solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])

# print(tri())

def dijkstra(W):
    INF = 9999
    n = len(W) - 1
    F = []

    touch = [-1] * (n + 1)
    length = [-1] * (n + 1)

    for i in range(2, n+ 1):
        touch[i] = 1
        length[i] = W[1][i]

    for _ in range(n - 1):
        min_value = INF
        v_near = -1

        # 노드를 돌며, 탐색하지 않은 노드중에서 가장 가까운 노드를 찾는다.
        for i in range(2, n + 1):
            if 0 <= length[i] < min_value:
                min_value = length[i]
                v_near = i

        if v_near >= 0:
            # 찾은 노드를 (현재위치, 현재위치에서 가까운 위치, 비용) 의 형태로
            # 탐색배열에 넣어준다
            edge = (touch[v_near], v_near, W[touch[v_near]][v_near])
            F.append(edge)

        for i in range(2, n + 1):
            # 노드를 탐색하며, v_near 를 경유해서 가는 경우와 경유해서 가지 않는 경우의
            # 비용을 비교해서 만약 v_near 를 경유하는 경우가 더 비용이 낮다면,
            # 그 노드를 경유하는 경우를 v_near 로 갱신한다. (비용도 갱신)
            if length[i] > length[v_near] + W[v_near][i]:
                length[i] = length[v_near] + W[v_near][i]
                touch[i] = v_near
            length[v_near] = -1

        return F

def Nqueen():
    def is_possible(now_row, move_to, col):

        # 여태 작업했던 row 들이 갖고 있는 col 중 에서 `현재 row 가 움직이려는 열(move_to) or 대각선
        # 이 있으면 False`
        for i in range(now_row):
            if move_to == col[i] or abs(move_to - col[i]) == now_row - i:
                return False
        return True

    def dfs(n, col, now_row):

        # 현재 진행하는 row 가 끝까지 가면 성공
        if n == now_row:
            return 1

        count = 0

        for i in range(n):
            if is_possible(now_row, i, col):
                # 만약, 이전에 작업한 것 중에서 대각선에 있거나 같은열에 있는게 없으면,
                # 현재 진행 열에 행의 값을 넣어준다.
                # 그리고 다음 열에서 같은 일을 진행 해준다.
                col[now_row] = i
                count += dfs(n, col, now_row + 1)

        return count


    def solution(n):
        # col[i] = i번쩨 row 의 col 위치
        col = [0] * n

        return dfs(n, col, 0)

    return solution(4)

# print(Nqueen())


def sum_of_subsets_container():
    w = [0, 3, 4, 5, 6]
    subsets = []
    W = 12

    def sum_of_subsets(i, weights, total):
        if is_promising(i, weights, total):
            if weights == W:
                print(subsets)
            else:
                subsets.append(w[i + 1])
                sum_of_subsets(i + 1, weights + w[i + 1], total - w[i + 1])
                subsets.pop()
                sum_of_subsets(i + 1, weights, total - w[i + 1])

    def is_promising(i, weight, total):
        if (weight == W or weight + w[i + 1] <= W) and (weight + total >= W):
            return True
        return False

    return sum_of_subsets(0, 0, sum(w))

# (sum_of_subsets_container())


def express_by_N_solution(N, number):
    dp = [[0]]
    dp += [[int(str(N) * i)] for i in range(1, 9)]
    def recursive_func(i):
        if i > 9 or i == 9 and number not in dp[8]:
            return -1

        if number in dp[i - 1]:
            return i - 1

        for k in range(1, i):
            for left in dp[i - k]:
                for right in dp[k]:
                    if left > 0 and right > 0:
                        divied = left // right > 0 and left // right or 0
                        divied2 = right // left > 0 and right // left or 0
                        minus = left - right > 0 and left - right or 0
                        minus2 = right - left > 0 and right - left or 0
                        plus = left + right > 0 and left + right or 0
                        mul = left * right > 0 and left * right or 0
                        dp[i] += list(x for x in set([divied, divied2, minus2, minus, plus, mul]) if x > 0)

        return recursive_func(i + 1)

    ans = recursive_func(0)

    if ans <= 8:
        return ans

    return -1

# print(express_by_N_solution(5, 31168))


def int_triangle(triangle):
    # dp = [[x for x in triangle[i]] for i in range(len(triangle))]

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] = triangle[i][j] + triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] = triangle[i][j] + triangle[i - 1][j - 1]
            else:
                triangle[i][j] = triangle[i][j] + max(triangle[i - 1][j - 1], triangle[i - 1][j])


    # def dfs(i, col):
    #     if i == len(triangle):
    #         return
    #
    #     dp[i][col] = max(dp[i][col], triangle[i][col] + dp[i - 1][col])
    #     dfs(i + 1, col)
    #
    #     dp[i][col + 1] = max(dp[i][col + 1], triangle[i][col + 1] + dp[i - 1][col])
    #     dfs(i + 1, col + 1)
    #
    # dfs(1, 0)
    return max(triangle[-1])


# print(int_triangle([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))


def go_to_school():
    def solution(m, n, puddles):
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][1] = 1
        dp[1][0] = 1
        puddles = [[x - 1, y - 1] for x, y in puddles]

        for row in range(n):
            for col in range(m):
                if row > 0 or col > 0:
                    if [col , row] not in puddles:
                        if [col - 1, row] in puddles:
                            dp[row][col] += dp[row - 1][col]
                        elif [col, row - 1] in puddles:
                            dp[row][col] += dp[row][col - 1]
                        else:
                            dp[row][col] += dp[row - 1][col] + dp[row][col - 1]
        return dp[n -1][m - 1] % 1000000007

    # print(solution(2, 2, []), 2)
    # print(solution(3, 3, []), 6)
    # print(solution(3, 3, [[2, 2]]), 2)
    # print(solution(4, 3, [[1, 3], [3, 1]]), 7)
    # print(solution(3, 3, [[1, 3]]), 5)
    # print(solution(3, 3, [[1, 3], [3, 1]]), 4)
    # print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
    # print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
    # print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0)
    # print(solution(4, 4, [[3, 2], [2, 4]]), 7)
    # print(solution(100, 100, []), 690285631)
    # return solution(4, 3, [[2, 2]])
#
# print(go_to_school())


def very_far_nodes():
    def solution(n, edge):
        import collections
        queue = collections.deque({1})
        visit = [False] * (n + 1)
        visit[1] = True

        graph = {}

        for i in range(n):
            graph[i + 1] = set()

        for f, t in edge:
            graph[f].add(t)
            graph[t].add(f)

        result = set()

        while queue:
            flag = False
            for _ in range(len(queue)):
                v = queue.popleft()
                temp = [x for x in graph[v] if visit[x] == False]
                queue.extend(temp)
                for x in graph[v]:
                    visit[x] = True

                if len(temp) == 0:
                    if not flag:
                        result.add(v)
                else:
                    flag = True
                    result = set()

        return len(result)


    return solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])

# print(very_far_nodes())

def rank():
    def solution(n, results):
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        results = [[x - 1, y - 1] for x, y in results]


        for w, l in results:
            matrix[w][l] = 1
            matrix[l][w] = -1

        for k in range(n):
            for row in range(n):
                for col in range(n):
                    if row != col:
                        if matrix[row][k] == 1 and matrix[k][col] == 1:
                            matrix[row][col] = 1
                            matrix[col][row] = -1
                        if matrix[row][k] == -1 and matrix[k][col] == -1:
                            matrix[col][row] = 1
                            matrix[row][col] = -1

        for i in range(len(matrix)):
            print(matrix[i])

        return len([y for y in [len([x for x in matrix[i] if x != 0]) for i in range(len(matrix))] if y == n - 1])


    return solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])

# print(rank())

def very_long_palindrome():
    def solution(s):
        max_palindrome = 0

        for i in range(len(s)):
            # if max_palindrome[i - 1] == len(s_array[i - 1:]):
            #     break
            array = s[i:]

            if len(array) < max_palindrome:
                break

            while array:
                if len(array) < max_palindrome:
                    break

                if array == array[::-1]:
                    max_palindrome = len(array)
                    break
                else:
                    array = array[:len(array) - 1]



        return (max_palindrome)

    return solution("abacde")

print(very_long_palindrome())