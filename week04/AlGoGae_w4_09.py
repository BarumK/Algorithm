def partition(lst, low, high):
    x = lst[high]                               # 지역 변수 x와 i 선언 후 피벗 값 lst[high] (리스트의 마지막 원소)와 처음 위치 low를 참조시킴
    i = low                                     # i의 역할: for-루프 탈출 후 lst 내 피벗 위치 기억
    for j in range(low, high):                  # 입력 받은 리스트 lst의 마지막 전까지(피벗 이전 위치까지) 순회(반복)
        if lst[j] <= x:                         # lst[j]의 값이 피벗 값보다 작다면
            lst[i], lst[j] = lst[j], lst[i]     # lst[j]와 lst[i]의 위치 교환 후 i의 값 증가
            i += 1                              # i는 lst의 원소 중 피벗보다 값이 작은 원소의 개수만큼 증가함
    lst[i], lst[high] = lst[high], lst[i]       # 순회를 끝마쳤다면(j의 값이 high-1까지 증가시킨 후 탈출했다면), 피벗과 lst[i]의 위치 교환 후
    return i                                    # 피벗 위치(위치를 교환 했으므로 피벗은 인덱스 i 위치에 존재) 반환

def qselect(lst, low, high, k):
    pi = partition(lst, low, high)              # partition 함수를 호출하여 두 개의 서브리스트로 분할(NOTE: partition 함수는 피벗의 인덱스를 반환하여 pi에 할당)
    if pi == k - 1:                             # pi와 k-1 값과 같다면(Python 리스트의 인덱스는 0부터 시작하므로 k-1)
        return lst[pi]                          # 검색 성공 및 결과 반환
    elif pi < k - 1:                            # pi가 k-1 값보다 작다면
        return qselect(lst, pi + 1, high, k)    # 오른쪽 서브리스트에 대해 퀵 선택 수행
    else:                                       # pi가 k-1 값보다 크다면
        return qselect(lst, low, pi - 1, k)     # 왼쪽 서브리스트에 대해 퀵 선택 수행

if __name__ == "__main__":
    lst = [4, 8, 12, 16, 20, 24, 26, 22, 18, 14, 10, 6, 2]
    print(qselect(lst, 0, len(lst) - 1, 3))