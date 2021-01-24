# 단순 재귀 함수로 피보나치 수열을 해결하면 지수 시간 복잡도를 가진다
# 중복되는 부분 문제가 많다

# 다이나믹 프로그래밍
# 1. 최적 부분 구조: 큰 문제를 작은 문제로 나눌 수 있다
# 2. 중복 되는 부분 문제: 동일한 작은 문제를 반복적으로 해결 가능
def fibonazzi(x):
    if x == 1 or x == 2:
        return 1
    return fibonazzi(x - 1) + fibonazzi(x - 2)


# print(fibonazzi(1))

# 메모리제이션
# 한 번 계산한 결과를 메모리 공간에 메모하는 기법
# Casing 기법을 사용 (dp, d) = 탑 다운 (재귀적)

def use_memorization(n: int, x: int):
    d = [0] * n

    def fibo(x):
        if x == 1 or x == 2:
            return 1

        if d[x] != 0:
            return d[x]

        d[x] = fibo(x - 1) + fibo(x - 2)
        return d[x]

    return fibo(x)

def fibo_dynamic(x):
    d = [0] * (x + 1)
    def get_fibo(x):
        if x == 1 or x == 2:
            return 1

        if d[x] != 0:
            return d[x]

        # d[x] 에 값이 들어오지 않으면
        d[x] = get_fibo(x - 1) + get_fibo(x - 2)

        return d[x]
    return get_fibo(x)


# print(use_memorization(100, 99))

# 바텀업 방식(dp 테이블)은, 반복문을 사용해서 dp의 초기값을 설정 해주는 것이 좋다
def get_fibo_with_DP(n: int):
    d = [0] * (n + 1)

    d[1] = 1
    d[2] = 1

    for i in range(3, n + 1):
        d[i] = d[i - 2] + d[i - 1]

    return d[n]


# print(get_fibo_with_DP(99))


# 개미 전사
import math


def ant_warrior(array: list):
    results = []

    def get_meal(n: int):
        result = 0
        now = -1
        for i in range(n, (len(array))):
            if i != now + 1:
                now = i
                result += array[i]
        return result

    for i in range(math.ceil(len(array) / 2)):
        results.append(get_meal(i))

    return max(results)


print(ant_warrior([1, 3, 1, 5, 7, 4, 11]))


def ant_warrior_dynamic(array):
    n = len(array)
    d = [0] * n

    d[0] = array[0]
    d[1] = max(array[0], array[1])
    for i in range(2, n):
        d[i] = max(d[i - 1], d[i - 2] + array[i])

    return d[len(array) - 1]


print(ant_warrior_dynamic([1, 3, 1, 5, 7, 4, 11]))


def make_one(x: int):
    d = [0] * (x + 1)
    for i in range(2, x + 1):
        d[i] = d[i - 1] + 1

        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)

        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)

        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)

    return d[x]


print(make_one(26))


def make_dollar_eff(target, dollars):
    d = [10001] * (target + 1)

    d[0] = 0
    for i in range(len(dollars)):
        for j in range(dollars[i], target + 1):
            if d[j - dollars[i]] != 10001:
                d[j] = min(d[j], d[j - dollars[i]] + 1)

    if d[target] == 10001:
        print(-1)
    else:
        print(d[target])


make_dollar_eff(7, [2, 3, 5])


# 다이나믹 프로그래밍
# 최대, 최소 (횟수) 를 구할 때 적절하다
# 점화식을 구하자
def ant_fighter(array: list) -> int:
    length = len(array)
    d = [0] * length

    d[0] = array[0]
    d[1] = max(array[0], array[1])

    for i in range(2, length):
        d[i] = max(d[i - 2] + array[i], d[i - 1]) # dp 에 저장된 것을 기억해야한다

def make_one_dynamic(x: int):
    length = x + 1
    d = [0] * length
    for i in range(2, length):
        if x % 5 == 0:
            d[i] = min(d[i // 5] + 1, d[i - 1] + 1)
        elif x % 3 == 0:
            d[i] = min(d[i // 3] + 1, d[i - 1] + 1)
        elif x % 2 == 0:
            d[i] = min(d[i // 2] + 1, d[i - 1] + 1)
    return d[x]

print('1 -->',make_one_dynamic(26))


def get_mine():
    n, m = map(int, input().split())
    array = (list(map(int, input().split())))
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index: index + m])
        index += m
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)
# get_mine()

def get_mine_dynamic(array):
    n, m = len(array), len(array[0])
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index: index + m])
        index += m

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)



def display_marin(marin: list):
    indexes = [marin[0]]

    for i in range(1, len(marin)):
        if indexes[len(indexes) - 1] < marin[i]:
            indexes.pop()
        indexes.append(marin[i])

    return len(marin) - len(indexes)

print(display_marin([15, 11, 4, 8, 5, 2, 4]))


def display_marin_dynamic():
    n = int(input())
    array = list(map(int, input().split()))
    array.reverse()

    dp = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + 1)
