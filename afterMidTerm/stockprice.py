# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    seconds = []
    idx = 0

    while len(prices) > idx:
        price = prices[idx]
        sec = 0

        for next_idx in range(idx + 1, len(prices)):
            sec += 1
            if(prices[next_idx] < price):
                break

        seconds.append(sec)
        idx += 1


    return seconds

print(solution([1,2,3,2,3]))