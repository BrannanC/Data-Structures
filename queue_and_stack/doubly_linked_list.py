"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
  as the new head of the list. Don't forget to handle
  the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        if len(self) == 0:
            node = ListNode(value)
            self.tail = node
            self.head = node
            self.length = 1
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
            self.length += 1

    """Removes the List's current head node, making the
  current head's next node the new head of the List.
  Returns the value of the removed Node."""

    def remove_from_head(self):
        temp = self.head
        if self.tail == self.head:
            self.delete(self.head)
            self.length = 0
        else:
            self.head = temp.next
            temp.delete()
            self.length -= 1
        return temp.value

    """Wraps the given value in a ListNode and inserts it
  as the new tail of the list. Don't forget to handle
  the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        if len(self) == 0:
            node = ListNode(value)
            self.tail = node
            self.head = node
            self.length = 1
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
            self.length += 1

    """Removes the List's current tail node, making the
  current tail's previous node the new tail of the List.
  Returns the value of the removed Node."""

    def remove_from_tail(self):
        temp = self.tail
        if self.tail == self.head:
            self.delete(self.tail)
            self.length = 0
        else:
            self.tail = temp.prev
            temp.delete()
            self.length -= 1
        return temp.value

    """Removes the input node from its current spot in the
  List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        value = node.value
        if node is self.head:
            return
        if node == self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1

        self.add_to_head(value)

    """Removes the input node from its current spot in the
  List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        value = node.value
        if node is self.tail:
            return
        if node == self.head:
            self.remove_from_head()
        else:
            self.length -= 1
            node.delete()

        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
  the node was the head or the tail"""

    def delete(self, node):
        if node is self.head and node is self.tail:
            node.delete()
            self.head = None
            self.tail = None
            self.length = 0
        elif node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            self.length -= 1
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        max_value = self.head.value
        current_node = self.head
        if len(self) == 0:
            return None
        while True:
            print(current_node.value)
            if current_node.value > max_value:
                max_value = current_node.value
            if current_node == self.tail:
                break
            current_node = current_node.next
        return max_value
