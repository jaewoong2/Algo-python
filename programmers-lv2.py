# 124 나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899

def one_two_four():
    n = 15 # 111
    def solution(n):
        def find_number(num):
            if num == 1 or num == 2:
                return num
            if num == 3 or num == 0:
                return 4

            if num % 3 == 0:
                return str(find_number((num // 3) - 1)) + str(find_number(num % 3))
            return str(find_number(num // 3)) + str(find_number(num % 3))

        return find_number(n)

    def solution_loop(n):
        num = ["1", "2", "4"]
        answer = ""

        while n > 0:
            n -= 1
            answer = num[n % 3] + answer
            n = n // 3

    return solution_loop(n)

# print(one_two_four())


# 실패! -> 왜 최대 공약수?
def rectangle():
    w = 3
    h = 11
    def solution(w, h):
        min_number = min(w, h)
        max_number = max(w, h)
        if max_number % min_number == 0:
            y = max_number // min_number
        else:
            y = (max_number // min_number) + 1

        print(max_number / min_number)
        if abs((max_number // min_number) - (max_number / min_number)) > 0.5:
            return ((w * h) - (y * min_number)) - 1

        return ((w * h) - (y * min_number))

    return solution(w, h)

# print(rectangle())

def skill_tree():
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    def solution(skill, skill_trees):
        skill = [x for x in skill]
        answer = 0

        while skill_trees:
            skills = list(skill)
            trees = [x for x in skill_trees.pop()]

            for s in trees:
                if s in skill:
                    if s != skills.pop(0):
                        break
            else:
                answer += 1
        #
        # while skill_trees:
        #     trees = [x for x in skill_trees.pop()]
        #     seq = []
        #     flag = True
        #
        #     for i in range(len(skill)):
        #         if skill[i] in trees:
        #             seq.append(str(trees.index(skill[i])))
        #         else:
        #             seq.append(9999999)
        #
        #     for i in range(len(seq) - 1):
        #         if int(seq[i]) > int(seq[i + 1]):
        #             flag = False
        #             break
        #
        #     if flag:
        #         answer += 1

        return answer

    return solution(skill, skill_trees)

print(skill_tree())