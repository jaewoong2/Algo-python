# 동빈북

# 1. 큰 수의 법칙 p92

# 개인 풀이
def rules_of_big_number(N, M, K, numbers):
    result = 0
    maxes = [x for x in numbers if x == max(numbers)]

    if len(maxes) > 1:
        return maxes[0] * M

    else:
        max_f = maxes[0]
        max_s = sorted([x for x in numbers if x < max(numbers)], reverse= True)[0]
        i = 0
        while i < M:
            j = 0
            while j < K:
                result += max_f
                j +=1
                i +=1
            result += max_s
            i += 1

        return result

# print(rules_of_big_number(5, 7, 2, [3, 4, 3, 4, 3]))

# 풀이 (수정)

def rules_of_big_number_2(N, M, K, numbers):
    numbers.sort()
    result = 0
    first = numbers[-1]
    second = numbers[-2]
    i = 0
    while i < M:
        j = 0
        while j < K and i < M:
            result += first
            j += 1
            i += 1
        if i < M:
            result += second
            i += 1

    return result

# print(rules_of_big_number_2(5, 7, 2, [3, 4, 3, 4, 3]))

# 숫자 카드 게임 p. 96

# 개인 풀이

def game_of_number_card(N, M, cards):
    newCards = []
    for row in range(N):
        temp = []
        for col in range(M):
            temp.append(cards.pop(0))
        newCards.append(temp)

    mines = 0
    for row in range(N):
        mines = max(mines, min(newCards[row]))
    return mines

# print(game_of_number_card(2, 4, [7, 3, 1, 8, 3, 3, 3, 4]))


# 1이 될 때 까지
def until_one(N, K):
    count = 0

    while N > K:
        while N % K != 0:
            N -= 1
            count += 1

        N = N // K
        count += 1

    if N > 1:
        count += 1
        N -= 1

    return count

# print(until_one(25, 3))


def until_one_2(N, K):
    result = 0

    while N >= K:
        while N % K != 0:
            N -= 1
            result += 1
        N //= K
        result += 1


    while N > 1:
        N -= 1
        result += 1

    return result

# print(until_one_2(27, 3))

# 상하좌우 p.110

def LRUD(n, moves):
    now = [1, 1]
    for move in moves:
        if move == 'L':
            if now[0] != 1:
                now = [now[0] - 1, now[1]]
        elif move == 'R':
            if now[0] != n:
                now = [now[0] + 1, now[1]]
        elif move == 'U':
            if now[1] != 1:
                now = [now[0], now[1] - 1]
        elif move == 'D':
            if now[1] != n:
                now = [now[0], now[1] + 1]

    return list(reversed(now))

# print(LRUD(5, ['R','R','R','U','D','D']))

# 왕실의 나이트 p.115
def knight_of_kingdom(position):
    n = 8
    col = {x: i + 1 for i, x in enumerate('abcdefgh')}
    now = [int(position[1]), col[position[0]]]
    count = 8
    moves = [[-2, +1], [-2, -1], [2, 1], [2, -1]]

    for move in moves:
        reversedMove = list(reversed(move))
        if now[0] + move[0] < 1 or now[1] + move[1] > n or now[0] + move[0] > n or now[1] + move[1] < 1:
            count -= 1

        if now[0] + reversedMove[0] < 1 or now[1] + reversedMove[1] > n or now[0] + reversedMove[0] > n or now[1] + reversedMove[1] < 1:
            count -= 1

    return count

# print(knight_of_kingdom('a1'))

# 게임 개발 p.118 (다시풀기)
def development_game(n, m, position, map):
    point = { 0: 'North', 1: "East", 2: "South", 3: "West" }
    cash = []
    stop = [False]

    def view_point(view):
        if view == 0: return 3
        return view - 1

    def find_land(pos):
        row, col, view = pos
        moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        flag = ''
        for move in moves:
            if [row + move[0], col + move[1]] in cash or map[row + move[0]][col + move[1]] == 1:
                flag += '1'

        if flag == '1111':
            if point[view] == 'North':
                if [row - 1, col] not in cash and row - 1 > 0 and map[row + 1][col] == 0:
                    row += 1

                if map[row + 1][col] == 1:
                    stop[0] = True

            elif point[view] == 'East':
                if [row, col + 1] not in cash and col + 1 <= m and map[row][col - 1] == 0:
                    col -= 1
                if map[row][col - 1] == 1:
                    stop[0] = True
            elif point[view] == 'South':
                if [row + 1, col] not in cash and row + 1 <= n and map[row - 1][col] == 0:
                    row -= 1
                if map[row - 1][col] == 1:
                    stop[0] = True
            elif point[view] == 'West':
                if [row, col - 1] not in cash and col - 1 > 0 and map[row][col + 1] == 0:
                    col += 1
                if map[row][col + 1] == 1:
                    stop[0] = True


        return [row, col, view]


    def canMove(pos):
        row, col, view = find_land(pos)
        view = view_point(view)
        nextPosition = moving([row, col, view])
        if [nextPosition[0], nextPosition[1]] not in cash:
            cash.append([nextPosition[0], nextPosition[1]])
        return nextPosition


    def moving(pos):
        row, col, view = pos
        if point[view] == 'North':
            if [row - 1, col] not in cash and row - 1 > 0 and map[row - 1][col] == 0:
                row -= 1
        elif point[view] == 'East':
            if [row, col + 1] not in cash and col + 1 <= m and map[row][col + 1] == 0:
                col += 1
        elif point[view] == 'South':
            if [row + 1, col] not in cash and row + 1 <= n and map[row + 1][col] == 0:
                row += 1
        elif point[view] == 'West':
            if [row, col - 1] not in cash and col - 1 > 0 and map[row][col - 1] == 0:
                col -= 1

        return [row, col, view]

    while not stop[0]:
        position = canMove(position)
    return len(cash)

print(development_game(4, 4, [1, 1, 0], [[1,1,1,1], [1,0,0,1], [1,1,0,1], [1,1,1,1]]))