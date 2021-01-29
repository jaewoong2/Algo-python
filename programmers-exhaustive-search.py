def test_math_give_up():
    answers = [1,3,2]
    def solution(answers):
        answer = []
        persons = {
            1: [1, 2, 3, 4, 5],
            2: [2, 1, 2, 3, 2, 4, 2, 5],
            3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        }

        for person in persons:
            # 싸이클 문제는 " % " 수식을 이용하자.
            ans = [answers[i] - persons[person][i % len(persons[person])] == 0 for i in range(len(answers))]
            answer.append((ans.count(True), person))

        max_person = max(answer, key= lambda x: x[0])
        return list(filter(lambda x: x != False, list(map(lambda x: x[0] == max_person[0] and x[1], answer))))

    return solution(answers)

# print(test_math_give_up())

def permutation(arr, r):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    return_array = []
    def generate(chosen, used):
        # 내가 원하는 만큼 뽑았으면, return
        if len(chosen) == r:
            return_array.append(''.join(chosen))
            return

        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)
    return return_array

def find_prime_number():
    numbers = "110"

    def solution(numbers):
        list_numbers = [x for x in numbers]
        count = 0
        array = []

        for i in range(len(list_numbers)):
            array.extend(permutation(list_numbers, i + 1))
        array = list(set(map(int, array)))

        def is_prime(n):
            prime = True
            if n < 2:
                return False
            for i in range(2, n):
                if n % i == 0:
                    prime = False
                    break
            return prime

        for num in array:
            if is_prime((num)):
                count += 1

        return count
    return solution(numbers)

# print(find_prime_number())

def carpet():
    brown = 10
    yellow = 2
    def solution(brown, yellow):

        for i in range(1, yellow + 1):
            if yellow % i == 0:
                k = yellow / i

                if brown == (i * 2) + (k * 2) + 4:
                    return [int(max(i, k) + 2), int(min(i, k) + 2)]

    return solution(brown,yellow)

print(carpet())



def dfs_permutation(array, r):
    i_array = [(x, i) for i, x in enumerate(array)]
    stack = [[i] for _, i in i_array]
    return_list = []

    while len(stack) > 0:
        current = stack.pop()

        for i in range(len(i_array)):
            if i not in current:
                temp = current + [i_array[i][1]]
                if len(temp) == r:
                    elements = []
                    for idx in temp:
                        elements.append(i_array[idx][0])
                    return_list.extend([elements])
                else:
                    stack.append(temp)
    return return_list

print(dfs_permutation("ABCD", 2))


def combination(array, r):
    chosen = []
    if r > len(array):
        return chosen

    if r == 1:
        for i in array:
            chosen.append(i)

    elif r > 1:
        # r 개 만큼 빼주는 이유 (순서가 고려사항이 아니기 때문에, r개는 고려하지 않아도 앞서서 정해진다)
        for i in range(len(array) - r + 1):
            for temp in combination(array[i + 1:], r - 1):
                chosen.append([array[i], temp])
    return chosen

print(combination("ABCD", 2))
