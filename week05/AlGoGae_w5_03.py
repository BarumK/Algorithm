import math, copy                                                   #  sqrt 함수를 사용하기 위해 math 모듈 import, deepcopy 함수를 사용하기 위해 copy 모듈 import

def dist(p1, p2):                                                   # 두 점 간의 유클리드 거리를 계산하는 함수 정의
    return math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) +            # Note: 본 강의에서 점은 튜플 (x, y)로 나타냄
                     (p1[1] - p2[1]) * (p1[1] - p2[1]))

def compute_closest_pair(P, n):                                     # 전처리 과정 후 최근접쌍 연산 함수 closest_pair()를 호출하고 최종 결과를 반환하는 함수 compute_closest_pair 정의
    P.sort(key = lambda x: x[0])                                    # 입력 받은 점(튜플)들의 집합 P(Note: 본 강의에서는 리스트에 저장)를 x좌표를 기준으로 정렬
    Q = copy.deepcopy(P)                                            # 알고리즘의 성능 향상을 위해 deepcopy함수를 이용하여 추가 리스트 Q 생성 후
    Q.sort(key = lambda x: x[1])                                    # y좌표를 기준으로 정렬
    return closest_pair(P, Q, n)                                    # 최근접쌍 연산 함수 closest_pair() 호출(인자는 x좌표로 정렬한 P, y좌표로 정렬한 Q 및 사이즈 n) 후 최종 결과 반환

def closest_pair(P, Q, n):                                          # 최근접쌍 연산 함수
    if n <= 3:                                                      # 만약 (서브)집합의 사이즈가 3 이하면
        return brute_force(P, n)                                    # 단순한 방법으로 최근접쌍 및 거리를 구하기 위한 brute_force 함수 호출
    d = float('inf')                                                # 왼쪽 서브집합의 최근접쌍 거리와 오른쪽 서브집합의 최근접쌍 거리 중 더 가까운 거리를 저장하기 위한 지역변수 d 선언 및 무한대로 초기화
    cp = ()                                                         # 왼쪽 서브집합의 최근접쌍과 오른쪽 서브집합의 최근접쌍 중 더 가까운 최근접쌍을 저장하기 위한 지역변수 cp 선언 및 empty 튜플로 초기화
    mid = n // 2                                                    # P의 중간 원소의 인덱스 계산
    midpoint = P[mid]                                               # 중간 원소를 저장하기 위한 midpoint 변수 선언 후 중간 원소 할당
    dl, cpl = closest_pair(P[:mid], Q, mid)                         # P의 앞 부분(왼쪽 부분)에 대해서 closest_pair() 함수 호출(재귀 호출)하여 반환 값을 dl과 cpl에 할당
    dr, cpr = closest_pair(P[mid:], Q, n - mid)                     # P의 뒷 부분(오른쪽 부분)에 대해서 closest_pair() 함수 호출(채귀 호출)하여 반환 값을 dr과 cpr에 할당
    if dl <= dr:                                                    # 왼쪽 서브집합의 최근접쌍 cpl의 거리 dl이 오른쪽 서브집합의 최근접쌍 cpr의 거리 dr보다 멀지 않다면
        d = dl                                                      # d와 cp에 각각 dleft와 cpleft 할당
        cp = cpl
    else:                                                           # cpleft의 거리 dleft가 cpright의 거리 dright보다 멀다면
        d = dr                                                      # d와 cp에 각각 dright와 cpright 할당
        cp = cpr
    strip = []                                                      # 띠(strip) 내부에 존재하는 점들을 저장하기 위한 빈 리스트 생성 후 strip 변수에 할당
    for i in range(n):                                              # x 좌표가 midpoint[0] – d와 midpoint[0] + d 사이인 점들을 리스트에 추가
        if midpoint[0] - d <= Q[i][0] <= midpoint[0] + d:
            strip.append(Q[i])
    dmid, cpmid = strip_closest_pair(strip, len(strip), d, cp)      # 하나의 점은 왼쪽 서브집합에 속하고, 다른 점은 오른쪽 서브집합에 속하는 쌍들 중 그 거리가 최소가 되는 쌍 cpmid와
                                                                    # 거리 dmid를 구하기 위해 함수 strip_closest_pair() 호출 (인자는 리스트 strip, strip의 사이즈, d와 cp) 후
                                                                    # 반환 값을 변수 cpmid와 dmid에 각각 할당
    if d <= dmid:                                                   # 만약 d의 값이 dmid의 값과 같거나 작다면(멀지 않다면)
        return d, cp                                                # d와 cp를 결과로 반환
    else:                                                           # 만약 d의 값이 dmid의 값보다 크다면(멀다면)
        return dmid, cpmid                                          # dmid와 cpmid를 결과로 반환

def brute_force(P, n):                                              # 단순한 방법으로 최근접쌍과 거리를 계산 후 반환
    min_val = float('inf')
    cp = ()
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < min_val:
                min_val = dist(P[i], P[j])
                cp = (P[i], P[j])
    return min_val, cp

def strip_closest_pair(strip, size, d, cp):
    dmid = d                                                        # dmid와 cpmid 선언 후 인자로 받은 d와 cp로 각각 초기화
    cpmid = cp
    for i in range(size):                                           # y좌표로 정렬되어 있는 점들의 리스트 strip에서 마지막 점을 제외한 각 점 a마다 d보다 더 가까운 쌍들을 찾고
                                                                    # 이들 중 가장 가까운 쌍을 선택하기 위한 for-루프 (i는 마지막 점을 제외한 각 점의 인덱스를 위해 사용)
        j = i + 1                                                   # 각 점 a의 위에 존재하는 점들의 인덱스를 위해 지역변수 j 선언 후 해당 점 바로 위의 점의 인덱스로 초기화
        while j < size and (strip[j][1] - strip[i][1]) < dmid:      # 점 a에 대해 위에 존재하는 점 b와 y좌표 간 거리가 dmid보다 가깝다면 (1) 두 점a, b 사이의 2차원 유클리드 거리를 계산하고
            if dist(strip[i], strip[j]) <= dmid:                    # (2) 계산한 값이 현재 dmid 값과 같거나 작다면(거리가 같거나 가깝다면)
                dmid = dist(strip[i], strip[j])                     # dmid와 cpmid를 각각 계산한 값과 두 점 (a, b)로 갱신
                cpmid = (strip[i], strip[j])                        #  이와 같은 과정을 y좌표 간 거리 값이 dmid와 같거나 커질 때까지 반복(while-루프)
            j += 1
    return dmid, cpmid                                              # 구한 strip 내 최근접쌍과 거리인 cpmid와 dmid 반환

if __name__ == "__main__":
    P = [(1, 1), (2, 2), (1, 3), (3, 6), (9, 15), (8, 12), (4, 7),
         (9, 7), (4, 4), (5, 4), (3, 3), (6, 7), (8, 9), (9, 2)]
    n = len(P)
    result = compute_closest_pair(P, n)
    print("The smallest distance and closest pair:", result)

    P = [(1, 11), (3, 7), (5, 3), (7, 7), (9, 6), (13, 7), (15, 11), (16, 4)]
    n = len(P)
    result = compute_closest_pair(P, n)
    print("The smallest distance and closest pair:", result)