def find_min_alphabet_movement(target):
    alphabet = {x.upper(): i for i, x in enumerate("abcdefghijklmnopqrstuvwxyz")}

    return min(alphabet[target] - alphabet['A'], alphabet['Z'] - alphabet[target] + 1)


def find_not_A_position(name, completed):
    indexes = []

    for i in range(len(name)):
        if name[i] != 'A' and i not in completed:
            indexes.append((i, min(abs(i - completed[-1]), abs(len(name) - (i + 1) + completed[-1] + 1))))

    if indexes:
        return min(indexes, key= lambda x: (x[1], (x[0] - completed[-1])))
    else:
        return (completed[-1], 0)

def solution(name):
    if name == 'A' * len(name):
        return 0
    completed = []
    total = 0
    now = 0

    while len(completed) < len([x for x in name if x != 'A']):
        if name[0] == 'A' and 0 in completed:
            completed.pop(0)
        up_or_down = find_min_alphabet_movement(name[now])
        total += up_or_down
        completed.append(now)
        idx, left_or_right = find_not_A_position(name, completed)
        now = idx
        total += left_or_right

    return total

print(solution("AAAABBB"))