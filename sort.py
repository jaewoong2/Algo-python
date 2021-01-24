# 선택 정렬 O(N^2)
def sort_by_choice(array: list):
    for i in range(len(array)):
        min_index = i # 정렬이 시작되면 맨앞에 있는 것이 가장 작은 수라고 설정
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i] #스와프

    print(array)

sort_by_choice([7, 5, 9, 0, 3, 1, 6, 2, 4, 8])

# 삽입 정렬
def insert_sort(array: list):
    for i in range(1, len(array)):
        for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
                break
    print(array)

insert_sort([7, 5, 9, 0, 3, 1, 6, 2, 4, 8])

# 퀵 정렬
def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1

        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort([7, 5, 9, 0, 3, 1, 6, 2, 4, 8], 0, 8)


def quick_sort_2(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort_2(left_side) + [pivot] + quick_sort_2(right_side)

print(quick_sort_2([7, 5, 9, 0, 3, 1, 6, 2, 4, 8]))


# 계수 정렬
# 배열을 2개 사용
def coefficient_sort(array):
    # array 에 있는 것의 크기보다 1큰 (0~9) 까지 되도록 배열을 하나더 만들어줌
    # 이 배열의 인덱스는 array 에 있는 각각의 수의 값을 의미한다.
    # 이 배열의 인덱스의 있는 값은 해당하는 인덱스가 array 배열에 들어있는 회수이다.
    count = [0] * (max(array) + 1)

    # array 에 있는 값을
    for i in range(len(array)):
        count[array[i]] += 1
    for i in range(len(count)):
        # 0 ~ 9 인덱스
        for j in range(count[i]):
            # 횟수
            print(i, end=' ')

coefficient_sort([7,5,9,0,3,1,6,2,9,1,4,8,0,5,2])

def swap_two_array(k, a_array, b_array):
    def array_sort(array):
        if len(array) <= 1:
            return array
        pivot = array[0]
        tail = array[1:]

        left_side = [x for x in tail if x <= pivot]
        right_side = [x for x in tail if x > pivot]

        return array_sort(left_side) + [pivot] + array_sort(right_side)

    sorted_a_array = array_sort(a_array)
    sorted_b_array = array_sort(b_array)

    for i in range(k):
        temp = sorted_a_array[i]
        sorted_a_array[i] = sorted_b_array[len(b_array) - 1 - i]
        sorted_b_array[len(b_array) - 1 - i] = temp

    result = 0
    for i in sorted_a_array:
        result += i
    return result

print(swap_two_array(3, [1,2,5,4,3], [5,5,6,6,5]))


def swap_two_array_2(a, b, k):
    a.sort()
    b.sort(reverse= True)

    for i in range(k):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break
    print(sum(a))

swap_two_array_2([1,2,5,4,3], [5,5,6,6,5], 3)


def getTarget(array):
    target = int(input())

    result = binary_search(array, target, 0, len(array) - 1)
    if result == None:
        print("원소가 존재 하지 않습니다")
    else:
        print(result + 1)


# 이진 탐색- 재귀
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

# getTarget([1,3,5,6,9,11,13,15,17,19])

# 이진 탐색은 정렬되어 있다고 가정하에 사용.
def binary_search_while(array, target):
    start = 0
    end = max(array)
    mid = (start + end) // 2

    while array[mid] != target:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
    return mid

def getTarget(array):
    target = int(input())

    result = binary_search_while(array, target)
    if result == None:
        print("원소가 존재 하지 않습니다")
    else:
        print(result + 1)

# getTarget([1,3,5,6,8,11,13,15,17,19])

# 파라메트릭 서치
# 최적화 문제
# 조건을 만족할 수 있는가를 확인해야함
def make_lice_cake(heights, m):
    def binary_search_for_cake(array_heights, target, start, end):
        if start > end:
            return None
        sum = 0
        mid = (end + start) // 2

        for height in array_heights:
            if height >= mid:
                sum += height - mid

        # mid 가 작다
        if sum > target:
            return binary_search_for_cake(array_heights, target, mid + 1, end)
        # mid 가 크다
        elif sum < target:
            return binary_search_for_cake(array_heights, target, start, mid - 1)
        else:
            return mid

    print(binary_search_for_cake(heights, m, 0, max(heights)))

make_lice_cake([19, 14, 10, 17], 3)


def make_lice_cake_2(array, m):
    start = 0
    end = max(array)

    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for x in array:
            if x > mid:
                total += x - mid

        if total < m:
            end = mid - 1
        else:
           result = mid
           start = mid + 1
    print(result)

make_lice_cake_2([19, 14, 10, 17], 3)

def count_target(array, target):
    left = 0
    right = len(array) - 1

    while array[left] != target or array[right] != target:
        if left > right:
            break

        if array[left] < target:
            left += 1

        if array[right] > target:
            right -= 1

    print(right - left + 1, '개')

count_target([1, 1, 2, 2, 2, 2, 3], 2)
