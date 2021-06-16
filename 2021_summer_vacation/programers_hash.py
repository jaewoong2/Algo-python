# 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576

def not_completion():
    def solution(participants, completions):
        hash = { participant: 0 for participant in participants }

        for participant in participants:
            hash[participant] += 1

        for completion in completions:
            hash[completion] -= 1


        return [v for v in hash if hash[v] > 0][0]

    print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))


# 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577

def phone_book_index():
    def solution(phone_book):
        lengths = set(len(number) for number in phone_book)
        hash = {number: True for number in phone_book}
        for length in lengths:
            for number in phone_book:
                if number[:length] in hash and number != number[:length]:
                    return False

        return True


    print(solution(["119", "97674223", "1195524421"]))

# phone_book_index()


# 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578

def camouflage():
    def solution(clothes):
        result = 1
        hash = {}
        for value, key in clothes:
            if key in hash:
                hash[key].append(value)
            else:
                hash[key] = [value]

        for key in hash:
            result *= len(hash[key]) + 1

        return result - 1

    return solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])

# print(camouflage())


# 베스트엘범
# https://programmers.co.kr/learn/courses/30/lessons/42579

def best_album():
    def solution(genres, plays):
        hash = {}
        result = []
        for i, genre in enumerate(genres):
            if genre in hash:
                hash[genre].append([i, plays[i]])
            else:
                hash[genre] = [[i, plays[i]]]

        # 1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
        for genre in sorted([[key, sum([value[1] for value in hash[key]])] for key in hash], key = lambda x: x[1], reverse=True):
            # 2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
                # 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
            arr = [x[0] for x in sorted(hash[genre[0]], key= lambda y: y[1], reverse= True)]
            result.extend(arr[:2])

        return result

    return solution(["classic", "pop", "classic", "classic", "pop"], [500, 2500, 2500, 800, 2500])

print(best_album())
