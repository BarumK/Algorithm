def fib(n):                             # 재귀 호출을 통한 구현
    if n == 0 or n == 1:                # 0 또는 1이면
        return n                        # 0 또는 1을 반환
    else:                               # 아니면
        return fib(n - 1) + fib(n - 2)  # 전 값 + 전전 값 반환