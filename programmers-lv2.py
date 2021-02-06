# 124 나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899

def one_two_four():
    n = 15 # 111
    def solution(n):
        def find_number(num):
            if num == 1 or num == 2:
                return num
            if num == 3 or num == 0:
                return 4

            if num % 3 == 0:
                return str(find_number((num // 3) - 1)) + str(find_number(num % 3))
            return str(find_number(num // 3)) + str(find_number(num % 3))

        return find_number(n)

    def solution_loop(n):
        num = ["1", "2", "4"]
        answer = ""

        while n > 0:
            n -= 1
            answer = num[n % 3] + answer
            n = n // 3

    return solution_loop(n)

# print(one_two_four())


# 실패! -> 왜 최대 공약수?
def rectangle():
    w = 3
    h = 11
    def solution(w, h):
        min_number = min(w, h)
        max_number = max(w, h)
        if max_number % min_number == 0:
            y = max_number // min_number
        else:
            y = (max_number // min_number) + 1

        print(max_number / min_number)
        if abs((max_number // min_number) - (max_number / min_number)) > 0.5:
            return ((w * h) - (y * min_number)) - 1

        return ((w * h) - (y * min_number))

    return solution(w, h)

# print(rectangle())

def skill_tree():
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    def solution(skill, skill_trees):
        skill = [x for x in skill]
        answer = 0

        while skill_trees:
            skills = list(skill)
            trees = [x for x in skill_trees.pop()]

            for s in trees:
                if s in skill:
                    if s != skills.pop(0):
                        break
            else:
                answer += 1
        #
        # while skill_trees:
        #     trees = [x for x in skill_trees.pop()]
        #     seq = []
        #     flag = True
        #
        #     for i in range(len(skill)):
        #         if skill[i] in trees:
        #             seq.append(str(trees.index(skill[i])))
        #         else:
        #             seq.append(9999999)
        #
        #     for i in range(len(seq) - 1):
        #         if int(seq[i]) > int(seq[i + 1]):
        #             flag = False
        #             break
        #
        #     if flag:
        #         answer += 1

        return answer

    return solution(skill, skill_trees)

# print(skill_tree())


# n 번씩 반복은 "% 나머지 연산" 을 사용해서 패턴을 나눠서 움직이자.
def tri_snail():
    def solution(n):
        snail = [[0 for _ in range(n)] for _ in range(n+1)]
        row, col = 0, 0
        value = 1
        i = 0
        while i < n:
            for j in range(i, n):
                if i % 3 == 0:
                    row += 1
                elif i % 3 == 1:
                    col += 1
                elif i % 3 == 2:
                    row -= 1
                    col -= 1
                snail[row][col] = value
                value +=1
            i+= 1

        return [x for y in snail for x in y if x != 0]

    return solution(6)

# print(tri_snail())


def trip_string():
    def solution(s):
        answer = []
        for i in range(1, len(s) // 2 + 1):
            string = ''
            count = 1
            temp = s[0:i]

            for j in range(i, len(s), i):

                if temp == s[j: j + i]:
                    count += 1
                else:
                    if count > 1:
                        string += str(count)
                    string += temp
                    temp = s[j: j + i]
                    count = 1

            if count > 1:
                string += str(count)
            string += temp
            print(string)
            # if len(string) > 0:
            #     if string[0].isalpha():
            #         break
            if len(string) not in answer:
                answer.append(len(string))

        return min(answer)



    return solution("abcabcabc")

# print(trip_string())


def ffibbo():
    def solution(n):
        dp = [-1] * (n + 1)

        def fibo(n):
            if n == 0 or n == 1:
                return n

            if dp[n] > -1:
                return dp[n]

            dp[n] = fibo(n - 2) + fibo(n - 1)

            return dp[n]

        return fibo(n)

    return solution(4)

# print(ffibbo())

def menu_renewal():
    orders = ["XYZ", "XWY", "WXA"]
    course = [2,3,4]

    def solution_itertools(orders, course):
        import itertools

        answer = []

        for size_of_course in course:
            order_dict = {}
            order_combinations = []
            for order in orders:
                order_combinations.extend(list(itertools.combinations(sorted(order), size_of_course)))

            for order_combination in order_combinations:
                order_str = ''.join(order_combination)
                if order_str in order_dict:
                    order_dict[order_str] += 1
                else:
                    order_dict[order_str] = 1

            for order in order_dict:
                if order_dict[order] == max([order_dict[order] for order in order_dict]):
                    if order_dict[order] > 1:
                        answer.append(order)

            # max_order = [order for order in order_dict
            #              if order_dict[order] == max([order_dict[order] for order in order_dict])
            #              if order_dict[order] > 1]

            # answer.extend(max_order)

        return sorted(answer)




    # def solution(orders, course):
    #     answer = []
    #     dic = {}
    #
    #     for i in course:
    #         dic[i] = {}
    #
    #     def comb(array, r):
    #         chosen = []
    #         if r > len(array):
    #             return chosen
    #
    #         if r == 1:
    #             for i in array:
    #                 chosen.append(i)
    #
    #         elif r > 1:
    #             for i in range(len(array) - r + 1):
    #                 for temp in comb(array[i + 1:], r - 1):
    #                     arr = [x for x in array[i]]
    #                     arr.extend([x for x in temp])
    #                     chosen.append(arr)
    #
    #         return chosen
    #
    #     for course_number in course:
    #         for order in orders:
    #             courses = comb(order, course_number)
    #
    #             for c in courses:
    #                 st = ''.join(sorted(c))
    #                 if st in dic[len(st)]:
    #                     dic[len(st)][st] += 1
    #                 else:
    #                     dic[len(st)][st] = 1
    #
    #     for course_key in dic:
    #         max_value = []
    #         for value in dic[course_key]:
    #             count = dic[course_key][value]
    #             if count > 1:
    #                 max_value.append((count, value))
    #
    #         answer.append([x[1] for x in max_value if x[0] == max([x[0] for x in max_value])])
    #     return sorted([y for x in answer for y in x])

    return solution_itertools(orders, course)

# print(menu_renewal())


def joy_stick():
    def solution(name):
        alphabet = [x.upper() for x in "abcdefghijklmnopqrstuvwxyz"]
        default_name = list('A' * len(name))
        target_name = list(name)

        length = len(target_name)
        count = 0
        dic = {}

        visit = [False] * length
        now_move = 0
        visit[now_move] = True

        for i in range(length):
            target_word = target_name[i]
            default_word = default_name[i]

            up = alphabet.index(target_word) - alphabet.index(default_word)
            down = len(alphabet) - alphabet.index(target_word)

            min_up_down = min(up, down % len(alphabet))
            count += min_up_down
            dic[i] = min_up_down

        while any([x == False for x in visit]):
            index_array = []
            for i in range(length):
                if visit[i] == False and dic[i] != 0 and i != now_move:
                    left = i > now_move and length - i + now_move or now_move - i
                    right = now_move > i and length + 1 or i - now_move
                    index_array.append((left, right, i))

            if len(index_array) > 0:
                next_move = min([x for x in index_array], key= lambda x: (min(x[1], x[0]), x[1], x[0]))
                count += (min(next_move[0], next_move[1]))
                visit[next_move[2]] = True
                now_move = next_move[2]

            else:
                for i in range(length):
                    if visit[i] == False and dic[i] == 0:
                        visit[i] = True


        return count

    # print(solution("BBBAAAB"))  # 8
    # print(solution("ABABAAAAABA"))  # 10
    # print(solution("CANAAAAANAN"))  # 48
    # print(solution("ABAAAAABAB"))  # 8
    # print(solution("ABABAAAAAB"))  # 8
    # print(solution("BABAAAAB"))  # 7
    # print(solution("AAA"))  # 0
    # print(solution("ABAAAAAAABA"))  # 6
    # print(solution("AAB"))  # 2
    # print(solution("AABAAAAAAABBB"))  # 11
    # print(solution("ZZZ"))  # 5
    # print(solution("BBBBAAAAAB"))  # 10
    # print(solution("BBBBAAAABA"))  # 12
    # return solution("AAAAAA")

# print(joy_stick())


def get_bigger():

    def solution(number, k):
        numbers = list([(str(x), i) for i, x in enumerate(number)])
        length = len(numbers) - k
        now = 0
        count = k
        answer = ''
        while length > 0:
            max_number = (-1, -1)
            for i in range(now, now + count + 1):
                if int(max_number[0]) < int(numbers[i][0]):
                    max_number = numbers[i]
                    if numbers[i][0] == '9':
                        break

            # max_number = max(numbers[now: now + count + 1], key= lambda x: x[0])
            count -= (max_number[1] - now)
            answer += max_number[0]
            now = max_number[1] + 1
            length -= 1

        return answer
    return solution("1924", 2)

# print(get_bigger())



# https://programmers.co.kr/learn/courses/30/lessons/60058
def bracket():
    def solution(p):

        def is_perfect(p):
            perfect = 0
            p = list(p)

            for word in p:
                if word == "(":
                    perfect += 1
                else:
                    perfect -= 1

                if perfect < 0:
                    break

            return perfect >= 0

        def bracket_recrusive(w):
            w = list(w)
            is_left = 0
            is_right = 0
            u, v = [], []

            for i in range(len(w)):
                if w[i] == "(":
                    is_left += 1
                else:
                    is_right += 1

                if is_left == is_right and is_left != 0:
                    u = w[0: i + 1]
                    v = w[i + 1: len(w)]
                    break

            if v == [] and is_perfect(u):
                return ''.join(u)

            if not is_perfect(u):
                u = u[1: len(u) - 1]
                for i in range(len(u)):
                    if u[i] == "(":
                        u[i] = ")"
                    elif u[i] ==")":
                        u[i] = "("
                v = bracket_recrusive(v)
                u = ["("] + list(v) + [")"] + list(u)
                return ''.join(u)
            else:
                v = bracket_recrusive(v)
                return ''.join(u) + ''.join(v)

        return bracket_recrusive(p)

    return solution(")()()()(")

# print(bracket())

# https://programmers.co.kr/learn/courses/30/lessons/42885
def life_boat():
    def solution(people, limit):
        from collections import deque
        peoples = deque(sorted(people))
        boat = 0

        while len(peoples) > 0:
            if peoples[0] + peoples[len(peoples) - 1] <= limit and len(peoples) > 1:
                peoples.popleft()
                peoples.pop()
                boat += 1
            else:
                boat +=1
                peoples.pop()

        return boat

    return solution([70, 80, 50], 100)

print(life_boat())

# https://programmers.co.kr/learn/courses/30/lessons/12909#
def bracket_easy():
    def solution(s):
        def is_perfect(p):
            perfect = 0
            p = list(p)

            for word in p:
                if word == "(":
                    perfect += 1
                else:
                    perfect -= 1

                if perfect < 0:
                    break

            return perfect == 0

        return is_perfect(s)
    return solution("()())")
print(bracket_easy())