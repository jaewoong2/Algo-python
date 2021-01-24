# 그리디 알고리즘

# 그리디 알고리즘은 현재 상황에서 지금 당장 좋은 것만 고르는 방법

# 거스름 돈 문제
# o(k)
def moneyChange(n):
    count = 0
    coins = [500, 100, 50, 10]
    for coin in coins:
        count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 갯수 새기
        # // 연산자는 나눈 후 소숫점을 버리고 정수를 반환 하는 연산자이다
        n %= coin
        # n 을 coin 으로 나눈 나머지 값 으로 대입
    print(count)

# moneyChange(1260)

# 1이 될때까지
def whileOne(n, k, count):
    if n == 1:
        print(count)
        return
    if n % k == 0:
        n = n // k
    else:
        n = n - 1
    count = count + 1
    whileOne(n, k, count)

# whileOne(25, 3, 0)

# 아이디어가 정당성을 분석하는 것이 중요하다.


# 복잡도가 단순하다
def whileOneOLogN(n, k):

    result = 0 # 결과 값

    while True: # n 값이 K보다 크거나 같을 때 까지 반복한다
        # target = n을 k로 나누어 떨어지개 만든 후 k를 곱한 값 즉, n 을 k 로 나누어 질때 까지 뺀 값
        # 가장 가까운 나눠 떨어지는 값을 얻는 방법
        target = (n // k) * k

        # result = 얼마나 뺐는지 결과 값에 더해준다 (즉, -1 의 갯수당 실행 횟수 1번이기 때문)
        result += (n - target)

        # n 을 1을 나누어질 때 까지 뺀 값으로 준다.
        n = target

        # 만약, n이 k로 나누어지지 않는다면 실행을 멈춘다.
        if n < k:
            break
        # 실행 1회 추가 (n 을 k로 나누었기 떄문)
        result += 1
        # n을 k로 나눈 정수의 몫을 n에 대입.
        n //= k

    # n이 k보다 작지만, 1보다 클경우 그만큼 실행 횟수를 더해주기 위함
    result += n - 1
    print(result)

# n, k = map(int, input().split())
# whileOneOLogN(n, k) # 입력 값으로 받은 값을 n과 k 로 int 형으로 각각 받는다.


# 곱하기 혹은 더하기
def multiOrAdd(inputS: str):
    s = (list(map(int, inputS.split(' '))))
    temp = s[0]
    for i in range(1, len(s)):
        if temp <= 1 or s[i] <= 1:
            temp += s[i]
        else:
            temp *= s[i]
    print(temp)

# multiOrAdd("0 2 9 8 4")

#모험가 길드
def guild(users):
    users.sort()
    result = 0
    count = 0

    for user in users:
        count += 1
        if count >= user:
            result += 1
            count = 0
    print(result)

# guild([2, 3, 1, 2, 2])


#상화좌우 문제
def getPostion():
    n = int(input())
    x, y = 1, 1
    plans = input().split()
    # L,R,U,D에 따른 이동방향 (방향 벡터를 위함)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']
    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        # 공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        # 이동 수행
        x, y = nx, ny
    print(x, y)

#getPostion()

def getPosition(space, moves):
    x, y = 1, 1

    #행
    dx = [0, 0, -1, 1]
    #열
    dy = [-1, 1, 0, 0]

    moves_plan = ['L', 'R', 'U', 'D']

    for move in moves:
        index = moves_plan.index(move)
        nx = x + dx[index]
        ny = y + dy[index]
        if nx < 1 or ny < 1 or nx > space or ny > space:
            continue
        x, y = nx, ny
        print(x, y)

# getPosition(5, ['R', 'R', 'R', 'U', 'D', 'D'])

# 시각 문제
# 정수 N이 입력 되면 00시 00분 00초 부터 N시 59분 59초 까지의 모든 시각 중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성

def getThreeinTime(n: int):
    count = 0
    hour = 0
    min = 0
    sec = 0
    while hour <= n:
        sec += 1
        if "3" in str(hour) + str(min) + str(sec):
            count += 1
        if sec == 60:
            min += 1
            sec = 0
        if min == 60:
            hour += 1
            min = 0
    print(count)

# getThreeinTime(5)

def KnightOfKingdom(pos: str):
    #행, 열
    col = ["1", "2", "3", "4", "5", "6", "7", "8"]
    row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    count = 8
    colIndex = col.index(pos[1]) + 1
    rowIndex = row.index(pos[0]) + 1

    #좌
    for i in range(3):
        if i == 0:
            continue
        if i == 1:
            if rowIndex - i < 1 or colIndex - 2 < 1:
                count -= 1
            if rowIndex - i < 1 or colIndex + 2 > 8:
                count -= 1
        if i == 2:
            if rowIndex - i < 1 or colIndex - 1 < 1:
                count -= 1
            if rowIndex - i < 1 or colIndex + 1 > 8:
                count -= 1
    #우
    for i in range(3):
        if i == 0:
            continue
        if i == 1:
            if rowIndex + i > 8 or colIndex - 2 < 1:
                count -= 1
            if rowIndex + i > 8 or colIndex + 2 > 8:
                count -= 1
        if i == 2:
            if rowIndex + i > 8 or colIndex - 1 < 1:
                count -= 1
            if rowIndex + i > 8 or colIndex + 1 > 8:
                count -= 1

    print(count)

# KnightOfKingdom("a1")

def GetPostionOfKnight():
    input_data = input()
    row = int(input_data[1])
    col = int(ord(input_data[0]) - int(ord('a')) + 1)

    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    result = 0
    for step in steps:
        next_row = row + step[0]
        next_column = col + step[1]
        if next_row > 0 and next_row < 9 and next_column > 0 and next_column < 9:
            result += 1
    print(result)

def string_sorting(input_str: str):
    number = 0
    s = ''
    for word in input_str:
        if word.isalpha() == False:
            number += int(word)
        else:
            s += word

    result = ''.join(sorted(s))
    print(result + str(number))

string_sorting("AJKDSI41")

def str_sorting(input_str: str):
    result = []
    value = 0

    for word in input_str:
        if word.isalpha():
            result.append(word)
        else:
            value += int(word)
    result.sort()

    if value != 0:
        result.append(str(value))

    print(''.join(result))