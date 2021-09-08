def fib(n):                                     # 반복을 통한 구현
    memo = [0 for _ in range(n + 1)]            # 0부터 입력값 n까지, 총 n개의 값을 담을 수 있는 리스트를 만들어야 함. (중요!)
                                                # 이거 관련해서 나중에 동적 프로그래밍에서 더 배울 예정 - memoization 방법
    memo[0], memo[1] = 0, 1                     # 0항과 1항을 각각 0과 1로 저장
    for i in range(2, n + 1):                   # 2번째 항부터 쭉 반복 돌림 - 끝까지
        memo[i] = memo[i - 1] + memo[i - 2]     # 지난 항과 지지난 항을 더해서 값을 저장
    return memo[n]                              # 마지막 항을 반환

if __name__ == "__main__":
    print(fib(5))