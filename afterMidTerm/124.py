# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    if n == 0:
        return '4'
    if n == 1:
        return '1'
    if n == 2:
        return '2'
    if n == 3:
        return '4'

    if n > 3:
        return solution(int((n - 1) / 3)) + solution(n % 3)

print(solution(3))

