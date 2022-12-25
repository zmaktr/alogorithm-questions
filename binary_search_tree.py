class Node:
  def __init__(self, data):
    self.data = data
    self.left_node = None 
    self.right_node = None
    #Although BST have uni-directional relationships. We are adding parent here to help us in remove()
    self.parent = None
    
class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  #for insertion each time start from root node
  def insert(self, data):
    if self.root is None:
      self.root = Node(data)
    else:
      parent = self.root
      currentNode = Node(data)
      while True:
        if parent.data < data:
          if parent.left_node is None:
            parent.left_node = currentNode
            break
          parent = parent.left_node
        elif parent.data > data:
          if parent.right_node is None:
            parent.right_node = currentNode
            break
          parent = parent.right_node
        # duplicates in BST are not allowed so no equal (=) condition is placed
              
          

i = BinarySearchTree()
i.insert(2) 
i.insert(1) 
i.insert(4) 
i.insert(6) 
i.insert(5) 
i.insert(23) 
i.insert(67) 
i.insert(90) 