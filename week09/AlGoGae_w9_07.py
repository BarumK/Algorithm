cache = {}                                                  # 기록(memo)을 위한 사전(dictionary) cache 선언(키는 n, 값은 피보나치 수) -> 리스트로 선언해도 됨
def fib_memorized(n):
    if n in cache:                                          # 만약 fib_memoized(n)을 이미 호출하여 기록하였다면
        return cache[n]                                     # 해당 기록 값을 반환
    if n == 0 or n == 1:                                    # 만약 n이 0 또는 1이라면
        result = n                                          # 변수 result에 n의 값(0 또는 1)을 할당 후
        cache[n] = result                                   # n과 result 쌍을 cache에 기록 후
        return  cache[n]                                    # result 반환
    result = fib_memorized(n - 1) + fib_memorized(n - 2)    # 라인 3과 라인 5의 조건에 해당하지 않으면 fib_memoized(n-1)의 반환 값과 fib_memoized(m-2)의 반환 값의 합을 result에 할당 후
    cache[n] = result                                       # n과 result 쌍을 cache에 기록 후
    return result                                           # result 반환

if __name__ == "__main__":
    print(fib_memorized(7))