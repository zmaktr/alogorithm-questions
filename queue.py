class Queue:
  def __init__(self):
    self.queue = []

  # time complexity O(1)
  def enqueue(self, data):
    self.queue.append(data)

  # time complexity O(1)
  def is_empty(self):
    return print(self.queue == [])
    
  # time complexity O(n)
  def dequeue(self):
    if self.queue == []:
      print("The list is empty")
    else:
      del self.queue[0]
 
  # time complexity O(1)
  def peek(self):
    return print(self.queue[0])
  
  # time complexity O(1)
  def size_of_queue(self):
    return print(len(self.queue))

queue = Queue()
queue.is_empty()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.peek()
queue.size_of_queue()
queue.dequeue()
queue.peek()
queue.size_of_queue()