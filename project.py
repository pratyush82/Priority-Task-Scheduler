#Min-Heap
class BinaryMinHeap:

    def __init__(self, heap=None):
        if heap is None:
            heap = []
        self.heap = heap
        self.len = len(heap)
        if heap is not None:
            self.buildHeap()


    @staticmethod
    def left(i):
        return i*2 + 1

    @staticmethod
    def right(i):
        return i*2 + 2

    @staticmethod
    def parent(i):
        if i == 0:
            return -1
        return (i-1) // 2

    def insert(self, k):
        self.heap.append(k)
        i = self.len
        self.len += 1
        while i > 0:
            p = BinaryMinHeap.parent(i)
            if self.heap[i].arrival < self.heap[p].arrival:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p
            else:
                break

    def heapify(self, i):
        left = BinaryMinHeap.left(i)
        right = BinaryMinHeap.right(i)
        if left < self.len and self.heap[i].arrival >= self.heap[left].arrival:
            if right < self.len and self.heap[left].arrival <= self.heap[right].arrival:
                self.heap[i], self.heap[left] = self.heap[left], self.heap[i]
                i = left
            elif right < self.len:
                self.heap[i], self.heap[right] = self.heap[right], self.heap[i]
                i = right
            else:
                self.heap[i], self.heap[left] = self.heap[left], self.heap[i]
                i = left
            self.heapify(i)
        elif right < self.len and self.heap[i].arrival >= self.heap[right].arrival:
            self.heap[i], self.heap[right] = self.heap[right], self.heap[i]
            i = right
            self.heapify(i)

    def minimum(self):
        if self.len == 0:
            return None
        return self.heap[0]

    def extractMin(self):
        val = self.heap[0]
        self.len -= 1
        if self.len > 1:
            self.heap[0] = self.heap.pop(self.len)
            self.heapify(0)
        else:
            self.heap.pop(0)
        return val

    def buildHeap(self):
        for i in range(BinaryMinHeap.parent(self.len - 1), -1, -1):
            self.heapify(i)


# Max-heap class
class BinaryHeap:
    def __init__(self, heap=None):
        if heap is None:
            heap = []
        self.heap = heap
        self.len = len(heap)
        if heap is not None:
            self.buildHeap()

    # left child
    @staticmethod
    def left(i):
        return i * 2 + 1

    # right child
    @staticmethod
    def right(i):
        return i * 2 + 2

    # parent
    @staticmethod
    def parent(i):
        if i == 0:
            return -1
        return (i - 1) // 2

    # inserting into a heap
    def insert(self, k):
        self.heap.append(k)
        i = self.len
        self.len += 1
        while i > 0:
            p = BinaryHeap.parent(i)
            if self.heap[i] > self.heap[p]:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p
            else:
                break

    # rebalance the heap
    def heapify(self, i):
        left = BinaryHeap.left(i)
        right = BinaryHeap.right(i)
        if left < self.len and self.heap[i] <= self.heap[left]:
            if right < self.len and self.heap[left] >= self.heap[right]:
                self.heap[i], self.heap[left] = self.heap[left], self.heap[i]
                i = left
            elif right < self.len:
                self.heap[i], self.heap[right] = self.heap[right], self.heap[i]
                i = right
            else:
                self.heap[i], self.heap[left] = self.heap[left], self.heap[i]
                i = left
            self.heapify(i)
        elif right < self.len and self.heap[i] <= self.heap[right]:
            self.heap[i], self.heap[right] = self.heap[right], self.heap[i]
            i = right
            self.heapify(i)

    # returns maximum element
    def maximum(self):
        if self.len == 0:
            return None
        return self.heap[0]

    # removes , returns and rebalances the heap
    def extractMax(self):
        val = self.heap[0]
        self.len -= 1
        if self.len > 1:
            self.heap[0] = self.heap.pop(self.len)
            self.heapify(0)
        else:
            self.heap.pop(0)
        return val

    # building the heap
    def buildHeap(self):
        for i in range(BinaryHeap.parent(self.len - 1), -1, -1):
            self.heapify(i)

    def __str__(self):
        s = ""
        for i in self.heap:
            s += str(i) + " "
        return s



# sorting the heap elements
def heapSort(l):
    H = BinaryMinHeap(l)
    for i in range(H.len):
        elem = H.extractMin()
        H.heap.append(elem)
    return H.heap



# class of each task with its attributes
class Task:
    def __init__(self):
        self.arrival = None
        self.time = None
        self.name = None
        self.priority = None

    def __lt__(self, other):
        return self.priority < other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __ge__(self, other):
        return self.priority >= other.priority



# class of all the tasks
class Tasks:
    def __init__(self, n):
        self.l = [Task() for i in range(n)]

    def arrivalSort(self):
        return heapSort(self.l)


# priority queue class
class PriorityQueue:
    def __init__(self):
        self.a = BinaryHeap()

    # returns topmost element
    def top(self):
        return self.a.maximum()

    # insert into the priority queue
    def enqueue(self, x):
        self.a.insert(x)

    # remove and return from priority queue
    def dequeue(self):
        return self.a.extractMax()

    # checks if priority queue is empty or not
    def isEmpty(self):
        if self.a.len == 0:
            return True
        else:
            return False



# main driver class
def main():
    print("Enter number of Tasks and Total Time to finish them")
    n = int(input())
    t = int(input())
    T = Tasks(n)
    # take in user inputs
    print("Enter Name,Arrival Time,Time required and Priority of Tasks")
    for i in range(n):
        print("Enter Details of Task ", i + 1, ":")
        T.l[i].name = input()
        T.l[i].arrival = int(input())
        T.l[i].time = int(input())
        T.l[i].priority = int(input())
    P=Tasks(n)
    #Sorting the tasks based on Arrival Time
    P=T.arrivalSort()
    k = []
    Q = PriorityQueue()
    cnt = 0
    for i in range(1, t + 1):
        # get all tasks of this time unit and push them
        while cnt < n and P[cnt].arrival == i:
            Q.enqueue(P[cnt])
            cnt += 1
        if not Q.isEmpty():
            tmp = Q.top()
            if tmp not in k:
                print(tmp.name, " has been started at time:", i)
                k.append(tmp)
            Q.dequeue()
            tmp.time -= 1
            # check if task if fully completed
            if tmp.time:
                Q.enqueue(tmp)
            else:
                print(tmp.name, " has been completed at time:", i)
    # check for time insufficiency
    while not Q.isEmpty():
        tmp2 = Q.dequeue()
        print(tmp2.name, " could not be completed due to insufficient time.")



# calling main class
if __name__ == '__main__':
    main()
