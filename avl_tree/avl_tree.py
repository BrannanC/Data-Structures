"""
Node class to keep track of
the data internal to individual nodes
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""


class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
  Display the whole tree. Uses recursive def.
  """

    def display(self, level=0, pref=''):
        # self.update_height()  # Update height before balancing
        # self.update_balance()

        if self.node != None:
            print('-' * level * 2, pref, self.node.key,
                  f'[{self.height}:{self.balance}]',
                  'L' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    """
  Computes the maximum number of levels there are
  in the tree
  """

    def update_height(self):
        self.update_height_helper(self)

    def update_height_helper(self, node, acc=0):
        if node is None:
            return acc - 1
        if not node.node.left and not node.node.right:
            node.height = acc
            return acc

        node.height = max(self.update_height_helper(node.node.left, acc),
                          self.update_height_helper(node.node.right, acc)) + 1
        return node.height

    """
  Updates the balance factor on the AVLTree class
  """

    def update_balance(self):
        l = 0
        r = 0
        if self.node.left:
            l = self.node.left.height + 1
            self.node.left.update_balance()
        if self.node.right:
            r = self.node.right.height + 1
            self.node.right.update_balance()
        self.balance = r - l
    """
  Perform a left rotation, making the right child of this
  node the parent and making the old parent the left child
  of the new parent.
  """

    def left_rotate(self):
        node = self.node
        temp = node.key
        node.key = node.right.node.key
        node.right.node.key = temp

        bot_node = node.right
        node.right = node.right.node.right
        bot_node.node.right = bot_node.node.left
        bot_node.node.left = node.left
        node.left = bot_node

    """
  Perform a right rotation, making the left child of this
  node the parent and making the old parent the right child
  of the new parent.
  """

    def right_rotate(self):
        node = self.node
        temp = node.key
        node.key = node.left.node.key
        node.left.node.key = temp

        bot_node = node.left
        node.left = node.left.node.left
        bot_node.node.left = bot_node.node.right
        bot_node.node.right = node.right
        node.right = bot_node

    """
  Sets in motion the rebalancing logic to ensure the
  tree is balanced such that the balance factor is
  1 or -1
  """

    def rebalance(self):
        if self.balance < -1:
            lb = self.node.left.balance
            if lb > 1 or lb < -1:
                self.node.left.rebalance()
            elif lb == 1:
                self.node.left.left_rotate()
            if self.balance < -1:
                self.right_rotate()
        elif self.balance > 1:
            rb = self.node.right.balance
            if rb < - 1 or rb > 1:
                self.node.right.rebalance()
            elif self.node.right.balance == -1:
                self.node.right.right_rotate()
            if self.balance > 1:
                self.left_rotate()

        self.update_height()
        self.update_balance()
        if self.balance < -1 or self.balance > 1:
            self.rebalance()
    """
  Uses the same insertion logic as a binary search tree
  after the value is inserted, we need to check to see
  if we need to rebalance
  """

    def insert(self, key):
        if self.node is None:
            self.node = Node(key)
        elif self.node.key > key:
            if self.node.left:
                self.node.left.insert(key)
            else:
                self.node.left = AVLTree(Node(key))
        else:
            if self.node.right:
                self.node.right.insert(key)
            else:
                self.node.right = AVLTree(Node(key))

        self.update_height()
        self.update_balance()
        self.rebalance()
