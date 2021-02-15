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

    def solution_stack(number, k):
        stack = [number[0]]
        number = number[1:]

        for num in number:
            while stack and stack[-1] < num and k > 0:
                stack.pop()
                k -= 1
            stack.append(num)
        print(stack)
        if k > 0:
            stack = stack[0:-k]

        return ''.join(stack)

    return solution_stack("999988", 2)

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

# print(life_boat())

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
# print(bracket_easy())

def find_biggest_rect():

    def solution(board):
        row_length = len(board)
        col_length = len(board[0])
        # dp = [[board[row][col] for col in range(col_length)] for row in range(row_length)]
        result = 0

        for row in range(1, row_length):
            for col in range(1, col_length):
                if board[row][col] == 1:
                    if board[row - 1][col] >= 1 and board[row][col - 1] >= 1 and board[row - 1][col - 1] >= 1:
                        board[row][col] = min(board[row - 1][col], board[row][col - 1], board[row - 1][col - 1]) + 1
        return max([x for y in board for x in y]) ** 2


    return solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])
# print(find_biggest_rect())


def coin_changer():
    def solution(coins, cost):
        dp = [9999999] * (cost + 1)
        dp[0] = 0

        for i in range(len(coins)):
            for j in range(coins[i], cost + 1):
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)

        return dp[cost]

    return solution([1, 2, 5], 15)

# print(coin_changer())


# https://programmers.co.kr/learn/courses/30/lessons/12911
def get_next_big_number():
    def solution(n):
        def get_binary(n):
            binary = ""
            while n > 0:
                binary = str(n % 2) + binary
                n = n // 2
            if n > 0:
                binary = str(n) + binary
            return binary

        binary_n_length_of_one = get_binary(n).count("1")

        while True:
            n += 1

            # n 보다 큰 수중 1의 갯수가 같은 수 가 나오면 가장 가까운 같은 수 이기 떄문에 바로 리턴
            if get_binary(n).count("1") == binary_n_length_of_one:
                return n

    return solution(78)

# print(get_next_big_number())

# https://programmers.co.kr/learn/courses/30/lessons/64065
def tuple_kakao():
    def solution(s: str):
        list_s = s.split("},")

        for i, a in enumerate(list_s):
            list_a = a.split(",")

            for j, b in enumerate(list_a):
                word = [x for x in b if x.isdigit()]
                list_a[j] = ''.join(word)
            list_s[i] = list_a

        list_s.sort(key= lambda x: len(x))

        now = list_s[0]
        for i in range(1, len(list_s)):
            now += set(list_s[i]) - set(now)


        return [int(x) for x in now]


    return solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")

# print(tuple_kakao())


def get_area():
    # def solution(land):
    #     visit = [[False for _ in range(len(land[0]))] for _ in range(len(land))]
    #     result = []
    #     def get_land(row, col, land):
    #         if row + 1 == len(land):
    #             visit[row][col] = True
    #             return land[row][col]
    #
    #         temp = 0
    #         for i in range(len(land[0])):
    #             if col != i:
    #                 if visit[row + 1][i] == True:
    #                     temp = max(temp, land[row][col] + land[row + 1][i])
    #                 else:
    #                     temp = max(temp, land[row][col] + get_land(row + 1, i, land))
    #                     visit[row + 1][i] = True
    #         land[row][col] = temp
    #
    #         return land[row][col]
    #
    #     for i in range(len(land[0])):
    #         result.append(get_land(0, i, land))
    #
    #
    #     return max(result)

    def solution_hyunta(land):

        for i in range(1, len(land)):
            for j in range(len(land[0])):
                land[i][j] = max(land[i - 1][:j] + land[i - 1][j+1:]) + land[i][j]

        return max(land[-1])

    return solution_hyunta([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]])

# print(get_area())


def expression_of_number():
    def solution(n):
        count = 0
        for i in range(1, n // 2 + 1):
            sum_value = 0
            while sum_value <= n:
                sum_value += i
                i += 1
                if sum_value == n:
                    count += 1
                    break
        return count + 1
    return solution(15)

# print(expression_of_number())



def get_land():
    def solution(land):
        for i in range(1, len(land)):
            for j in range(len(land[i])):
                prev_land = [x for idx, x in enumerate(land[i - 1]) if j != idx]
                land[i][j] += max(prev_land)

        return max(land[-1])

    return solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]])

# print(get_land())


