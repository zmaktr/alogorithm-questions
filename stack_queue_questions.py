"""
Question:
The aim is to design an algorithm that can return the maximum item of a stack in O(1) running time complexity.
We can use O(n) extra memory!
Hint: we can use another stack to track the max item!
"""

class Stack:
  def __init__(self):
    self.stack = []
    self.maxItem = None

  def push(self,data):
    self.stack.append(data)
    if self.maxItem is None:
      self.maxItem = data
    else:
      if self.maxItem > data:
        pass
      else:
        self.maxItem = data

  def maxMethod(self):
    return print(self.maxItem)

stack = Stack()
stack.push(1)
stack.push(4)
stack.push(3)
stack.maxMethod()
  