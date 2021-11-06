class BinaryHeap:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def enheap(self, item):
        self.items.append(item)
        self.upheap(self.size() - 1)

    def deheap(self):
        if self.size() == 0:
            return None
        minimum = self.items[0]
        self.swap(0, -1)
        del self.items[-1]
        self.downheap(0)
        return minimum

    def downheap(self, i):
        while ((2 * i + 1) <= (self.size() - 1)):
            k = 2 * i + 1
            if (k < (self.size() - 1)) and (self.items[k] > self.items[k + 1]):
                k += 1
            if self.items[i] < self.items[k]:
                break
            self.swap(i, k)
            i = k

    def upheap(self, i):
        while (i > 0) and (self.items[(i - 1) // 2] > self.items[i]):
            self.swap(i, (i - 1) // 2)
            i = (i - 1) // 2

def classroom_assignment(C):
    C.sort(key = lambda x: x[0])                        # 강의를 시작 시간 기준으로 오름차순 정렬
    depth = 0                                           # 강의실의 번호를 저장하기 위한 depth 변수 선언 및 0으로 초기화(강의실 번호는 0부터 시작)
    solution_set = BinaryHeap()                         # 해 집합(강의실 및 강의)을 위한 변수 solution_set 선언 후 최소 힙(우선순위 큐) 생성 및 할당
    for c in C:                                         # 모든 강의를 고려할 수 있도록 각 강의 c에 대해 반복(해답 점검)
        if solution_set.size() == 0:                    # 만약 강의실이 하나도 존재하지 않는다면
            room = [c[1], depth, [c]]                   # 새로운 강의실 생성 후
            solution_set.enheap(room)                   # solution_set에 enheap
                                                        # NOTE: 강의실 room은 room에 포함된 강의 중 (1) 가장 이른 종료 시간을 가지는 강의의 종료시간, (2) 강의실 번호, (3) 포함된 강의들의 리스트를 유지
        else:                                           # 만약 강의실이 하나 이상 존재한다면
            current_room = solution_set.deheap()        # 현재 존재하는 강의실들 중 강의 종료 시간이 가장 이른 종료 시간을 가지는 강의실 current_room을 선택
            if c[0] >= current_room[0]:                 # c의 시작 시간이 current_room의 종료 시간보다 늦다면
                current_room[2].append(c)               # current_room의 강의 리스트에 포함시키고,
                current_room[0] = c[1]
                solution_set.enheap(current_room)       # 다시 solution_set에 enheap
            else:                                       # c의 시작 시간이 current_room의 종료 시간보다 이르다면
                depth += 1                              # 새로운 강의실을 생성(강의실 번호는 depth + 1),
                room = [c[1], depth, [c]]               # 강의 리스트에 c를 포함시키고,
                solution_set.enheap(room)
                solution_set.enheap(current_room)       # 해당 강의를 solution_set에 enheap
    return solution_set                                 # solution_set을 최종 해로 반환

if __name__ == "__main__":
    C = [[900, 1030, 'a'], [900, 1230, 'b'], [900, 1030, 'c'], [1100, 1230, 'd'], [1100, 1400, 'e'], [1300, 1430, 'f'],
         [1300, 1430, 'g'], [1400, 1630, 'h'], [1500, 1630, 'i'], [1500, 1630, 'j']]
    result = classroom_assignment(C)
    for i in range(result.size()):
        i = result.deheap()
        print(i[1], i[2])