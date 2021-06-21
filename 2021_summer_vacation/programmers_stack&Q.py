def development():
    def solution(progresses, speeds):
        count = 0
        result = []
        idx = 0

        while progresses[idx] < 100:
            progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
            while progresses[idx] >= 100:
                idx += 1
                count += 1
                if idx == len(progresses):
                    break
                if progresses[idx] < 100:
                    result.append(count)
                    count = 0
            if idx == len(progresses):
                result.append(count)
                break


        return result

    return solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])

# print(development())

def printer():
    def solution(priorities, location):
        count = 0
        priorities_ = [[x, i] for i, x in enumerate(priorities)]

        while priorities_:
            v, i = priorities_.pop(0)

            if any([v < x[0] for x in priorities_]):
                priorities_.append([v, i])
            else:
                count += 1
                if i == location:
                    return count

        return count

    return solution([2,1,3,2], 2)

# print(printer())

def bridge_through_truck():
    def solution(bridge_length, weight, truck_weights):
        result = 0


        while truck_weights:
            result += 1


        return result + 1

    return solution(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1])
# 2(1-6) 2(2-7)
# 2(2-7) 2(6-11)
# 2(6-11) 2(7-12)
# 2(7-12) 1(11-16) 1(12-17) 1(13-18)
# 1(11-16) 1(12-17) 1(13-18) 1(14-19) 1(15-20)

print(bridge_through_truck())