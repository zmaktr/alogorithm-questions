class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList(Node):
  def __init__(self, head)
    self.head = None
    self.count = 0
  
# O(1) constant time complexity
  def insert_beginning(self,data):
    currentNode = Node(data)
    if self.head is None:
      self.head = currentNode
    else:
      currentNode.next = self.head
      self.head = currentNode
    self.count += 1
  
    # O(n) linear time complexity
  def insert_end(self,data):
    currentNode = Node(data)
    if self.head is None:
      self.head = currentNode
    else:
      headNode = self.head
      while headNode.next is not None:
        lastNode = headNode.next
      lastNode.next = currentNode
    self.coint += 1
      