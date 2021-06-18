# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165

def target_number():
    def solution(numbers, target):
        import itertools
        result = 0
        sum_numbers = sum(numbers)

        for i in range(len(numbers)):
            combs = [x for x in itertools.combinations([x for x in range(len(numbers))], i + 1)]
            for comb in combs:
                if sum_numbers - (2 * sum([numbers[x] for x in comb])) == target:
                    result += 1


        return result

    def solution_2(numbers, target):
        result = []
        def dfs(idx, sum_numbers):
            if idx == len(numbers) - 1:
                if sum_numbers == target:
                    result.append(1)
            else:
                dfs(idx + 1, sum_numbers + numbers[idx + 1])
                dfs(idx + 1, sum_numbers - numbers[idx + 1])

        dfs(0, -numbers[0])
        dfs(0, numbers[0])

        return len(result)

    return solution_2([1,1,1,1,1], 3)

# print(target_number())

# 네트워크
# https://programmers.co.kr/learn/courses/30/lessons/43162

def network():
    def solution(n, computers):
        count = 1
        graph = {x: [] for x in range(len(computers))}
        for i in range(len(computers)):
            for j in range(len(computers)):
                if i != j and computers[i][j] == 1:
                    graph[i].append(j)

        stack = [0]
        visited = [0]
        while stack:
            v = stack.pop()
            for node in graph[v]:
                if node not in visited:
                    stack.append(node)
                    visited.append(node)

            if not stack and len(visited) != n:
                n_ = [x for x in range(n) if x not in visited][0]
                stack.append(n_)
                visited.append(n_)
                count += 1

        return count

    return solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])

# print(network())

# 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163

def change_word():
    def find_word(target, word):
        count = 0
        for i in range(len(word)):
            if word[i] != target[i]:
                count += 1
        return count == 1


    def solution(begin, target, words):
        result = []
        def dfs(value, target, words):
            if value[0] == target:
                result.append(value[1])
                return

            candidate_words = []
            for word in words:
                if find_word(value[0], word):
                    candidate_words.append(word)

            for candidate_word in candidate_words:
                dfs([candidate_word, value[1] + 1], target, [word for word in words if word != candidate_word])

        dfs([begin, 0], target, words)

        return min(result)
    return solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])

print(change_word())


