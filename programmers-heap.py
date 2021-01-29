def more_hot():
    scoville = [1, 2, 3, 9, 10, 12]
    k = 7
    def solution(scoville, k):
        import heapq
        answer = 0
        heapq.heapify(scoville)
        while len(scoville) > 1:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            if a >= k:
                return answer
            scoville_sum = a + (2 * b)
            answer += 1
            heapq.heappush(scoville, scoville_sum)

        if sum(scoville) < k:
            answer = -1


    return solution(scoville, k)

# print(more_hot())

def disk_controller():
    jobs = [[0, 3], [1, 9], [2, 6]]	 #9
    def solution(jobs):
        time = 0
        passed_times = []
        while jobs:
            request_jobs = []

            for i, job in enumerate(jobs):
                if time >= job[0]:
                    request_jobs.append((i, job[1]))

            if len(request_jobs) == 0:
                min_job = min(jobs, key=lambda x: (x[0], x[1]))
                request_jobs.append((jobs.index(min_job), min_job[1]))
                time = min_job[0]

            min_job = min(request_jobs, key=lambda x:(x[1]))
            time += min_job[1]
            passed_times.append(time - jobs[min_job[0]][0])
            jobs.remove(jobs[min_job[0]])

        return int(sum(passed_times) // len(passed_times))

    #return solution(jobs)

# print(disk_controller())

def double_queue():
    def solution(operations):
        import heapq
        queue = []
        heapq.heapify(queue)
        commands = [x.split(' ') for x in operations]

        for command in commands:
            if command[0] == 'I':
                heapq.heappush(queue, int(command[1]))
            elif command[0] == 'D':
                if int(command[1]) > 0:
                    queue.pop()
                if int(command[1]) < 0:
                    heapq.heappop(queue)

        if len(queue) == 0:
            return [0, 0]

        return [max(queue), min(queue)]

    return solution(["I 16","D 1"])

print(double_queue())



def heapsort(iterable):
    import heapq
    heap = []
    for value in iterable:
        heapq.heappush(heap, value)
    return [heapq.heappop(heap) for _ in range(len(heap))]

print(heapsort([5, 2, 3, 4, 1]))