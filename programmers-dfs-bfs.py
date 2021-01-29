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


print(change_word())
