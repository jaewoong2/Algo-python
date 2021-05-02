def solution(numbers):
    numbers = [str(x) for x in numbers]
    max_length = len(max(numbers, key=lambda x:len(x)))
    positioned_numbers = []
    for i in range(len(numbers)):
        number = numbers[i]
        length = len(number)
        if length < max_length:
            number *= int(max_length / length) + 1
            number = number[:max_length]
        positioned_numbers.append((number, i))

    positioned_numbers.sort(key= lambda x:x[0], reverse=True)

    numbers = [numbers[i] for _, i in positioned_numbers]

    return str(int(''.join([x for x in numbers])))

print(solution([3, 30, 34, 5, 9]))