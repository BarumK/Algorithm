def job_scheduling(J):                                  # 겹치다의 기준: 내 종료시작보다 다른 것의 시작시간이 이르다면...
    J.sort(key = lambda x: x[2])                        # 종료 시간이 이른 순으로 선택하므로 종류 시간 이른 순으로 정렬함
    solution_set = []                                   # 해 집합; 빈 리스트로 초기화
    previous_f = 0                                      # 바로 전 선택한 작업의 종료 시간을 담기 위한 변수 선언, 0 초기화
    for i in range(len(J)):                             # 각 작업마다
        if J[i][1] >= previous_f:                       # 시작시간이 종료시간보다 같거나(끝날 때 시작) 크다면(나중에 시작); 즉 안겹친다면
            solution_set.append(J[i])                   # 해 집합에 포함시킴
            previous_f = J[1][2]                        # 종료 시간 갱신
    return solution_set                                 # 해집합 반환
"""
라인 2: O(nlogn) -> 정렬은 빨라봐야 평균 nlogn보다 좋아질 수 없음
라인 5-8: O(n) -> 각 작업을 하나하나 보니까 선형의 시간
따라서 O(nlogn)
"""

if __name__ == "__main__":
    J = [['a', 0, 6], ['b', 1, 4], ['c', 3, 5],         # id, start time, end time
         ['d', 3, 8], ['e', 4, 7], ['f', 5, 9],
         ['g', 6, 10], ['h', 8, 11]]
    print(job_scheduling(J))