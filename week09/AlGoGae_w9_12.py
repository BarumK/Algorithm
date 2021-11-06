def fib_dp(n):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 0; cache[1] = 1
    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[n]

if __name__ == "__main__":
    print(fib_dp(5))