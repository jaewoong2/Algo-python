def is_prime(target):
    if target == 1 or target == 0:
        return False
    for i in range(2, int(target ** 0.5) + 1):
        if target % i == 0: return False
    return True

def solution(numbers):
    import itertools
    nums = set()
    for i in range(1, len(numbers) + 1):
        for n in [''.join(x) for x in itertools.permutations(numbers, i)]:
            if n != '':
                nums.add(int(n))
    count = 0

    for num in nums:
        if is_prime(num):
            count += 1

    return count

print(solution("011"))