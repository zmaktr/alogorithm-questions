class Node:
  def __init__(self, data, nextPointer=None, prevPointer=None):
    self.nextPointer = nextPointer
    self.prevPointer = prevPointer
    self.data = data

class Doubly_linkedlist:
  def __init__(self):
    self.head = None
    self.tail = None
    self.count = 0

  def size_of_list(self):
    return print(self.count)

  # time complexity O(1)
  def insert_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
      self.count += 1
    else:
      new_node.nextPointer = None 
      new_node.prevPointer = self.tail
      self.tail.nextPointer = new_node
      self.tail = new_node
      self.count += 1

  # we can traverse doubly linkedlist in both directions
  # time complexity O(n)
  def traverse_forward(self):
    if self.head is not None:
      node = self.head
      while node is not None:
        print(node.data)
        node = node.nextPointer

  def traverse_backwards(self):
    if self.tail is not None:
      node = self.tail
      while node is not None:
        print(node.data)
        node = node.prevPointer

list = Doubly_linkedlist()
list.insert_end(1)
list.insert_end(2)
list.insert_end(3)
list.insert_end(4)
list.insert_end(5)
list.size_of_list()
list.traverse_forward()
list.traverse_backwards()
