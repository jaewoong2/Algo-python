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



print(keep_distance([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                     ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                     ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                     ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                     ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))