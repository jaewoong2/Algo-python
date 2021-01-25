# 주식가격

def stock_price():
    def solution(prices):
        answer = []
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] < prices[i]:
                    answer.append(j - i)
                    break
            if len(answer) - 1 != i:
                answer.append(len(prices) - 1 - i)
        return answer

    def solution_stack(prices):
        from collections import deque
        answer = []
        prices = deque(prices)
        while prices:
            # prices 에서의 맨 왼쪽 값을 가져온다.
            c = prices.popleft()

            count = 0
            # prices 에서의 맨 왼쪽 값(c) 과 그 다음 값들 을 비교한다.
            for i in prices:
                # 만약, 맨 왼쪽 값(현재 값)이 가 다음 값들 과 비교시 크게 된다면,
                # count 1을 하고, 반복문을 종료한다(for 문 종료)
                if c > i:
                    count += 1
                    break
                # 비교 인덱스를 한개 씩 넘길 때 마다 count 를 1씩 샌다
                count += 1

            answer.append(count)

    return solution(prices=[1,2,3,2,3])

print(stock_price())

# 기능개발

def developing():
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    # return = [2, 1]
    def solution(progresses, speeds):
        answer = []
        counts = [0] * len(progresses)
        for i in range(len(progresses)):
            while progresses[i] < 100:
                progresses[i] += speeds[i]
                counts[i] = counts[i] + 1
        i = 0
        while i < len(counts):
            count = 1
            for idx in range(i + 1, len(counts)):
                if counts[idx] <= counts[i]:
                    count += 1
                else:
                    break
            i += count
            answer.append(count)

        return answer

    def solution_simple(progresses, speeds):
        answer = []
        time = 0
        count = 0

        # time 을 1씩 증가시킨다.
        # 맨 왼쪽기능 (먼저 구현이 되어야 되는 기능) 이 구현이 됐을 때,
        # 자동으로 다음 기능들도 검사를하며 구현이 되어있으면 각각 count 가 1씩 증가 된다.
        # 다음 기능이 구현이 되지 않았다면, answer 에 count 가 들어오고 count 는 0 이된다.
        # 그리고 그 기능이 구현될 때 까지 time 을 증가 시킨다.
        # time 을 counts 배열로 넣은 것과 달리 1씩 증가 시켜 비교하는 방법을 사용한 이 방법이 더 깔끔한 것 같다.
        while len(progresses) > 0:
            if progresses[0] + time * speeds[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            else:
                if count > 0:
                    answer.append(count)
                    count = 0
                time += 1
        answer.append(count)
        return answer
    return solution(progresses, speeds)

print(developing())

def truck_cross_the_bridge():
    def solution(bridge_length, weight, truck_weights):
        answer = 1
        cross_trucks = []
        while len(truck_weights) > 0 or len(cross_trucks) > 0:
            while len(truck_weights) > 0 and sum([x[0] for x in cross_trucks]) + truck_weights[0] <= weight:
                for idx in range(len(cross_trucks)):
                    cross_trucks[idx] = (cross_trucks[idx][0], cross_trucks[idx][1] + 1)
                truck_next = truck_weights.pop(0)
                cross_trucks.append((truck_next, 1))

                for idx in range(len(cross_trucks)):
                    if cross_trucks[0][1] == bridge_length:
                        answer += 1
                        cross_trucks.pop(0)

            for idx in range(len(cross_trucks)):
                cross_trucks[idx] = (cross_trucks[idx][0], cross_trucks[idx][1] + 1)
            answer += 1

            for idx in range(len(cross_trucks)):
                if cross_trucks[0][1] == bridge_length :
                    answer += 1
                    cross_trucks.pop(0)

        return answer

    def solution_class(bridge_length, weight, truck_weights):
        from collections import deque
        DUMMY_TRUCK = 0

        class Bridge(object):

            def __init__(self, length, weight):
                self._max_length = length
                self._max_weight = weight
                self._queue = deque()
                self._current_weight = 0

            def push(self, truck):
                next_weight = self._current_weight + truck
                if next_weight <= self._max_weight and len(self._queue) < self._max_length:
                    self._queue.append(truck)
                    self._current_weight = next_weight
                    return True
                else:
                    return False

            def pop(self):
                item = self._queue.popleft()
                self._current_weight -= item
                return item

            def __len__(self):
                return len(self._queue)

            def __repr__(self):
                return 'Bridge({}/{} : {})'.format(self._current_weight, self._max_weight, list(self._queue))

        def solution(bridge_length, weight, truck_weights):
            bridge = Bridge(bridge_length, weight)
            trucks = deque(w for w in truck_weights)

            for _ in range(bridge_length):
                bridge.push(DUMMY_TRUCK)

            count = 0
            while trucks:
                bridge.pop()

                if bridge.push(trucks[0]):
                    trucks.popleft()
                else:
                    bridge.push(DUMMY_TRUCK)
                count += 1

                print(bridge)

            while bridge:
                bridge.pop()
                count += 1

            return count

        return solution(bridge_length, weight, truck_weights)

    return solution_class(5, 5, [2, 2, 2, 2, 1, 1, 1, 1, 1]) # 19

print(truck_cross_the_bridge())
