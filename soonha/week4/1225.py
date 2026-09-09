for test_case in range(1, 11):
    T = int(input()) # 테스트 케이스의 번호
    arr = list(map(int, input().split()))
    # 큐 정의
    class CircularQueue:
        def __init__(self, capacity = 10):
            self.capacity = capacity + 1 # 실제 용량은 요청된 용량보다 1 크게 설정(한 칸은 항상 비워둠)
            # front 인덱스는 값을 비워두기 위해서임
            self.items = [None] * self.capacity # 리스트 초기화
            self.front = 0 # 큐의 맨 앞 요소 바로 앞의 인덱스
            self.rear = 0 # 큐의 맨 뒤 요소의 인덱스

        def enqueue(self, item):
            if self.is_full():
                raise IndexError("Queue is Full")
            self.rear = (self.rear + 1) % self.capacity # rear를 다음 위치로 이동(원형으로 순환)
            self.items[self.rear] = item # 새 위치에 항목 삽입

        def dequeue(self):
            if self.is_empty():
                raise IndexError("Queue is Empty")
            self.front = (self.front + 1) % self.capacity # front를 다음 위치로 이동(원형으로 순환)
            item = self.items[self.front] # front 위치의 항목을 가져옴
            self.items[self.front] = None # 해당 위치의 데이터 제거
            return item

        def is_empty(self):
            # front와 rear가 같으면 큐가 비어있음
            return self.front == self.rear

        def is_full(self):
            # rear 다음 위치가 front와 같으면 큐가 가득 참
            return (self.rear + 1) % self.capacity == self.front

        def peek(self):
            if self.is_empty():
                raise IndexError("Queue is Empty")
            # front 다음 위치의 항목 반환(제거하지 않음)
            return self.items[(self.front + 1) % self.capacity]

        def get_size(self):
            # 현재 큐에 있는 항목의 개수 계산
            # rear가 front보다 앞에 있으면 capacity를 더해 음수가 되지 않게 함
            return (self.rear - self.front + self.capacity) % self.capacity

    q = CircularQueue(8)
    for i in range(8):
        q.enqueue(arr[i])

    cycle = 0 # 사이클(첫 번째는 1 감소, 두 번째는 2 감소, ..., 다섯 번째는 5 감소)
    while(True):
        val = q.dequeue()
        val = val - (cycle + 1)
        if(val <= 0):
            val = 0
            q.enqueue(val)
            break
        else:
            q.enqueue(val)
            cycle = (cycle + 1) % 5

    print(f'#{T}', end = ' ')
    for i in range(8):
        num = q.dequeue()
        print(num, end = ' ')
    print()