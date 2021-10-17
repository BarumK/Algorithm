# 거스름돈 계산하기 문제
def coin_change(x):
    d = [1, 5, 10, 50, 100, 500]
    result = []
    i = len(d) - 1                          # i는 가장 큰 것부터
    while True:                             # do while을 이용하면 편함
        while x >= d[i]:                    # 거스름돈보다 선택한 값이 작으면
            x -= d[i]                       # 가격만큼 빼고
            result.append(d[i])             # 해집합에 포함
        i -= 1                              # 그 다음 큰 동전으로 이동
        if i < 0:                           # 0보다 작으면 -> 종료 조건
            break
    for i in range(len(result)):            # 해집합 내의 결과 출력
        print(result[i], end = " ")

if __name__ == "__main__":
    x = 16
    coin_change(x)