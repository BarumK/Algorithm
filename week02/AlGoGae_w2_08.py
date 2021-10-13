def linear_search(lst, n, x):
    for i in range(n):
        if lst[i] == x:         # 비교 연산
            return i
    return i

"""
최악의 경우: 단위 연산을 n번 돌았을 때; x가 리스트 마지막에 있거나 리스트에 존재하지 않을 때 -> W(n) = n
최선의 경우: 단위 연산을 1번 돌았을 때; x가 리스트 처음에 있을 때 -> B(n) = 1
"""
