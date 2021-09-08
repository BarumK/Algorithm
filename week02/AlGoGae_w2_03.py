def binary_search(lst, n, x):                       # 이진 검색 역시 최악의 경우는 리스트에 존재하지 않을 때.
                                                    # 이 경우 탐색 횟수는 입력 사이즈가 n일 때 log2(n) + 1
                                                    # n을 넣은 이유는 문제와 일관성을 맞추기 위해, 분석 시에 사이즈를 강조하기 위해
    mid = 0                                         # 이 함수는 반복문을 이용하여 구현했음, 재귀를 이용한 구현도 가능하다!
    low = 0                                         # 초기 설정: 시작점 위치
    high = n - 1                                    # 초기 설정: 끝점 위치
    while low <= high:                              # 탈출 조건 만족 전까지 반복: low가 high보다 크거가 같기 전까지
        mid = (low + high) // 2                     # 중간 위치 설정: 시작과 끝 더한 후 2로 나눔
                                                    # 중간 위치의 값과 찾고자 하는 값을 계속 비교함
        if x == lst[mid]:                           # 찾고자 하는 값이 존재할 경우
            return mid                              # 리턴하고 종료
        if x < lst[mid]:                            # 찾고자 하는 값이 더 작다면 더 큰 값들을 확인할 필요가 없음, 따라서 오른쪽 배제
            high = mid - 1                          # high를 재설정: mid 바로 직전 값의 인덱스로
        else:                                       # 찾고자 하는 값이 더 크다면 더 작은 값들을 확인할 필요가 없음, 따라서 왼쪽 배제
            low = mid + 1                           # low를 재설정: mid 바로 다음 값의 인덱스로
    return -1                                       # 없을 경우 -1 리턴
                                                    # 매 반복문을 돌 때마다 search space가 절반씩 줄어듦.

if __name__ == "__main__":
    lst = [3, 5, 7, 8, 10, 11, 13, 16]
    n = len(lst)
    result = binary_search(lst, n, 30)              # 최악의 경우로 설정해 둔 상태; 리스트 내에 존재하지 않음
    if result != -1:
        print("Found at index {}".format(result))
    else:
        print("Not found.")