
# k번 째 수

def number_of_k():
    array = [1,5,2,6,3,7,4]
    commands = [[2,5,3], [4,4,1], [1,7,3]]
    def solution(array, commands):
        answer = []

        while commands:
            i, j, k = commands.pop(0) # i ~ j 까지 자르고 난 후 정렬하고 k번 째에 있는 수를 구하시오
            sliced_array = array[i-1 : j]
            sliced_array.sort()
            answer.append(sliced_array[k - 1])

        return answer

    def solution_map_lambda(array, commands):
        return list(map(lambda x: sorted(array[x[0] - 1: x[1]])[x[2] - 1], commands))
    # commands 의 각 값이 lambda 의 x로 변환되고 x = [2, 5, 3] // x = [4, 4, 1] \\ x = [1, 7, 3]
    # 그 x를 이용해서 array 를 slicing 한다.
    # 그리고 sorted() 함수를 이용해서 새로운 list 로 반환 한후, k 위치(x[2])에 있는 값을 찾는다.
    # 그리고 map() 의 반환 값은 map object 이기 때문에
    # list() 로 묶어서 list 로서 반환 한다

    # --- map(function(x ==> Iterable 의 반복 가능한 요소 (ex. list들의 각각의 값)), Iterable) ---
    return solution_map_lambda(array, commands)

print(number_of_k())

def number_of_k_review():
    array = [1,5,2,6,3,7,4]
    commands = [[2,5,3], [4,4,1], [1,7,3]]
    def solution(array, commands):
        return list(map(lambda x: sorted(array[x[0] - 1: x[1]])[x[2] - 1], commands))
    return solution(array, commands)




# 가장 큰 수
def the_biggest_number():
    numbers = [40, 403] #"1111111111"
    def solution(numbers):
        answer = ''
        str_numbers = list(map(str, numbers))
        max_length = max([len(str_number) for str_number in str_numbers])
        new_numbers = []

        for i, number in enumerate(str_numbers):
            new_number = number
            while len(new_number) < max_length:
                new_number += new_number[0: max_length - len(new_number)]
            new_numbers.append((i, new_number))

        new_numbers.sort(key= lambda x: x[1], reverse=True)

        for i, _ in new_numbers:
            answer += str_numbers[i]

        return str(int(answer))

    def solution_functools(numbers):
        import functools

        def comparator(now, next):
            str = int(now + next)
            reverse_str = int(next + now)

            if str > reverse_str:
                return 1
            elif str == reverse_str:
                return 0
            else:
                return -1
        def solution(numbers):
            numbers = [str(number) for number in numbers]
            numbers.sort(key=functools.cmp_to_key(comparator), reverse=True)

            answer = str(int(''.join(numbers)))

            return answer
        return solution(numbers)


    return solution_functools(numbers)

print(the_biggest_number())


def the_biggest_number_review():
    numbers = [5, 5555, 555, 50, 5] #"1111111111"

    def solution(numbers):
        str_numbers = list(map(str, numbers))
        max_length = max([len(x) for x in str_numbers])
        new_str_numbers = [(x * (max_length - len(x) + 1), i) for i, x in enumerate(str_numbers)]
        new_str_numbers.sort(reverse=True)
        new_numbers = [(x[0: max_length], i) for x, i in new_str_numbers]

        return str(int(''.join([str_numbers[i] for _, i in new_numbers])))

    return solution(numbers)

print(the_biggest_number_review())

# H-index

def H_index():
    def solution(citations):
        counts = []
        h = max(citations)
        while h >= 0:
            count = 0
            for i, citation in enumerate(citations):
                if h <= citation:
                    count += 1

            if count >= h:
                counts.append(h)
            h -= 1

        return max(counts)

    return solution([0, 0, 0, 0, 0])

print(H_index())



