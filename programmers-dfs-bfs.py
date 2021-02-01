# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165

def target_number():
    numbers = [1, 2, 3, 4, 5]
    target = 5

    def combination(arr, r):
        for i in range(len(arr)):
            if r == 1:
                yield [arr[i]]
            else:
                for next in combination(arr[i + 1:], r - 1):
                    yield [arr[i]] + next

    def solution(numbers, target):
        # from itertools import combinations
        answer = 0
        target_x = (sum(numbers) - target) // 2

        for i in range(len(numbers)):
            print([x for x in list(combination(numbers, i + 1))])
            for x in list(combination(numbers, i + 1)):
                if sum(x) == target_x:
                    answer += 1

        return answer

    return solution(numbers, target)


# print(target_number())


# 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162
def network():
    n = 3
    computers = [[1,1,0], [1,1,0], [0,1,1]]
    def solution(n, computers):
        answer = 0
        connected = [(0, computers[0])]
        visited = [False] * n

        visited[0] = True
        answer += 1

        while len(connected) > 0:
            i, computer = connected.pop(0)

            for idx, connect in enumerate(computer):
                if i != idx and connect == 1 and visited[idx] == False:
                    connected.append((idx, computers[idx]))
                    visited[idx] = True

            if len(connected) == 0 and any([x == False for x in visited]):
                not_visited = visited.index(False)
                connected.append((not_visited, computers[not_visited]))
                visited[not_visited] = True
                answer += 1

        return answer

    return solution(n, computers)

# print(network())

# 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163

def change_word():
    begin = "hit"
    target = "cog"
    words =["hot", "dot", "dog", "lot", "log"]

    def find_change_able_word(now, visited, words):
        change_able = []
        for index, word in enumerate(words):
            count = 0
            if visited[index] == False:
                for i in range(len(word)):
                    if now[0][i] != word[i]:
                        count += 1

            if count == 1:
                change_able.append((index, (word, now[1] + 1)))

        return change_able

    def solution(begin, target, words):
        answer = 1
        visited = [False] * len(words)
        change_able = find_change_able_word((begin, 0), visited, words)

        while len(change_able):
            for i, word in change_able:
                visited[i] = True

            index, now = change_able.pop()

            if now[0] == target:
                answer = now[1]
                return answer

            if len(find_change_able_word(now, visited, words)) > 0:
                change_able.extend(find_change_able_word(now, visited, words))


        return 0

    return solution(begin, target, words)


# print(change_word())


def dfs_outer():
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
    visited = [False] * len(graph)
    answer = []
    def dfs(graph, node, visited):
        visited[node] = True
        answer.append(node)

        for idx in graph[node]:
            if not visited[idx]:
                dfs(graph, idx, visited)

    dfs(graph, 1, visited)

    return answer

# print(dfs_outer())


def bfs_outer():
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }
    def bfs(graph, start_node):
        import collections
        visited = {x: False for x in graph}
        answer = [start_node]
        queue = collections.deque([])

        queue.append(start_node)
        visited[start_node] = True

        while queue:
            current_node = queue.popleft()

            for node in graph[current_node]:
                if not visited[node]:
                    visited[node] = True
                    queue.append(node)
                    answer.append(node)

        return answer

    return bfs(graph, 'A')

# print(bfs_outer())



# 여행경로
# https://programmers.co.kr/learn/courses/30/lessons/43164

def travel_load():
    tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    # tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    def solution(tickets):
        answer = []
        tickets.sort(key= lambda x: (x[0] < 'ICN', x[0], x[1]))
        tickets = [(index, ticket) for index, ticket in enumerate(tickets)]
        visited = [False] * len(tickets) # 5
        now_ticket = tickets[0]
        visited[now_ticket[0]] = True
        answer.append(now_ticket[1][0])

        while True:
            if len(list(filter(lambda x: x == False, visited))) == 2:
                for idx, ticket in enumerate(tickets):
                    if ticket[1][0] == now_ticket[1][1] and not visited[ticket[0]]:
                        visited[ticket[0]] = True
                        answer.extend(ticket[1])
                for idx, visit in enumerate(visited):
                    if visit == False:
                        visited[idx] = True
                        answer.extend(tickets[idx][1])
                break

            if any([now_ticket[1][1] == ticket[1][0] and not visited[ticket[0]] for ticket in tickets]) == False:
                for idx, ticket in enumerate(tickets):
                    if ticket[1][0] == "ICN" and visited[ticket[0]] == False:
                        visited[now_ticket[0]] = False
                        now_ticket = ticket
                        visited[now_ticket[0]] = True
                        break


            for idx, ticket in enumerate(tickets):
                if ticket[1][0] == now_ticket[1][1] and not visited[ticket[0]]:
                    temp = now_ticket
                    now_ticket = ticket
                    if any([now_ticket[1][1] == ticket[1][0] and not visited[ticket[0]] for ticket in tickets]) == False:
                        if any([visit == False and now_ticket[0] != i for i, visit in enumerate(visited)]):
                            now_ticket = temp
                            continue
                    visited[now_ticket[0]] = True
                    answer.append(now_ticket[1][0])
                    break


            if not any([x == False for x in visited]):
                answer.append(now_ticket[1][1])
                break

        return answer

    # print(solution([["ICN", "A"], ["ICN", "A"], ["A", "ICN"], ["A" , "C"]]))
    # print(solution([["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"],["SFO","QRE"]]))
    # print(solution([['ICN', 'COO'], ['COO', 'ICN'],['ICN', 'COO']]))
    # print(solution([['ICN','BOO'], ['ICN', 'COO'], ['COO', 'DOO'], ['DOO', 'COO'], ['BOO', 'DOO'] ,['DOO', 'BOO'], ['BOO', 'ICN'], ['COO', 'BOO']]))
    # print(solution([["ICN", "A"],["ICN", "A"],["A","ICN"]]))
    # print(solution([["ICN", "A"], ["ICN", "A"], ["A", "ICN"], ["A", "C"]]))
    # print(solution([["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]))
    # print(solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]))
    # print(solution([['ICN' ,'B'], ['ICN', 'C'] ,['C', 'D'], ['D', 'ICN']]))
    # print(solution([['ICN', 'B'], ['B', 'C'], ['C', 'ICN'], ['ICN', 'D'], ['ICN', 'E'], ['E', 'F']]))

    # return solution(tickets)


# print(travel_load())


def travel_load_2():
    tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    def solution(tickets):
        routes = {}

        for ticket in tickets:
            if ticket[0] in routes:
                routes[ticket[0]].append(ticket[1])
            else:
                routes[ticket[0]] = [ticket[1]]

        for route in routes:
            routes[route].sort(reverse=True)

        stack = ["ICN"]
        answer = []

        while stack:
            top = stack[-1]

            if top in routes and routes[top]:
                stack.append(routes[top].pop())
            else:
                answer.append(stack.pop())

        return answer[::-1]

    return solution(tickets)

print(travel_load_2())