def phone_cat_mon():
    def solution(nums):
        list = []
        numbers = set(nums)

        while len(list) < (len(nums) // 2):
            if len(numbers) == 0:
                break
            list.append(numbers.pop())

        return len(list)

    return solution([3,3,3,2,2,4])

# print(phone_cat_mon())


def binary_loop():
    def solution(s):
        count = 1
        zero = 0
        def get_binary(p):
            binary_string = ""
            p = int(p)
            while p > 0:
                binary_string = str(p % 2) + binary_string
                p = p // 2

            return binary_string

        zero += len([x for x in s if x == "0"])
        s = str(len([x for x in s if x == "1"]))
        while s != "1":
            s = get_binary(s)
            zero += len([x for x in s if x == "0"])
            s = str(len([x for x in s if x == "1"]))
            count += 1


        return [count, zero]

    return solution("1111111")

# print(binary_loop())

def make_min_value():
    def solution(A, B):
        from collections import deque
        a = deque(sorted(A))
        b = deque(sorted(B))
        result = 0
        while len(a) > 0:
            result += a.popleft() * b.pop()
        return result

    return solution([1, 2], [3, 4])

# print(make_min_value())


# https://programmers.co.kr/learn/courses/30/lessons/67257
def maximum():
    def calculate(x, operand):
        copy_operand = operand.copy()
        for i in range(len(copy_operand)):
            if copy_operand[i] == x:
                if x == "*":
                    copy_operand[i + 1] = str(int(copy_operand[i - 1]) * int(copy_operand[i + 1]))
                elif x == "-":
                    copy_operand[i + 1] = str(int(copy_operand[i - 1]) - int(copy_operand[i + 1]))
                else:
                    copy_operand[i + 1] = str(int(copy_operand[i - 1]) + int(copy_operand[i + 1]))
                copy_operand[i] = "_"
                copy_operand[i - 1] = "_"
        copy_operand = [x for x in copy_operand if x != "_"]
        return copy_operand



    def solution(expression):
        import itertools
        expression_list = ["*", "-", "+"]
        operand = []
        after_expression_index = 0
        result = []

        for i in range(len(expression)):
            if expression[i] in expression_list:
                operand.append(expression[after_expression_index:i])
                operand.append(expression[i])
                after_expression_index = i + 1

        operand.append(expression[after_expression_index:])

        expression_priority = list(itertools.permutations(expression_list, 3))

        while expression_priority:
            priority = expression_priority.pop()
            copy_operand = operand.copy()

            for x in priority:
                copy_operand = calculate(x, copy_operand)

            result.append(abs(int(copy_operand[0])))
        return max(result)

    return solution("100-200*300-500+20")

# print(maximum())

def matrix_multply():
    def solution(arr1, arr2):
        col_max = len(arr2[0])
        row_max = len(arr1)
        result = [[0] * col_max for _ in range(row_max)]

        for row in range(row_max):
            for col in range(col_max):
                for arr_col in range(len(arr1[0])):
                    result[row][col] += arr1[row][arr_col] * arr2[arr_col][col]
        return result

    return solution([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]])

# print(matrix_multply())



def jadenCase():
    def solution(s):
        print(s)
        return ' '.join([''.join([i == 0 and a.upper() or a.lower() for i, a in enumerate(x)]) for x in s.split(" ")])
    return solution("3people unFollowed me")

# print(jadenCase())

def gcds():
    def solution(arr):
        def get_gcd(a, b):
            normal_a = a
            normal_b = b

            while normal_a != normal_b:
                if normal_a > normal_b:
                    normal_b += b
                elif normal_a < normal_b:
                    normal_a += a

            return normal_a

        for i in range(1, len(arr)):
            arr[i] = get_gcd(arr[i - 1], arr[i])

        return arr[-1]

    return solution([2,6,8,14])

# print(gcds())


def couple_remove():
    def solution(s):
        stack = [s[0]]

        for i in range(1, len(s)):
            print(stack)
            if len(stack) == 0:
                stack.append(s[i])
            if stack[-1] == s[i]:
                stack.pop()
            if stack[-1] != s[i]:
                stack.append(s[i])


        if len(stack) > 0:
            return 0
        else:
            return 1

    return solution("abccaabaa")

# print(couple_remove())

def make_prime():
    def solution(nums):
        answer = 0
        import itertools
        is_prime_number = [sum(x) for x in itertools.combinations(nums, 3)]
        def is_prime(num):
            max_length = int(num ** 0.5) + 1
            for i in range(2, max_length):
                if num % i == 0:
                    return False

            return True

        for n in is_prime_number:
            if is_prime(n):
                answer += 1

        return answer

    return solution([1, 2, 3, 4])

# print(make_prime())


def teleport_jump():
    def solution(n):
        jump = 0
        while n > 0:
            if n % 2:
                jump += 1
            n = n //2

        return jump
    return solution(5)

# print(teleport_jump())


