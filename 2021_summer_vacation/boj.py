# https://covenant.tistory.com/224 에 있는 문제 풀기

# 약수 구하기 https://www.acmicpc.net/problem/2501
# n 의 약수중 k 번째로 작은 약수 를 return
def find_divisor():
    n, k = map(int, input().split())
    arr = []
    for i in range(1, n + 1):
        if n % i == 0:
            arr.append(i)

    if k > len(arr):
        print(0)
    else:
        print(arr[k - 1])

# print(find_divisor())


# 이진수 https://www.acmicpc.net/problem/3460
# 이진수로 변환 후 1의 위치를 return
def digit_find_one():
    n = int(input())
    tests = []
    for _ in range(n):
        tests.append(int(input()))

    def to_digit(number):
        num = number
        digit = ''
        while num > 0:
            spare = num % 2
            num = num // 2
            digit = str(spare) + digit

        return digit

    def find_one(digit):
        positions = []
        length = len(digit) - 1
        for idx, bit in enumerate(digit):
            if int(bit) == 1:
                positions.append(length - idx)

        return sorted(positions)

    for test in tests:
        for pos in find_one(to_digit(test)):
            print(pos)


# print(digit_find_one())

# 최소, 최대 https://www.acmicpc.net/problem/10818
# 최소 값과 최대 값은?

def minimum_maximum():
    n = int(input())
    numbers = [x for x in map(int, input().split())]

    def find_max_min(numbers):
        maximum = -1 * float('inf')
        minimum = float('inf')
        for number in numbers:
            if number > maximum:
                maximum = number

            if number < minimum:
                minimum = number

        return [minimum, maximum]


    numbers = find_max_min(numbers)

    print(numbers[0], numbers[1], end='')

# print(minimum_maximum())


# 지능형 기차 2 https://www.acmicpc.net/problem/2460
# 단순 구현
def ai_train_2():
    now = 0
    maximum = 0
    for _ in range(10):
        out_people, in_people = map(int, input().split())
        now += (in_people - out_people)
        if maximum < now:
            maximum = now

    print(maximum)

# print(ai_train_2())

# 피보나치 수 5 https://www.acmicpc.net/problem/10870
# 입력 n 번째 피보나치 수 구하기
def fibonacci_5(n):
    n = int(input())
    dp = {}
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 2] +  dp[i - 1]

    return dp[n]

# print(fibonacci_5(17))

# 일곱 난쟁이 https://www.acmicpc.net/problem/2309
# 9명중 2명을 빼라. (7명의 키의 합이 100이 되도록)
def snow_white():
    dwarfs = []
    results = []
    for _ in range(9):
        dwarfs.append(int(input()))

    for i in range(len(dwarfs)):
        for j in range(i + 1, len(dwarfs)):
            if sum(dwarfs) - dwarfs[i] - dwarfs[j] == 100:
                results = sorted([dwarfs[k] for k in range(len(dwarfs)) if i != k and j != k])

    for result in results:
        print(result)

# print(snow_white())


