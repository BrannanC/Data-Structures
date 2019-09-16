from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return
        else:
            last = self.storage.remove_from_head()
            self.size -= 1
            return last

    def len(self):
        return self.size


q = Queue()
q.enqueue(2)
q.enqueue(200)
q.dequeue()
q.dequeue()
q.dequeue()
print(q.len())
