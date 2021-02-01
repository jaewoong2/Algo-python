def doll_pick_up():
    board = [
        [0,0,0,0,0],
        [0,0,1,0,3],
        [0,2,5,0,1],
        [4,2,4,4,2],
        [3,5,1,3,1]
    ]
    moves = [1,5,3,5,1,2,1,4]
    def solution(board, moves):
        answer = 0
        board_hash = {}
        for i in range(len(board)):
            for j in range(len(board)):
                if i + 1 in board_hash:
                    board_hash[i + 1].append(board[j][i])
                else:
                    board_hash[i + 1] = [board[j][i]]

        save_box = []
        while moves:
            move = moves.pop(0)

            for i in range(len(board_hash[move])):
                if board_hash[move][i] != 0:
                    if len(save_box) > 0 and save_box[len(save_box) - 1] == board_hash[move][i]:
                        save_box.pop()
                        answer += 2
                    else:
                        save_box.append(board_hash[move][i])
                    board_hash[move][i] = 0
                    break
        return answer

    return solution(board, moves)

# print(doll_pick_up())

def pick_two_numbers_and_sum():
    def solution(numbers):
        return sorted(
            list(set([numbers[i] + numbers[j] for i in range(len(numbers)) for j in range(i + 1, len(numbers))])))

    return solution([0,0,0,0,0,])

# print(pick_two_numbers_and_sum())

def make_new_id():
    def solution(new_id: str):
        # 1단계 아이디의 모든 대문자를 소문자로 바꿔라
        special_word = "~ ! @ # $ % ^ & * ( ) = + [ { ] } : ? , < > /".split(' ')
        id_new = []
        for alpha in new_id:
            if alpha.isalpha():
                id_new.append(alpha.lower())
            else:
                id_new.append(alpha)
                
        # 2단계 문자 지우기
        id_new = [x for x in id_new if x not in special_word]

        # 3단계 마침표가 중복되면 하나로 줄이기

        for i, word in enumerate(id_new):
            end_point = -1
            if word == '.':
                for j in range(i + 1, len(id_new)):
                    if id_new[i + 1] == '.':
                        if id_new[j] != '.':
                            end_point = j
                            break
            if end_point > 0:
                for idx in range(len(id_new)):
                    if idx > i or idx >= end_point:
                        id_new[i] = ''


        # 4단계 아이디의 처음에 위치한 '.' 제거
        id_new = [x for x in id_new if x != '']
        id_new = [x for i, x in enumerate(id_new) if not(i == 0 and x == '.') if not(i == len(id_new) - 1 and x == '.')]

        if len(id_new) == 0:
            id_new.append('a')

        if len(id_new) > 15:
            id_new = id_new[0:15]

        while id_new[-1] == '.':
            id_new = [x for i, x in enumerate(id_new) if not(i == 0 and x == '.') if not(i == len(id_new) - 1 and x == '.')]

        while len(id_new) < 3:
            id_new.append(id_new[-1])

        return ''.join(id_new)

    return solution("...!@BaT#*..y.abcdefghijklm")

# print(make_new_id())


# 체육복
def training_clothe():
    def solution(n: int, lost: list, reserve: list):
        l_answer = n - len(lost)
        r_answer = n - len(lost)
        l_dict_reserve = {0: False, n + 1: False}
        r_dict_reserve = {0: False, n + 1: False}

        for i in range(n):
            if i + 1 in reserve:
                l_dict_reserve.setdefault(i + 1, True)
                r_dict_reserve.setdefault(i + 1, True)
            else:
                l_dict_reserve.setdefault(i + 1, False)
                r_dict_reserve.setdefault(i + 1, False)

        for i, person_lost in enumerate(lost):
            if r_dict_reserve[person_lost]:
                r_dict_reserve[person_lost] = False
                r_answer += 1
            elif r_dict_reserve[person_lost + 1] and person_lost + 1 not in lost:
                r_dict_reserve[person_lost + 1] = False
                r_answer += 1
            elif r_dict_reserve[person_lost - 1] and person_lost - 1 not in lost:
                r_dict_reserve[person_lost - 1] = False
                r_answer += 1


        for i, person_lost in enumerate(lost):
            if l_dict_reserve[person_lost]:
                l_dict_reserve[person_lost] = False
                l_answer += 1
            elif l_dict_reserve[person_lost - 1] and person_lost - 1 not in lost:
                l_dict_reserve[person_lost - 1] = False
                l_answer += 1
            elif l_dict_reserve[person_lost + 1] and person_lost + 1 not in lost:
                l_dict_reserve[person_lost + 1] = False
                l_answer += 1


        return max(l_answer, r_answer)

    return solution(5, [1,2,4,5], [2,3,4])

print(training_clothe())

def two_zero_one_six():
    def solution(a, b):
        month_day = [31,29,31,30,31,30,31,31,30,31,30,31]
        diff_m = a - 1
        date = b + 4
        for i in range(diff_m):
            date += month_day[i]

        day = ["SUN","MON","TUE","WED","THU","FRI","SAT"]

        return day[date % 7]

    return solution(5, 24)

print(two_zero_one_six())


# 삼진법 뒤집기
def three_reverse():
    def solution(n):
        three = ''
        answer = 0
        while n >= 3:
            three += str(n % 3)
            n = n // 3
        three += str(n)

        three = [x for x in three]

        count = 0
        while three:
            now = three.pop()
            answer += int(now) * (3 ** count)
            count += 1

        return answer
    return solution(45)

print(three_reverse())

def hate_same_number():
    def solution(arr):
        arr_ = [arr[0]]
        for i in range(1, len(arr)):
            if arr_[-1] != arr[i]:
                arr_.append(arr[i])

        return arr_

    return solution([1,1,3,3,0,1,1])

print(hate_same_number())