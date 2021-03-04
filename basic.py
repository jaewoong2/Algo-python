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
                # 그리고 다음 열에서 같은 일을 진행해준다.
                col[now_row] = i
                count += dfs(n, col, now_row + 1)

        return count


    def solution(n):
        # col[i] = i번쩨 row 의 col 위치
        col = [0] * n

        return dfs(n, col, 0)

    return solution(4)

print(Nqueen())