# 최대공약수와 최소 공배수 https://www.acmicpc.net/problem/2609
# lcm = gcd * (a // gcd) * (b // gcd) 을 이용하자
# gcd * lcm = a * b 를 이용하자
def GCD_LCM(a, b):
    ################### GCD => LCM
    a, b = map(int, input().split())
    def find_divisor(number):
        divisors = []
        for i in range(1, number + 1):
            if number % i == 0:
                divisors.append(i)

        return divisors

    a_divisor = find_divisor(a)
    b_divisor = find_divisor(b)
    GCD = [x for x in a_divisor if x in b_divisor][-1]
    LCM = ((a // GCD) * (b // GCD)) * GCD

    print(GCD)
    print(LCM)
    ################### LCM => GCD
    a_multiple = a
    b_multiple = b
    left = 1
    right = 1

    while a_multiple * left != b_multiple * right:
        if a_multiple * left < b_multiple * right:
            left += 1
        else:
            right += 1

    LCM_2 = a_multiple * left
    GCD_2 = (a * b) // LCM_2

    print(GCD_2)
    print(LCM_2)

# print(GCD_LCM(24, 18))

def nth_bigger():
    n = int(input())
    numberses = []

    for _ in range(n):
        numberses.append([x for x in map(int, input().split())])


    def quick_sort(arr):
        if len(arr) == 0:
            return []
        pivot = arr[0]
        left = [x for x in arr[1:] if pivot < x]
        right = [x for x in arr[1:] if pivot > x]

        return quick_sort(right) + [pivot] + quick_sort(left)
    for numbers in numberses:
        print(quick_sort(numbers)[-3])

# print(nth_bigger([931, 240, 986, 894, 826, 640, 965, 833, 136, 138]))

# 소수 찾기 https://www.acmicpc.net/problem/1978
def find_prime_number(numbers):
    # n = int(input())
    count = 0
    # numbers = [x for x in map(int, input().split())]
    def find_prime(number):
        if number == 1:
            return False

        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    for number in numbers:
        if find_prime(number):
            count += 1

    print(count)

# print(find_prime_number([1,3,5,7]))


# 쉽게 푸는 문제 https://www.acmicpc.net/problem/1292
# 구현
def easy_problem(a, b):
    a, b = map(int, input().split())
    result = 0
    i = 1
    length = 0
    strings = []
    while length < b:
        length += len([str(i) for _ in range(i)])
        strings.append([str(i) for _ in range(i)])
        i += 1

    count = 0
    for i in range(len(strings)):
        for j in range(len(strings[i])):
            count += 1
            if a - 1 < count <= b:
                result += int(strings[i][j])

    print(result)

# print(easy_problem(3, 7))

def prime_sum_min(a, b):
    a = int(input())
    b = int(input())

    primes = []
    def find_prime(number):
        if number == 1:
            return False

        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    for num in range(a, b + 1):
        if find_prime(num):
            primes.append(num)

    if len(primes) > 0:
        print(sum(primes))
        print(primes[0])
    else:
        print(-1)

# print(prime_sum_min(60, 100))

# 연산자 끼워 넣기 https://www.acmicpc.net/problem/14888
# n개의 수, n-1개의 연산자
def operator_attach(numbers, operators):
    numbers = []
    operators = []
    n = int(input())
    numbers = [x for x in map(int, input().split())]
    operators = [x for x in map(int, input().split())]

    results = []

    def dfs(ops, curr, nums):
        if len(nums) == 0:
            results.append(curr)

        for i, op in enumerate(ops):
            if op > 0:
                temp = ops[:]
                temp[i] -= 1
                if i == 0:
                    dfs(temp, curr + nums[0], nums[1:])
                elif i == 1:
                    dfs(temp, curr - nums[0], nums[1:])
                elif i == 2:
                    dfs(temp, curr * nums[0], nums[1:])
                elif i == 3:
                    if curr < 0:
                        dfs(temp, -1 * (-1 * curr // nums[0]), nums[1:])
                    else:
                        dfs(temp, curr // nums[0], nums[1:])

    dfs(operators[:], numbers[0], numbers[1:])

    print(max(results))
    print(min(results))

# print(operator_attach([1,2,3,4,5,6], [2,1,1,1]))


# 괄호의 값 https://www.acmicpc.net/problem/2504
def bracket_value(brackets):
    # brackets = input()
    results = []
    obj = {"[": 3, "(": 2}

    stack = []

    for bracket in brackets:
        if bracket in ["]", ")"]:
            if stack:
                if stack[-1] == '[' and bracket == ']':
                    results = [[len(stack), obj[stack[-1]]]] + results[:]
                    stack.pop()

                elif stack[-1] == '(' and bracket == ')':
                    results = [[len(stack), obj[stack[-1]]]] + results[:]
                    stack.pop()
            else:
                # '[, (' 가 먼저 들어 올 때 처리
                print(0)
                return
        else:
            stack.append(bracket)


    while len(results) > 1:
        max_depth, idx = max([[x[0], i] for i, x in enumerate(results)])
        if results[idx - 1][0] < max_depth:
            results[idx] = [results[idx - 1][0], results[idx][1] * results[idx -1][1]]
            results.pop(idx - 1)

        elif results[idx - 1][0] == max_depth:
            results[idx] = [results[idx - 1][0], results[idx][1] + results[idx -1][1]]
            results.pop(idx - 1)


    if len(stack) > 0:
        print(0)
    else:
        print(results[0][1])

# print(bracket_value(']()'))

# 빗물 https://www.acmicpc.net/problem/14719
def rain_drop(height, width, board):
    height, width = map(int, input().split())
    board = [x for x in map(int, input().split())]
    rain = 0

    idx = 1
    while idx < width - 1:
        left_max = max([x for i, x in enumerate(board) if i < idx])
        right_max = max([x for i, x in enumerate(board) if i > idx])

        if left_max != 0 and right_max != 0:
            if min(left_max, right_max) - board[idx] > 0:
                rain += min(left_max, right_max) - board[idx]

        idx += 1

    print(rain)

# print(rain_drop(3, 5, [0, 0, 0, 2, 0]))

# 가르침 https://www.acmicpc.net/problem/1062
def teaching(n, k, words):
    import itertools
    # n, k = map(int, input().split())
    # words = []
    # for _ in range(n):
    #     words.append(input())
    maximum = 0
    taught = list('antic')
    k = k - 5
    words =[[y for y in x[4:-3] if y not in taught] for x in words]
    arr = []
    for word in words:
        for x in word:
            if x not in arr:
                arr.append(x)

    lists = list(itertools.combinations(arr, k))

    for li in lists:
        count = 0
        for word in words:
            if not any([x not in li for x in word]):
                count += 1

        maximum = max(maximum, count)

    print(maximum)



print(teaching(9, 8, ['antabtica',
'antaxtica',
'antadtica',
'antaetica',
'antaftica',
'antagtica',
'antahtica',
'antajtica',
'antaktica']))
