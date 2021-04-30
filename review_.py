def kruskal_algorithm():
    class dis_join_set:
        def __init__(self, n):
            self.U = []
            for i in range(n):
                self.U.append(i)

        def equal(self, q, p):
            if q == p:
                return True
            return False

        def find(self, i):
            j = i
            while self.U[j] != j:
                j = self.U[j]
            return j

        def union(self, p, q):
            if p < q:
                self.U[q] = p
            else:
                self.U[p] = q


    def kruskal(n, graph):
        d_set = dis_join_set(n)
        edges = []
        graph = sorted(graph, key= lambda x: x[2])

        while len(edges) < n - 1:
            edge = graph.pop(0)
            p = d_set.find(edge[0])
            q = d_set.find(edge[1])

            if d_set.equal(p, q) == False:
                d_set.union(p, q)
                edges.append(edge)

        return (edges)


    return kruskal(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	)

# print(kruskal_algorithm())

def far_node():
    from collections import deque
    def solution(n, vertex):
        graph = {}

        for from_, to_ in vertex:
            if from_ in graph:
                graph[from_].append(to_)
            else:
                graph[from_] = [to_]

            if to_ in graph:
                graph[to_].append(from_)
            else:
                graph[to_] = [from_]

        start = 1
        distances = [0] * (n + 1)
        queue = deque([start])
        visit = [False] * (n + 1)
        visit[start] = True

        while queue:
            v = queue.popleft()
            for node in graph[v]:
                if not visit[node]:
                    distances[node] = distances[v] + 1
                    queue.append(node)
                    visit[node] = True

        return len([x for x in distances if x == max(distances)])

    return solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])

# print(far_node())


def long_palindrome():
    def solution(s):

        for i in range(8, -1, -1):
            print(i)
        # s = list(s)
        # answer = 0
        # for i in range(len(s)):
        #  if answer > 0:
        #      return answer
        #  for j in range(len(s) - i, 1, -1):
        #      if s[i:j] == s[i:j][::-1]:
        #          answer = j - i
        #          break
        #
        # return answer

    return solution("abacde")

# print(long_palindrome())

def camera():
    def solution(routes):
        count = 0
        routes = sorted(routes, key= lambda x: x[1])

        while routes:
            count += 1
            passes = []
            for idx in range(len(routes)):
                if is_meet(routes[0][1], routes[idx]):
                    passes.append(idx)

            routes = [routes[i] for i in range(len(routes)) if i not in passes]

        return count

    return solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])

print(camera())