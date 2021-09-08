def factorial_iteration(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursion(n):
    """
    T(n): factorial_recursion(n)을 계산하기 위하여 factorial_recursion( ) 함수를 호출하는 횟수
    T(1) = 1;
    T(n) = 1 + T(n-1)
         = 2 + T(n-2)
         = 3 + T(n-3)
         ...
         = (n-2) + T(2)
         = (n-1) + T(1)
    T(1)은 1이므로 T(n) = n

    :param n: 구하고자 하는 팩토리얼 수
    :return: n!의 값
    """
    if n <= 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)

if __name__ == "__main__":
    print(factorial_iteration(5))
    print(factorial_recursion(5))