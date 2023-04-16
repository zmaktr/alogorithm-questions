# define the number of items to be stored inside the heap tree
CAPACITY = 10

# max heap
class Heap:
  def __init__(self):
    # no. of items in the data structure
    self.heap_size = 0
    
    # underlying list data structure 
    self.heap = [0]*CAPACITY
  
  # running time complexity O(log(n))
  def insert(self, item):
    # heap is full
    if self.heap_size == CAPACITY:
      return

    # insert item into the underlying list
    self.heap[self.heap_size] = item
    # fix violated heap properties
    self.fix_up(self.heap_size)

    # increment index for new insersion
    self.heap_size += 1
  
  # running time complexity O(log(n))
  def fix_up(self, index):
    # first check from the index if new insertion is left or right to its parent
    # a left insersion will always have even index
    if index == 0:
      return
    elif index % 2 == 0:
      # index is right child to its parent
      # find parent_index = (i-1)/2
      parent_index = int((index - 2) / 2)
    else:
      # index is left child to its parent 
      # formula parent index = (i-2)/2
      parent_index = int((index - 1) / 2)
    
    # if parent is smaller than inserted children swap values
    if index > 0 and self.heap[index] > self.heap[parent_index]:
      self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
      self.fix_up(parent_index)
  
  # running time complexity O(1)
  def get_max(self):
    # this method will return the max item 
    return self.heap[0]
    
  # running time complexity O(log(n))
  def pool(self):
    # this method returns the max and removes it as well
    max_item = self.get_max()
    self.heap[0], self.heap[self.heap_size - 1] = self.heap[self.heap_size - 1], 0
    self.heap_size -= 1

    # heapify tree
    self.fix_down(0)
    
    return max_item

  def fix_down(self, index):
    # heapify tree from index to downwards 
    right_child_index = 2 * index + 2
    left_child_index = 2 * index + 1
    
    if self.heap_size - 1 == left_child_index and self.heap[index] < self.heap[left_child_index]:
      self.heap[index], self.heap[left_child_index] = self.heap[left_child_index], self.heap[index]
    elif self.heap_size -1  >= right_child_index:
      if self.heap[index] < self.heap[left_child_index] and self.heap[left_child_index] > self.heap[right_child_index]:
        self.heap[index], self.heap[left_child_index] = self.heap[left_child_index], self.heap[index]
        self.fix_down(left_child_index)
      elif self.heap[index] < self.heap[right_child_index] and self.heap[right_child_index] > self.heap[left_child_index]:
        self.heap[index], self.heap[right_child_index] = self.heap[right_child_index], self.heap[index]
        self.fix_down(right_child_index)
  
  def heap_sort(self):
    for _ in range(self.heap_size):
      max_item = self.pool()
      print(max_item)


heap = Heap()
heap.insert(13)
heap.insert(-2)
heap.insert(0)
heap.insert(8)
heap.insert(1)
heap.insert(-5)
heap.insert(99)

# print(heap.heap)
heap.heap_sort()