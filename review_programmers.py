def not_completion():
    def solution(participants, completions):
        hash_map = {}

        for participant in participants:
            hash_key = hash(participant)
            while hash_key in hash_map:
                hash_key += 1
            hash_map[hash_key] = participant

        for completion in completions:
            hash_key = hash(completion)

            if hash_key in hash_map:
                if hash_map[hash_key] != None:
                    hash_map[hash_key] = None
                else:
                    while hash_map[hash_key] == None:
                        hash_key += 1
                    hash_map[hash_key] = None


        return [hash_map[key] for key in hash_map if hash_map[key]].pop()

    return solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])

# print(not_completion())


def phone_number_book():
    def solution(phone_book):
        phone_book = sorted(phone_book, key= len, reverse=True)

        while phone_book:
            short = phone_book.pop()
            short_length = len(short)

            for number in phone_book:
                if short == number[:short_length]:
                    return False

        return True

    return solution(["12","123","1235","567","88"])

# print(phone_number_book())


def spy():
    def solution(clothes):
        hash_map = {}
        answer = 0

        def dfs(key, r, visited):
            if r == 1:
                return len(hash_map[key])

            length = 0

            if r > 1:
                for opt in hash_map:
                    if opt not in visited:
                        visited.append(opt)
                        length += len(hash_map[key]) * dfs(opt, r - 1, visited)
                        break

            return length

        for clothe, option in clothes:
            if option in hash_map:
                hash_map[option].append(clothe)
            else:
                hash_map[option] = [clothe]

        for i in range(len(hash_map)):
            print("--------")
            for key in hash_map:
                length = dfs(key, i + 1, [key])
                answer += length

        return answer

    return solution([["a", "a"], ["b", "b"], ["c", "c"]])

# print(spy())


def truck_cross_bridge():
    def solution(bridge_length, weight, truck_weights):
        import collections
        queue = collections.deque(truck_weights)
        now = []
        total = 0

        while queue:
            now.append([queue.popleft(), 0])

            while len(queue) > 0 and (sum([x[0] for x in now]) + queue[0]) <= weight:
                now = [[x[0], x[1] + 1] for x in now if x[1] + 1 < bridge_length]
                now.append([queue.popleft(), 1])
                total += 1

            while now:
                now = [[x[0], x[1] + 1] for x in now]
                if now[0][1] >= bridge_length:
                    total += 1
                    now = [now[i] for i in range(len(now)) if i > 0]
                    while len(queue) > 0 and (sum([x[0] for x in now]) + queue[0]) <= weight:
                        now = [[x[0], x[1] + 1] for x in now if x[1] + 1 < bridge_length]
                        now.append([queue.popleft(), 1])
                        total += 1
                else :
                    total += 1

        return total + 1

    return solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])


# print(truck_cross_bridge())


def price():
    def solution(prices):
        import collections
        queue = collections.deque(prices)

        result = [0] * len(queue)
        i = 0
        while queue:
            v = queue.popleft()
            time = 0
            for idx in range(len(queue)):
                if v > queue[idx]:
                    time += 1
                    break
                time += 1

            result[i] = time
            i += 1

        return result

    return solution([1,2,3,2,3])

# print(price())

def develop_talent():
    def solution(progresses, speeds):
        import collections
        queue = collections.deque([(x, y) for x, y in zip(progresses, speeds)])
        result = []
        while queue:
            queue = collections.deque([(x + y, y) for x, y in queue])
            count = 0
            while queue and queue[0][0] >= 100:
                queue.popleft()
                count += 1
            if count > 0:
                result.append(count)

        return result

    return solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])

# print(develop_talent())

def printer():
    def solution(priorities, target):
        import collections
        queue = collections.deque([(x, i) for i, x in enumerate(priorities)])


        result = {}
        count = 0
        while queue:
            v, i = queue.popleft()

            if any([x[0] > v for x in queue]):
                queue.append((v, i))
                continue
            count += 1
            result[i] = count

        return result[target]


    return solution([2, 1, 3, 2], 2)

# print(printer())


