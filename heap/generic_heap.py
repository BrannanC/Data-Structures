class Heap:
    def __init__(self, compare, arr=[]):
        self.heap = self.construct(arr)
        self.compare = compare

    def __len__(self):
        return len(self.heap)

    def construct(self, arr):
        if not len(arr):
            return arr
        parent_ind = (len(arr) - 1) // 2
        for i in reversed(range(parent_ind)):
            self.sift_down(i, len(arr)-1, arr)
        return arr

    def sift_down(self, i, end, heap):
        left_child = i * 2 + 1
        while left_child <= end:
            right_child = i * 2 + 2 if i * 2 + 2 <= end else None
            if right_child is not None:
                if self.compare(heap[right_child], heap[left_child]):
                    temp = right_child
                else:
                    temp = left_child
            else:
                temp = left_child
            if self.compare(heap[temp], heap[i]):
                heap[temp], heap[i] = heap[i], heap[temp]
                i = temp
                left_child = i * 2 + 1
            else:
                return

    def sift_up(self, i, heap):
        parent = (i - 1) // 2
        while i > 0:
            if self.compare(heap[i], heap[parent]):
                heap[i], heap[parent] = heap[parent], heap[i]
                i = parent
                parent = (i - 1) // 2
            else:
                return

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        val = self.heap.pop()
        self.sift_down(0, len(self)-1, self.heap)
        return val

    def insert(self, val):
        self.heap.append(val)
        self.sift_up(len(self)-1, self.heap)


def max_heap_func(a, b):
    return a > b


def min_heap_func(a, b):
    return a < b