def english_play():
    def solution(n, words):
        person_cycle = [0] * (n)
        person_number = 0
        last_word = words[0][0]
        for i in range(len(words)):
            person_number = i % n
            person_cycle[person_number] += 1
            if last_word != words[i][0] or words[i] in words[:i] or len(words[i]) == 1:
                return [person_number + 1, person_cycle[person_number]]
            last_word = words[i][-1]


        return [0, 0]

    return solution(3, 	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
# print(english_play())


def sieve_of_eratos(n):
    sieve = [True] * (n + 1)
    max_length = int(n ** 0.5) + 1
    for i in range(2, max_length):
        if sieve[i]:
            for j in range(i + i, n + 1, i):
                sieve[j] = False

    return [i for i in range(2, len(sieve)) if sieve[i] != False]

# print(sieve_of_eratos(100))

def news_cluster():
    def solution(str1, str2):
        arr1 = [(str1[i - 1] + str1[i]).lower() for i in range(1, len(str1)) if str1[i].isalpha() and str1[i - 1].isalpha()]
        arr2 = [(str2[i - 1] + str2[i]).lower() for i in range(1, len(str2)) if str2[i].isalpha() and str2[i - 1].isalpha()]
        same = {}
        diff = {}

        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if arr1[i] == arr2[j] and arr1[i] != "":
                    if arr1[i] in same:
                        same[arr1[i]] += 1
                        arr1[i] = ""
                        arr2[j] = ""
                    else:
                        same[arr1[i]] = 1
                        arr1[i] = ""
                        arr2[j] = ""

        for i in range(len(arr1)):
            if arr1[i] != "":
                if arr1[i] in diff:
                    diff[arr1[i]] += 1
                else:
                    diff[arr1[i]] = 1

        for i in range(len(arr2)):
            if arr2[i] != "":
                if arr2[i] in diff:
                    diff[arr2[i]] += 1
                else:
                    diff[arr2[i]] = 1

        same_length = 0
        diff_length = 0

        for key in same:
            same_length += same[key]

        for key in diff:
            diff_length += diff[key]

        if diff_length == same_length and same_length == 0:
            return 65536

        return int(65536 * (same_length / (same_length + diff_length)))
    return solution("aa1+aa2", "AAAA12")

# print(news_cluster())


def frends_four_block():
    def solution(m, n, board):
        answer = 0
        def fung(m, n, board):
            result = 0
            flag = False
            index_list = []
            for row in range(1, m):
                for col in range(1, n):
                    if board[row][col] != "0":
                        if board[row][col] == board[row - 1][col] and board[row - 1][col] == board[row][col - 1] and board[row][col - 1] == board[row - 1][col - 1]:
                            index_list.append((row, col))
                            flag = True

            if flag:
                for row, col in index_list:
                    if board[row][col] != "0":
                        result += 1
                        board[row][col] = "0"
                    if board[row - 1][col] != "0":
                        result += 1
                        board[row - 1][col] = "0"
                    if board[row][col - 1] != "0":
                        result += 1
                        board[row][col - 1] = "0"
                    if board[row - 1][col - 1] != "0":
                        result += 1
                        board[row - 1][col - 1] = "0"

                for col in range(n):
                    temp = []
                    for row in range(m - 1, -1, -1):
                        temp.append(board[row][col])

                    temp = [x for x in temp if x != "0"]

                    if len(temp) < m:
                        temp.extend(["0"] * (m - len(temp)))

                    for row in range(m - 1, -1, -1):
                        board[row][col] = temp[m - row - 1]

            return (flag, result)

        board = [[a for a in x] for x in board]

        while True:
            flag, temp = fung(m, n, board)
            answer += temp
            if not flag:
                break

        return answer

    return solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])

# print(frends_four_block())

def casheSize():
    def solution(size, cities):
        import collections
        cashes = []
        answer = 0
        cities = collections.deque([x.lower() for x in cities])

        while len(cities) > 0:
            if size == 0:
                return len(cities) * 5
            city = cities.popleft()
            if len(cashes) > 0:
                if city in cashes:
                    if len(cashes) == size:
                        cashes.pop(cashes.index(city))
                    answer -= 4
                else:
                    if len(cashes) == size:
                        cashes.pop(0)

            answer += 5
            cashes.append(city)


        return answer

    return solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])

print(casheSize())


def open_chat():
    def solution(record):
        dic = {}
        str_list = []
        for i in range(len(record)):
            command = record[i].split(" ")
            action = command[0]
            if action == "Enter":
                uid = command[1]
                name = command[2]
                dic[uid] = name
                str_list.append(uid + "님이 들어왔습니다.")
            elif action == "Leave":
                uid = command[1]
                str_list.append(uid + "님이 나갔습니다.")
            elif action == "Change":
                uid = command[1]
                name = command[2]
                dic[uid] = name

        for i in range(len(str_list)):
            arr = str_list[i].split("님이")
            str_list[i] = dic[arr[0]] + "님이" + arr[1]

        return str_list

    return solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

# print(open_chat())

def candidate_key():
    def solution(relation):
        import itertools
        stack = []
        relation_reverse = []
        for col in range(len(relation[0])):
            temp = []
            for row in range(len(relation)):
                temp.append(relation[row][col])
            relation_reverse.append(temp)

        while stack:
            compare = []
            for s in stack:
                relation_reverse[s]






        return

    return solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])

print(candidate_key())