def more_scoville():
    def solution(scoville, k):
        import heapq
        heap = []
        count = 0
        for s in scoville:
            heapq.heappush(heap, s)

        while len(heap) > 1:
            a = heapq.heappop(heap)
            if a >= k:
                return count
            b = heapq.heappop(heap)

            count += 1
            heapq.heappush(heap, (a + b * 2))

        if heap[0] < k:
            return -1
        else:
            return count + 1


    return solution([1, 2, 3, 9, 10, 12], 7)

# print(more_scoville())

def disk_controller():
    def solution(jobs):
        jobs = sorted(jobs, key= lambda x: x[0], reverse=True)
        length = len(jobs)

        count = 0
        take_able = []
        now_time = 0

        while jobs or take_able:
            if len(take_able) == 0 and jobs:
                a = jobs.pop()
                take_able.append(a)

            while len(take_able) > 0 and take_able[-1][0] <= now_time:
                take_able = sorted(take_able, key= lambda x: x[1], reverse= True)
                now_process = take_able.pop()
                now_time += now_process[1]
                count += now_time - now_process[0]

                rest = [x for x in jobs if x[0] <= now_time]
                take_able.extend(rest)
                jobs = [x for x in jobs if x[0] > now_time]

            while len(take_able) > 0 and take_able[-1][0] > now_time:
                now_process = take_able.pop()
                now_time = now_process[0] + now_process[1]
                count += now_time - now_process[0]

                rest = [x for x in jobs if x[0] <= now_time]
                take_able.extend(rest)
                jobs = [x for x in jobs if x[0] > now_time]

        print(now_time, count)
        return count // length

    return solution([[0, 5], [2, 10], [100000000000, 2]])

# print(disk_controller())

def priority_queue_double():
    def solution(operations):
        import heapq
        if len(operations) == 0:
            return [0, 0]

        commands = ([command.split(' ') for command in operations])[::-1]
        queue = []

        while commands:
            command, number = commands.pop()

            if command == "I":
                heapq.heappush(queue, int(number))

            if command == "D":
                if number == "1":
                    queue = sorted(queue)
                    if queue:
                        queue.pop()
                else:
                    heapq.heappop(queue)


        return queue and [max(queue), min(queue)] or [0, 0]

    return solution(["I 16", "D 1"])

# print(priority_queue_double())



def index_of_k():
    def solution(array, commands):
        return [sorted(array[i - 1: j])[k - 1] for i, j, k in commands]

    return solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])


# print(index_of_k())


def the_biggest_number():
    def solution(numbers):
        str_numbers = list(map(str, numbers))
        max_length = max(len(x) for x in str_numbers)

        new_str_numbers = [(x * (max_length - len(x) + 1), i) for i, x in enumerate(str_numbers)]
        new_str_numbers.sort(reverse= True)

        return str(int(''.join(str_numbers[i] for x, i in new_str_numbers)))

    return solution([3, 30, 34, 5, 9])

# print(the_biggest_number())

def H_index():
    def solution(citations):
        length = len(citations)
        mid = (length // 2)
        sorted_citations = sorted(citations)
        max_length = 0

        while True:
            if mid <= len([x for x in sorted_citations if x >= mid]):
                mid += 1
                if mid <= len([x for x in sorted_citations if x >= mid]):
                    if max_length <= len([x for x in sorted_citations if x >= mid]):
                        max_length = len([x for x in sorted_citations if x >= mid])
                else:
                    return mid - 1
            else:
                mid -= 1
    return solution([0, 0, 1, 1])

# print(H_index())


def target_number():

    # def solution(numbers, target):
    #     from itertools import combinations
    #     answer = 0
    #     target_x = (sum(numbers) - target) // 2
    #
    #     for i in range(len(numbers)):
    #         for x in list(combinations(numbers, i)):
    #             if sum(x) == target_x:
    #                 answer += 1
    #
    #     return answer

    def solution(numbers, target):
        count = 0
        target_x = (sum(numbers) - target) // 2
        if sum(numbers) == target:
            count += 1
        def combination(arr, r):
            chosen = []

            if len(arr) < r:
                return chosen

            if r == 1:
                return arr


            if r > 1:
                for i in range(len(arr) - r  + 1):
                    for temp in combination(arr[i + 1:], r - 1):
                        if type(temp) == list:
                            a = [arr[i]] + temp
                        else:
                            a = [arr[i]] + [temp]
                        chosen.append(a)

            return chosen

        for i in range(len(numbers) + 1):
            for x in combination(numbers, i):
                if type(x) == list:
                    if sum(x) == target_x:
                        count += 1
                else:
                    if x == target_x:
                        count += 1

        return count

    # print(solution([1, 1, 1, 1, 1], 3), 5)
    # print(solution([1, 2, 1, 2], 2), 3)
    # print(solution([1, 2, 1, 2], 6), 1)
    # return solution([1, 1, 1, 1, 1], 3)

# print(target_number())

def net_work():
    def solution(n, computers):
        stack = [computers[0]]
        visited = [0]
        count = 1

        while stack:
            v = stack.pop()

            for idx in range(len(v)):
                if v[idx] == 1:
                    if idx not in visited:
                        visited.append(idx)
                        stack.append(computers[idx])

            if len(stack) == 0:
                for i in range(len(computers)):
                    if i not in visited:
                        count += 1
                        visited.append(i)
                        stack.append(computers[i])
                        break

        return count

    return solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])

