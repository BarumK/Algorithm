def linear_search(lst, n, x):                       # 선형 검색은 입력 사이즈가 n일 때 평균적으로 n / 2번 탐색함.
                                                    # n을 넣은 이유는 문제와 일관성을 맞추기 위해, 분석 시에 사이즈를 강조하기 위해
    for i in range(n):                              # 최선의 경우 탐색 1회
        if lst[i] == x:                             # 최악의 경우 입력값 n일 때 n회 탐색
            return i
    return -1

if __name__ == "__main__":
    lst = [10, 7, 11, 5, 3, 8, 16, 13]              # 가장 운 좋을 때: 맨 처음 (10)
                                                    # 가장 운이 나쁠 때: 맨 마지막(13), 더 나쁠 때는 아예 없을 때
    n = len(lst)
    result = linear_search(lst, n, 30)
    if result != -1:
        print("Found at index {}".format(result))
    else:
        print("Not found.")