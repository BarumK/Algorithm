def sum(lst, n):
    result = 0
    for i in range(n):
        result = result + lst[i]        # 더하기가 n번 반복됨
    return result

if __name__ == "__main__":
    lst = [10, 7, 11, 5, 13, 8]         # 리스트 내의 값이 어떻든 간에 영향을 받지 않음, 모든 경우의 분석에선 입력의 크기만 중요하다
    n = len(lst)
    print(sum(lst, n))