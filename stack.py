class Stack:
  def __init__(self):
    self.stack = []

  # time complexity O(1)
  def push(self, data):
    self.stack.append(data)
  
  # time complexity O(1)
  def pop(self):
    if self.stack_size() < 1:
      return print("Stack is empty")
    else:
      del self.stack[-1]

  # time complexity O(1)
  def peek(self):
    return print(self.stack[-1])
  
  # time complexity O(1)
  def is_empty(self):
    return print(self.stack == [])

  # time compleity O(1)
  def stack_size(self):
    return print(len(self.stack))


stk = Stack()
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.peek()
stk.pop()
stk.peek()
stk.is_empty()
stk.stack_size()