# print(net_work())

def word_change():
    def check_word(a, b):
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1

        return count

    def solution(begin, target, words):
        temp = []
        def dfs(t, c, arr):
            if arr:
                if t == target:
                    return c

                for i in range(len(arr)):
                    if check_word(arr[i], t) == 1:
                        a = dfs(arr[i], c + 1, arr[:i] + arr[i+1:])
                        if a:
                            temp.append(a)

        dfs(begin, 0, words[:])
        if temp:
            return min(temp)
        else:
            return 0

    return solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log"])

# print(word_change())

def math_give_up():
    def solution(answers):
        person_answer = {
            1: [1, 2, 3, 4, 5],
            2: [2, 1, 2, 3, 2, 4, 2, 5],
            3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        }

        persons = [0] * (len(person_answer) + 1)

        for key in person_answer:
            length = len(person_answer[key])
            for i in range(len(answers)):
                if answers[i] == (person_answer[key][i % length]):
                    persons[key] += 1

        return [i for i, x in enumerate(persons) if max(persons) == x]

    return solution([1,2,3,4,5])

# print(math_give_up())


def find_prime_number():
    def is_prime(n):
        if n > 1:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False

            return True
        else:
            return False

    def permutation(arr, r):
        chosen = []
        if len(arr) < r:
            return chosen

        if r == 1:
            for v in arr:
                chosen.append(v)

        if r > 1:
            for i in range(len(arr)):
                temp = [arr[i]]
                for v in permutation(arr[:i] + arr[i + 1:], r - 1):
                    temp.extend(v)
                    if len(temp) == r:
                        chosen.append(temp)
                        temp = [arr[i]]


        return chosen


    def solution(numbers):
        count = 0
        number = set([])
        for i in range(1, len(numbers) + 1):
            for values in permutation(numbers, i):
                number.add(int(''.join(values)))

        for v in number:
            if is_prime(v):
                count += 1

        return count

    return solution("011")

# print(find_prime_number())

def capet():
    def solution(brown, yellow):
        for row in range(1, yellow + 1):
            y_row = row
            if (yellow // y_row) == int(yellow / y_row):
                b_col = (yellow // y_row) + 2
                b_row = y_row + 2
                if (b_row * b_col) - (yellow) == brown:
                    return [max(b_row, b_col), min(b_row, b_col)]
    return solution(8, 1)

# print(capet())


def connect_island():
    class dis_join_set:
        def __init__(self, n):
            self.U = []
            for i in range(n):
                self.U.append(i)

        def find(self, i):
            j = i
            while self.U[j] != j:
                j = self.U[j]
            return j

        def equal(self, p, q):
            if p == q:
                return True
            return False

        def union(self, p, q):
            if p < q:
                self.U[q] = p
            else:
                self.U[p] = q


    def solution(n, costs):
        F = []
        d_set = dis_join_set(n)
        costs = sorted(costs, key=lambda x: x[2], reverse=True)

        while len(F) < n - 1:
            edge = costs.pop()
            p = d_set.find(edge[0])
            q = d_set.find(edge[1])
            if d_set.equal(p, q) == False:
                d_set.union(p, q)
                F.append(edge[2])

        return sum(F)

    return solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])

print(connect_island())