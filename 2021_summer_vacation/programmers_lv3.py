
def n_queen(n):
    answer = []
    def is_promising(row, col, result):
        # result = [row, col][]
        flag = True
        for v in result:
            pre_row, pre_col = v
            if flag:
                if row == pre_row or col == pre_col or abs(col - pre_col) == abs(row - pre_row):
                    # 같은 열, 같은 행, 대각선
                    flag = False
        return flag

    def dfs(result, row):
        if len(result) == n:
            answer.append(1)
        else:
            for col in range(n):
                if is_promising(row, col, result):
                    dfs(result + [[row, col]], row + 1)

    dfs([], 0)

    return len(answer)

# print(n_queen(4))

def sticker_attach(sticker):
    if len(sticker) > 1:
        length = len(sticker)
        # dp[index] = index 번 째까지 스티커를 붙혔을 때 최대 값
        dp = [0] * length
        dp_ = [0] * length

        # 0번째 스티커를 붙이는 경우 (맨 마지막 스티커를 버리는 경우)
        dp[0] = sticker[0]
        dp[1] = dp[0]
        for i in range(2, length - 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + sticker[i])

        # 0번째 스티커를 안 붙이는 경우 (맨 마지막 스티커를 붙이는 경우)
        dp_[0] = 0
        dp_[1] = sticker[1]
        for i in range(2, length):
            dp_[i] = max(dp_[i - 1], dp_[i - 2] + sticker[i])


        return max(max(dp), max(dp_))
    return max(sticker)

print(sticker_attach([14, 6, 5, 11, 3, 9, 2, 10]))