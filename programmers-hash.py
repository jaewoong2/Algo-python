# 1. 완주하지 못한 선수

def not_finished():
    participant = ['mislav', 'stanko', 'mislav', 'ana']
    completion = ['stanko', 'ana', 'mislav']

    def solution(participant, completion):
        answer = ''
        participant.sort()
        completion.sort()

        for idx in range(len(participant)):
            if participant[idx] != completion[idx]:
                answer = participant[idx]
                break
        return answer

    def solution_hash(participant, completion):
        answer = ''
        temp = 0
        dic = {}

        for part in participant:
            dic[hash(part)] = part
            temp += hash(part)
        for com in completion:
            temp -= hash(com)
        answer = dic[temp]
        return answer

    return solution_hash(participant, completion)

# print(not_finished())

def not_finished_hash():
    participant = ['mislav', 'stanko', 'mislav', 'ana']
    completion = ['stanko', 'ana', 'mislav']

    def solution_hash(participant, completion):
        dict = {}
        temp = 0
        for participant_name in participant:
            dict[hash(participant_name)] = participant_name
            temp += hash(participant_name)
        for completion_name in completion:
            temp -= hash(completion_name)

        return dict[temp]



    return solution_hash(participant, completion)

# print(not_finished_hash())


def number_list():
    phone_book = ["119", "97674223", "1195524421"]
    def solution(phone_book):
        answer = True
        phone_book.sort()
        for idx in range(len(phone_book)):
            value = phone_book[idx]
            for j in range(idx + 1, len(phone_book)):
                if value in phone_book[j]:
                    answer = False
                    break
            if answer == False:
                break
        return answer

    def solution_hash(phone_book):
        answer = True
        hash_map = {}
        for phone_number in phone_book:
            hash_map[phone_number] = 1

        for phone_number in phone_book:
            temp = ""
            for number in phone_number:
                temp += number
                if temp in hash_map and temp != phone_number:
                    answer = False
        return answer

    return solution(phone_book)

# print(number_list())

def number_list_hash():
    phone_book = ["119", "97674223", "1195524421"]
    def solution_hash(phone_book):
        answer = True
        hash_map = {}
        for phone_number in phone_book:
            hash_map[phone_number] = phone_number

        for phone_number in hash_map:
            temp = ''
            for number in phone_number:
                temp += number
                if temp in hash_map and temp != phone_number:
                    answer = False
                    break
            if answer == False:
                break
        return answer
    return solution_hash(phone_book)

#print(number_list_hash())

def spy():
    clothes = [
        ["yellow_hat", "headgear"],
        ["blue_sunglasses", "eyewear"],
        ["smoky_makeup", "face"],
        ["green_turban", "headgear"],
        ["green_nike", "shoes"],
        ["red_adidas", "shoes"]
    ]
    def solution(clothes):
        answer = 1
        hash_map = {}
        for clothe in clothes:
            if clothe[1] in hash_map:
                hash_map[clothe[1]] += 1
            else:
                hash_map[clothe[1]] = 1

        for key in hash_map:
            answer *= (hash_map[key] + 1)
        answer -= 1
        return  answer

    return solution(clothes)

# print(spy())

def best_album():
    genres = ["classic", "pop", "classic", "classic", "pop",]
    plays = ["500", "500", "500", "500", "500",]
    def solution(genres, plays):
        hash_map = {}
        lists = []
        result = []
        idx = 0

        for genre in genres:
            if not genre in hash_map:
                hash_map[genre] = {'values': [(idx, int(plays[idx]))], "sum": int(plays[idx])}
            else:
                hash_map[genre]['values'].append((idx, int(plays[idx])))
                hash_map[genre]['sum'] += int(plays[idx])
            idx += 1
        print(hash_map)

        for genre in hash_map:
            hash_map[genre]['values'].sort(key= lambda x: x[1])
            lists.append((genre, hash_map[genre]['sum']))
        lists.sort(key = lambda x: (x[1]))

        for genre in hash_map:
            for idx in range(len(hash_map[genre]['values'])):
                for jdx in range(idx, len(hash_map[genre]['values'])):
                    if hash_map[genre]['values'][idx][0] < hash_map[genre]['values'][jdx][0] and hash_map[genre]['values'][idx][1] == hash_map[genre]['values'][jdx][1]:
                        temp = hash_map[genre]['values'][idx]
                        hash_map[genre]['values'][idx] = hash_map[genre]['values'][jdx]
                        hash_map[genre]['values'][jdx] = temp

        while len(lists) > 0:
            genre, count = lists.pop()
            genre_limit = 0

            while len(hash_map[genre]['values']) > 0 and genre_limit < 2:
                index, counts = hash_map[genre]['values'].pop()
                result.append(index)
                genre_limit += 1
        return result

    def solution_good(genres, plays):
        genres_dict = {}
        genres_list = []

        for i in range(len(genres)):
            if not genres[i] in genres_dict:
                genres_dict[genres[i]] = []
            genres_dict[genres[i]].append([i, plays[i]])

        for genre in genres_dict:
            genres_dict[genre].sort(key= lambda x: x[1], reverse=True)
            genres_list.append([genre, sum([int(play) for _, play in genres_dict[genre]])])

        genres_list.sort(key= lambda x: x[1], reverse=True)
        answer = []
        for genre, _ in genres_list:
            answer.extend([x[0] for x in genres_dict[genre][:2]])
        return answer


    return solution_good(genres, plays)


print(best_album())