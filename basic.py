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

# print(very_long_palindrome())

def change_the_money():
    def solution(n, monies):
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(len(monies)):
            for j in range(monies[i], n +1):
                dp[j] = dp[j] + dp[j - monies[i]]

        return dp[n] % 1000000007
    return solution(5, [1,2,5])

# print(change_the_money())

def long_jump():
    def solution(n):
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] += dp[i - 1] + dp[i - 2]

        return dp[n]

    return solution(1)

# print(long_jump())

def pirodo():
    def solution(works, n):
        import heapq
        works = list([-x for x in works])

        heapq.heapify(works)

        while n > 0:
            v = heapq.heappop(works)

            n -=1
            v += 1

            heapq.heappush(works, v)

        return sum([(-x) ** 2 for x in works])

    return solution([1, 1], 3)

# print(pirodo())

def the_best_set():
    def solution(n, s):
        mid = s // n
        if mid == 0:
            return [-1]

        array = [mid] * n
        total = sum(array)
        diff = s - total
        
        for i in range(diff):
            array[i % n] += 1

        return sorted(array)

    return solution(2, 9)

# print(the_best_set())

def hanoi():
    def solution(n):
        answer = []
        def recrusive(start, target, empty, array):
            if len(array) == 1:
                answer.append([start, target])
                return

            recrusive(start, empty, target, array[:-1])
            recrusive(start, target, empty, [array[-1]])
            recrusive(empty, target, start, array[:-1])

        recrusive(1, 3, 2, [i for i in range(n, 0, -1)])
        return answer
    return solution(2)
# print(hanoi())

def how_to_queue():
    def i_permutation(n, arr, r, limit):
        import collections
        stack = collections.deque([[i] for i in range(n)])
        result = []

        if r == 1:
            return [x for x in arr]

        while stack:
            if len(result) == limit:
                break

            curr = stack.popleft()
            for i in range(n):
                if i not in curr:
                    temp = curr + [i]
                    if len(temp) == r:
                        elements = []
                        for idx in temp:
                            elements.append(arr[idx])
                        result.append(elements)
                    else:
                        stack.append(temp)

        return result

    def solution(n, k):
        import itertools
        array = [i + 1 for i in range(n)]
        answer = list(itertools.permutations(array, n))
        # answer = list(i_permutation(len(array), array, n, k))
        return answer[-1]
    return solution(3, 5)

# print(how_to_queue())

def the_biggest_box():
    def solution(board):
        row_length = len(board)
        col_length = len(board[0])
        result = 0

        for row in range(1, row_length):
            for col in range(1, col_length):
                if board[row][col] > 0:
                    across = board[row - 1][col - 1]
                    left = board[row][col - 1]
                    up = board[row - 1][col]
                    if across > 0 and left > 0 and up > 0:
                        board[row][col] = min(across, left, up) + 1
                        result = max(board[row][col], result)

        return result ** 2

    return solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])


# print(the_biggest_box())


def traffic():
    def solution(lines: list):
        new_lines = [(
            (float(x.split(' ')[1].split(':')[0]) * 3600 +
                float(x.split(' ')[1].split(':')[1]) * 60 +
                float(x.split(' ')[1].split(':')[2])) * 1000 - float(x.split(' ')[2][:-1]) * 1000,

            float(x.split(' ')[1].split(':')[0]) * 3600 +
                  float(x.split(' ')[1].split(':')[1]) * 60 +
                  float(x.split(' ')[1].split(':')[2])
             ) for x in lines]

        new_lines = [(new_lines[i][0] + 1, new_lines[i][1] * 1000) for i in range(len(new_lines))]

        count = 0
        for j in range(len(new_lines)):
            temp_start = set()
            temp_end = set()
            s = new_lines[j]

            for i in range(len(new_lines)):
                if (new_lines[i][0] <= s[1] and (new_lines[i][1] > s[1] + 1000)) \
                        or (s[1] <= new_lines[i][0] < s[1] + 1000) \
                        or (s[1] <= new_lines[i][1] < s[1] + 1000):
                    temp_end.add(i)

                elif (new_lines[i][0] <= s[0] and (new_lines[i][1] > s[0] + 1000)) \
                        or (s[0] <= new_lines[i][0] < s[0] + 1000) \
                        or (s[0] <= new_lines[i][1] < s[0] + 1000):
                    temp_start.add(i)

            print(s)
            count = max(count, len(temp_start), len(temp_end))

        return count

    return solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])
# print(traffic())

def network():
    def solution(computers):
        graph = {node: [i for i in range(len(computers[node])) if node != i and computers[node][i] == 1] for node in range(len(computers))}
        stack = [0]
        visit = [False] * len(computers)
        visit[0] = True
        num_of_network = 1

        while stack:
            v = stack.pop()

            for node in graph[v]:
                if not visit[node]:
                    stack.append(node)
                    visit[node] = True

            for node in graph:
                if not visit[node] and len(stack) == 0:
                    num_of_network += 1
                    stack.append(node)
                    visit[node] = True
                    break

        return num_of_network

    return solution([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
# print(network())


def disc_controller():
    import heapq
    def solution(jobs):
        jobs.sort(reverse= True)
        length = len(jobs)
        result = 0
        time = 0
        tasks = []
        while jobs or tasks:
            if len(tasks) == 0:
                jobs.sort(reverse= True)
                job = jobs.pop()
                time = job[0]
                heapq.heappush(tasks, [job[1], job[0]])

            else:
                t, n = heapq.heappop(tasks)
                time += t

                temp = [i for i in range(len(jobs)) if jobs[i][0] <= time]

                for num in temp:
                    heapq.heappush(tasks, [jobs[num][1], jobs[num][0]])

                jobs = [jobs[i] for i in range(len(jobs)) if jobs[i][0] > time]

                result += (time - n)

        return result // length


#     print(solution([[0, 3], [1, 9], [2, 6]]), 9)
#     print(solution([[1, 10], [3, 3], [10, 3]]), 9)
#     print(solution( [[0, 10], [4, 10], [5, 11], [15, 2]]), 15)
#     print(solution([[0, 10]]), 10)
#     print(solution([[0, 3], [1, 9], [2, 6], [4, 3]]), 9)
#     print(solution( [[0, 1], [1, 2], [500, 6]]), 3)
#     # return solution([[0, 3], [1, 9], [2, 6]])
# print(disc_controller())


def bad_users():

    def solution(user_ids, banned_ids):
        results = []

        for banned_id in banned_ids:
            temp = []
            for user_id in user_ids:
                banned_id_length = len(banned_id)
                if banned_id_length == len(user_id):
                    flag = True
                    for idx in range(banned_id_length):
                        if banned_id[idx] != user_id[idx] and banned_id[idx] != '*':
                            flag = False
                            break
                    if flag:
                        temp.append(user_id)

            results.append(temp)

        ans = []
        def dfs(answers, level):
            if level == len(banned_ids):
                ans.append(answers)
                return

            for value in results[level]:
                if value not in answers:
                    answers.append(value)
                    dfs(answers[:], level + 1)
                    answers.pop()

        dfs([], 0)
        ans = set(''.join(sorted(x)) for x in ans)


        return len(ans)

    return solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
print(bad_users())