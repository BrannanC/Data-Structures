class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        temp = self.storage[0]
        self.storage[0] = self.storage.pop()
        self._sift_down(0)
        return temp

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index == 0:
            return
        parent_i = (index - 1) // 2
        if self.storage[index] <= self.storage[parent_i]:
            return
        else:
            temp = self.storage[index]
            self.storage[index] = self.storage[parent_i]
            self.storage[parent_i] = temp
            self._bubble_up(parent_i)

    def _sift_down(self, index):
        st_len = len(self.storage)
        l = None
        r = None
        if index*2+1 < st_len - 1:
            l = self.storage[index*2+1]
        if index*2+2 < st_len - 1:
            r = self.storage[index*2+2]
        if self.storage[index] > l and self.storage[index] > r:
            return
        else:
            temp = self.storage[index]
            i = index*2+1 if l > r else index*2+2
            self.storage[index] = self.storage[i]
            self.storage[i] = temp
            self._sift_down(i)


heap = Heap()
heap.insert(6)
heap.insert(8)
heap.insert(10)
heap.insert(9)
heap.insert(1)
heap.insert(9)
heap.insert(9)
heap.insert(5)
print('[10, 9, 9, 6, 1, 8, 9, 5]')
print(heap.storage)
# ,
