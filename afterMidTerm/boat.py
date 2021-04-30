# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people: list, limit):
    people.sort()
    small = 0
    big = len(people) - 1
    count = 0

    while small <= big:
        if len(people) > 1 and people[small] + people[big] <= limit:
            small += 1
            big -= 1
        else:
            big -= 1

        count += 1

    return count

print(solution([70, 50, 80, 50], 100))