#"""
#Option-1 
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
  
  #for insertion each time start from root node each time
  def insert(self, data):
    if self.root is None:
      self.root = Node(data)
    else:
      currentNode = Node(data)
      currentNode.parent = self.root
      while True:
        if currentNode.parent.data > data:
          if currentNode.parent.left_node is None:
            currentNode.parent.left_node = currentNode
            break
          currentNode.parent = currentNode.parent.left_node
        elif currentNode.parent.data < data:
          if currentNode.parent.right_node is None:
            currentNode.parent.right_node = currentNode
            break
          currentNode.parent = currentNode.parent.right_node
        # duplicates in BST are not allowed so no equal (=) condition is placed
  
  def max_node(self):
    max_node = self.root
    if max_node is not None:
      while max_node.right_node is not None:
        max_node = max_node.right_node
    return print(max_node.data)

  def min_node(self):
    min_node = self.root
    if min_node is not None:
      while min_node.left_node is not None:
        min_node = min_node.left_node
    return print(min_node.data)

  def inorder_traverse(self):
    if self.root is not None:
      self.inorder_recursion(self.root)

  def inorder_recursion(self, node):
    if node.left_node is not None:
      self.inorder_recursion(node.left_node)

    print(node.data)

    if node.right_node is not None:
      self.inorder_recursion(node.right_node)
  
  def remove(self, data):
    if self.root is not None:
      self.remove_possibilities(self.root, data)

  def remove_possibilities(self, node, data):
    
    #assign the node we want to remove with a variable
    if data == node.data:
      removeNode = node
      #possibility-1 (the node to delete is the leaf node)
      if removeNode.left_node is None and removeNode.right_node is None:
        #inform parent node that child has been unlinked/removed
        if removeNode.data < removeNode.parent.data:
          removeNode.parent.left_node = None
          #you dont have to del the node the garbage collector will take care of it
          #del removeNode
        elif removeNode.data > removeNode.parent.data:
          removeNode.parent.right_node = None
          #del removeNode
        
      #possibility-2 (the node to delete has child nodes and sigle level of depth)
      #possibility-3 (the node to delete has child nodes and mutiple level of depth)

    #traverse and find the position of the node to be deleted
    if data < node.data:
      self.remove_possibilities(node.left_node, data)
    elif data > node.data:
      self.remove_possibilities(node.right_node, data)
  
    
#"""

"""
#Option-2
class Node:
  def __init__(self, data, parent=None):
    self.data = data
    self.right_node = None
    self.left_node = None
    self.parent = parent

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, data):
    if self.root is None:
      self.root = Node(data)
    else:
      self.insert_node(data, self.root)

  def insert_node(self, data, node):
    if data < node.data:
      if node.left_node is not None:
        self.insert_node(data, node.left_node)
      else:
        node.left_node = Node(data, node)
    else:
      if node.right_node is not None:
        self.insert_node(data, node.right_node)
      else:
        node.right_node = Node(data, node)

  def inorder_traverse(self):
    if self.root is not None:
      self.traverse(self.root)

  def inorder_recursion(self, node):
    if node.left_node is not None:
      self.traverse(node.left_node)
    
    print(node.data)
    
    if node.right_node is not None:
      self.traverse(node.right_node)

"""
          

i = BinarySearchTree()
i.insert(50)
i.insert(2)
i.insert(5)
i.insert(10)
i.insert(15) 
i.insert(20) 
i.insert(25) 
i.insert(30) 
i.insert(35) 
i.insert(40) 
i.insert(45) 
i.insert(55) 
i.insert(60) 
i.insert(65) 
i.insert(70) 
i.insert(75) 
i.insert(80) 
i.insert(85) 
i.insert(90) 
i.insert(95) 
#i.min_node()
#i.max_node()
#i.inorder_traverse()
i.remove(95)
i.inorder_traverse()