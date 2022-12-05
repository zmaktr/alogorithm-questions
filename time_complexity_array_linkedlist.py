import time 

# implementation of linked list
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.count = 0
  
  def size_of_list(self):
    return print(self.count)
  
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
      node = self.head
      while node.next is not None:
        node = node.next
      node.next = currentNode
    self.count += 1
  
  # O(n) linear time complexity
  def traverse(self):
    node = self.head
    while node is not None:
      print(node.data)
      node = node.next

  # O(n) linear time complexity
  def remove(self, value):
    currentNode = self.head
    if currentNode.data == value:
      self.head = currentNode.next
      # no need to set "currentNode = None" GARBAGE COLLECTER will do that
      self.count -= 1
    else:
      while currentNode.data != value and currentNode is not None:
        prevNode = currentNode
        currentNode = currentNode.next
        # check if value in list
        if currentNode is None:
          print("not in list")
          break
      # change references only if value in list
      if currentNode is not None:
        prevNode.next = currentNode.next
        self.count -= 1
      
### Case - 1 => begining 
# time complexity for inserting at begining of linkedlist
li = LinkedList()
now = time.time()
for i in range(5):
  li.insert_beginning(i)
print(f"Time taken to add 5000 items to beginning of Linked List {time.time()-now}")

# time complexity for inserting at begining of array
array = []
now = time.time()
for i in range(5):
  #insert(position, value)
  array.insert(0,i)
print(f"Time taken to add 5000 items to beginning of array {time.time()-now}")

### Case - 2 => end
# time complexity for inserting at begining of linkedlist
li = LinkedList()
now = time.time()
for i in range(5):
  li.insert_end(i)
print(f"Time taken to add 5000 items to end of Linked List {time.time()-now}")

# time complexity for inserting at begining of array
array = []
now = time.time()
for i in range(5):
  array.append(i)
print(f"Time taken to add 5000 items to end of array {time.time()-now}")