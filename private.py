def bfs(start):
    graph = {
        1: [2, 3, 4],
        2: [5],
        3: [5],
        4: [],
        5: [6, 7],
        6: [],
        7: [3]
    }
    from collections import deque
    queue = deque([start])
    visited = []
    while queue:
        v = queue.popleft()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                queue.append(w)

    return visited

# print(bfs(1))


def i_permutataion(n, arr, r):
    stack = [[i] for i in range(n)]
    result = []

    if r == 1:
        return [x for x in arr]

    while stack:
        curr = stack.pop()
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

# print(i_permutataion(4, "ABCD", 2))

def recursive_permutation(arr, r):
    visited = [False for _ in range(len(arr))]
    result = []

    def generate(selected, visited):
        if len(selected) == r:
            result.append(''.join(selected))
            return


        for i in range(len(arr)):
            if not visited[i]:
                selected.append(arr[i])
                visited[i] = True
                generate(selected, visited)
                visited[i] = False
                selected.pop()

    generate([], visited)
    return result

# print(recursive_permutation("ABCD", 2))


def recursive_combination(arr, r):
    chosen =[]
    if len(arr) < r:
        return chosen

    if r == 1:
        for i in range(len(arr)):
            chosen.append(arr[i])

    elif r > 1:
        for i in range(len(arr) - r + 1):
            for temp in recursive_combination(arr[i + 1:], r - 1):
                chosen.append([arr[i], temp])

    return chosen

# print(recursive_combination("ABCD", 2))

def remove_duplicate_letters(s):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_dic = {}
    for i in range(len(alpha)):
        alpha_dic[alpha[i]] = i

    count_dic = {}
    for i in range(len(s)):
        if s[i] in count_dic:
            count_dic[s[i]] += 1
        else:
            count_dic[s[i]] = 1

    stack = []

    for char in s:
        count_dic[char] -= 1

        if char in stack:
            continue

        while stack and char < stack[-1] and count_dic[stack[-1]] > 0:
            stack.pop()
        stack.append(char)


    return ''.join(stack)

# print(remove_duplicate_letters("bcabc"))


def number_of_islands(islands):
    islands = [list(x) for x in islands]
    def dfs(v):
        if v[0] >= len(islands) or v[1] >= len(islands[0]):
            return

        if islands[v[0]][v[1]] == '0':
            return

        if islands[v[0]][v[1]] == '1':
            islands[v[0]][v[1]] = '0'
            dfs([v[0] + 1, v[1]])
            dfs([v[0], v[1] + 1])

    count = 0

    for i in range(len(islands)):
        for j in range(len(islands[i])):
            if islands[i][j] == '1':
                dfs([i, j])
                count += 1

    return count

# print(number_of_islands(["11000", "11000", "00100", "00011"]))


def letter_combinataions_of_a_phone_number(digits: str):
    dic = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def dfs(numbers):
        if len(numbers) == 1:
            return list(dic[numbers[0]])

        temps = []

        for w in dic[numbers[0]]:
            for temp in dfs(numbers[1:]):
                temps.append(w + temp)

        return temps

    return dfs(digits)

print(letter_combinataions_of_a_phone_number("2"))

def Reconstruct(tickets):
    ticket = sorted(tickets, key=lambda x: (x[0] != 'ICN', x[0], x[1]))
    graph = {}
    for from_, to_ in ticket:
        if from_ in graph:
            graph[from_].append(to_)
        else:
            graph[from_] = [to_]

    stack = ["ICN"]
    path = []
    while stack:
        if stack[-1] not in graph or len(graph[stack[-1]]) == 0:
            path.append(stack.pop())
        else:
            stack.append(graph[stack[-1]].pop(0))


    return path[::-1]

# print(Reconstruct( [['ICN','B'],['B','ICN'],['ICN','A'],['A','D'],['D','A']]))


def course_shecdule(n, courses):
    graph = {}

    for course in courses:
        graph[course[0]] = course[1]


    def dfs(v):
        if v in graph and graph[v] != "":

            if graph[v] == "cycle":
                return False

            temp = graph[v]

            graph[v] = "cycle"

            if dfs(temp):
                graph[v] = ""
                return True
            else:
                return False
        else:
            return True

    return dfs(courses[0][0])


# print(course_shecdule(2, [[1, 0]]))

def Cheapest_flights_within_k_stops(n, edges, options):
    from heapq import heappop, heappush
    src = options["src"]
    dst = options["dst"]
    k = options["k"]

    graph = {}
    graph_cost = {}

    for i in range(n):
        graph_cost[i] = 99999

    graph_cost[src] = 0

    for edge in edges:
        if edge[0] in graph:
            graph[edge[0]].append((edge[1], edge[2]))
        else:
            graph[edge[0]] = [(edge[1], edge[2])]

    queue = []
    stop = 0

    heappush(queue, (src, graph_cost[src]))

    while queue:
        destination, cost = heappop(queue)

        if cost > graph_cost[destination]:
            continue

        for new_destination, new_cost in graph[destination]:
            temp = stop
            if temp <= k:
                if new_cost + cost < graph_cost[new_destination]:
                    graph_cost[new_destination] = cost + new_cost
                    if new_destination in graph:
                        heappush(queue, (new_destination, new_cost + cost))

        stop += 1

    return graph_cost[dst]


# print(Cheapest_flights_within_k_stops(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], { "src": 0, "dst": 2, "k": 0 }))



def game():
    def solution(n, a, b):
        count = 0
        while a != b:
            count += 1
            # 홀수
            if a % 2:
                a = (a + 1) // 2
            else:
                a = a // 2

            if b % 2:
                b = (b + 1) // 2
            else:
                b = b // 2

        return count
    return solution(8, 4, 7)

# print(game())

def skill_tree():
    def solution(skill, skill_trees):
        answer = 0
        for s_tree in skill_trees:
            temp = []
            for i in range(len(s_tree)):
                if s_tree[i] in skill:
                    temp.append(skill.index(s_tree[i]))

            if [i for i in range(len(temp))] == temp:
                answer += 1


        return answer
    return solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])

print(skill_tree())