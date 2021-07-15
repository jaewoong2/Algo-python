# 2021 카카오톡 인턴 연계 https://programmers.co.kr/learn/courses/30/lessons/81302
from typing import List

def keep_distance(places: List[List[str]]):
    def find_people(position, placeIndex):
        row, col = position
        flag = False

        if flag == False and col - 1 >= 0 and row - 1 >= 0:
            if places[placeIndex][row - 1][col - 1] == 'P':
                if places[placeIndex][row - 1][col] != 'X' or  places[placeIndex][row][col - 1] != 'X':
                    flag = True

        if flag == False and col + 1 <= 4 and row + 1 <= 4:
            if places[placeIndex][row + 1][col + 1] == 'P':
                if places[placeIndex][row + 1][col] != 'X' or  places[placeIndex][row][col + 1] != 'X':
                    flag = True

        if flag == False and col + 1 <= 4 and row - 1 >= 0:
            if places[placeIndex][row - 1][col + 1] == 'P':
                if places[placeIndex][row - 1][col] != 'X' or  places[placeIndex][row][col + 1] != 'X':
                    flag = True

        if flag == False and col + 1 <= 4 and row - 1 >= 0:
            if places[placeIndex][row - 1][col + 1] == 'P':
                if places[placeIndex][row - 1][col] != 'X' or  places[placeIndex][row][col + 1] != 'X':
                    flag = True

        if flag == False and col - 1 >= 0:
            if places[placeIndex][row][col - 1] == 'P':
                flag = True

        if flag == False and col + 1 <= 4:
            if places[placeIndex][row][col + 1] == 'P':
                flag = True

        if flag == False and row - 1 >= 0:
            if places[placeIndex][row - 1][col] == 'P':
                flag = True

        if flag == False and row + 1 <= 4:
            if places[placeIndex][row + 1][col] == 'P':
                flag = True

        if flag == False and col - 2 >= 0:
            if places[placeIndex][row][col - 2] == 'P':
                if places[placeIndex][row][col - 1] != 'X':
                    flag = True

        if flag == False and col + 2 <= 4:
            if places[placeIndex][row][col + 2] == 'P':
                if places[placeIndex][row][col + 1] != 'X':
                    flag = True

        if flag == False and row - 2 >= 0:
            if places[placeIndex][row - 2][col] == 'P':
                if places[placeIndex][row - 1][col] != 'X':
                    flag = True

        if flag == False and row + 2 <= 4:
            if places[placeIndex][row + 2][col] == 'P':
                if places[placeIndex][row + 1][col] != 'X':
                    flag = True

        return flag

    result = []

    for i, place in enumerate(places):
        flag = False

        for row in range(5):
            for col in range(5):
                if place[row][col] == 'P' and flag == False:
                    flag = find_people([row, col], i)
                    if flag == True:
                        result.append(0)

        if flag == False:
            result.append(1)

    return result
# print(keep_distance([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
#                      ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
#                      ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
#                      ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
#                      ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))


def keep_distance_re(places: List[List[str]]):
    dy_no_partition = [0, 1, 0, -1]
    dx_no_partition = [1, 0, -1, 0]

    dy_one_partition = [0, 2, 0, -2]
    dx_one_partition = [2, 0, -2, 0]

    dy_two_partition = [1, -1, 1, -1]
    dx_two_partition = [1, -1, -1, 1]

    result = []

    for place in places:
        place_index = {'X': [], 'P': [], 'O': []}
        flag = False

        for row in range(5):
            for col in range(5):
                place_index[place[row][col]].append([row, col])

        for i in range(len(place_index['P'])):
            if flag == True:
                break
            p_row, p_col = place_index['P'][i]

            for j in range(4):
                if [p_row + dy_no_partition[j], p_col + dx_no_partition[j]] in place_index['P'] and flag == False:
                    flag = True

            for j in range(4):
                if [p_row + dy_one_partition[j], p_col + dx_one_partition[j]] in place_index['P'] and flag == False:
                    if [p_row + dy_no_partition[j], p_col + dx_no_partition[j]] not in place_index['X']:
                        flag = True

            for j in range(4):
                if [p_row + dy_two_partition[j], p_col + dx_two_partition[j]] in place_index['P'] and flag == False:
                    if [p_row + dy_two_partition[j], p_col] not in place_index['X'] or [p_row, p_col + dx_two_partition[j]] not in place_index['X']:
                        flag = True

        if flag == True:
            result.append(0)
        else:
            result.append(1)

    return result
#
# print(keep_distance_re([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
#                      ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
#                      ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
#                      ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
#                      ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

def rotate_matrix(row, col, queries):
    # 행렬 생성
    result = []
    matrix = []
    value = 1
    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(value)
            value += 1
        matrix.append(temp)

    # 행렬 돌리기
    for query in queries:
        top, bottom, left, right = query[0] - 1, query[2] - 1, query[1] -1, query[3] -1
        matrix_copy = [[x for x in row] for row in matrix]
        minimum = row * col
        for row_ in range(top, bottom + 1):
            for col_ in range(left, right + 1):
                minimum = min(minimum, matrix[row_][col_])

                if row_ == top or row_ == bottom \
                    or col_ == left or col_ == right:
                    if row_ == top and col_ != left:
                        matrix_copy[row_][col_] = matrix[row_][col_ - 1]

                    elif row_ == bottom and col_ != right:
                        matrix_copy[row_][col_] = matrix[row_][col_ + 1]

                    elif col_ == left and row_ != bottom:
                        matrix_copy[row_][col_] = matrix[row_ + 1][col_]

                    elif col_ == right and row_ != top:
                        matrix_copy[row_][col_] = matrix[row_ - 1][col_]

        result.append(minimum)
        matrix = matrix_copy


    # return result


print(rotate_matrix(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))


