def partition(lst, low, high):
    x = lst[high]                               # 지역 변수 x와 i 선언 후 피벗 값 lst[high] (리스트의 마지막 원소)와 처음 위치 low를 참조시킴
    i = low                                     # i의 역할: for-루프 탈출 후 lst 내 피벗 위치 기억
    for j in range(low, high):                  # 입력 받은 리스트 lst의 마지막 전까지(피벗 이전 위치까지) 순회(반복)
        if lst[j] <= x:                         # lst[j]의 값이 피벗 값보다 작다면
            lst[i], lst[j] = lst[j], lst[i]     # lst[j]와 lst[i]의 위치 교환 후 i의 값 증가
            i += 1                              # i는 lst의 원소 중 피벗보다 값이 작은 원소의 개수만큼 증가함
    lst[i], lst[high] = lst[high], lst[i]       # 순회를 끝마쳤다면(j의 값이 high-1까지 증가시킨 후 탈출했다면), 피벗과 lst[i]의 위치 교환 후
    return i                                    # 피벗 위치(위치를 교환 했으므로 피벗은 인덱스 i 위치에 존재) 반환

def qsort(lst, low, high):
    if low < high:                              # lst 사이즈가 1이 아니라면
        pi = partition(lst, low, high)          # partition 함수를 호출하여 두 개의 서브리스트로 분할(NOTE: partition 함수는 피벗의 인덱스를 반환)
        qsort(lst, low, pi - 1)                 # 왼쪽 서브리스트에 대해 퀵 정렬 수행(qsort 재귀 호출)
        qsort(lst, pi + 1, high)                # 오른쪽 서브리스트에 대해 퀵 정렬 수행(qsort 재귀 호출)

if __name__ == "__main__":
    lst = [10, 80, 30, 90, 40, 50, 70, 60]
    print('정렬 전:\t', end='')
    print(lst)
    qsort(lst, 0, len(lst) - 1)
    print('정렬 후:\t', end='')
    print(lst)