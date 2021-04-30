# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    import collections
    queue = collections.deque([[i, x] for i, x in enumerate(priorities)])
    count = 0
    while queue:
        i, v = queue.popleft()
        if (any(x > v for j, x in queue)):
            queue.append((i, v))
        else:
            count += 1
            if i == location:
                return count


    return count

print(solution([1, 1, 9, 1, 1, 1], 0))

