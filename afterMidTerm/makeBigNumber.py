# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    start = 0
    last = k
    s = ''

    while len(s) < len(number) - k:
        if last > 0:
            max_number = number[start]
            max_index = start

            for i in range(start, start + last + 1):
                if max_number == '9':
                    break
                if max_number < number[i]:
                    max_number = number[i]
                    max_index = i

            last = start + last - max_index
            start = max_index + 1
            s += max_number

        else:
            s += number[start:]

    return s