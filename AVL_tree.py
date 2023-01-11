class Node:
  def __init__(self, data):
    self.data = data
    self.leftNode = None
    self.rightNode = None
    self.parent = None
    self.height = 0

class AVLTree:
  def __init__(self):
    self.root = None

  def insert(self, data):
    if self.root is None:
      self.root = Node(data)
    else:
      self.insert_node(data, self.root)
  
  def insert_node(self, data, node):
    if node.data > data:
      if node.leftNode is not None:
        self.insert_node(data, node.leftNode)
      else:
        currentNode = Node(data)
        #assign attributes to the new added node
        node.leftNode = currentNode
        currentNode.parent = node
        currentNode.height = self.calculate_height(currentNode)
        #check AVL violation
        self.handle_violation(node)
    elif node.data < data:
      if node.rightNode is not None:
        self.insert_node(data, node.rightNode)
      else:
        currentNode = Node(data)
        #assign attributes to the new added node
        node.rightNode = currentNode
        currentNode.parent = node
        node.height = self.calculate_height(node)
        #check AVL violation
        self.handle_violation(node)

  def calculate_height(self, node):
    #deal with four possibilities
    if node.leftNode and node.rightNode:
      return max(node.leftNode.height, node.rightNode.height) + 1
    elif node.leftNode and not node.rightNode:
      return max(node.leftNode.height, -1) + 1
    elif not node.leftNode and node.rightNode:
      return max(-1, node.rightNode.height) + 1
    elif not node.leftNode and not node.rightNode:
      return max(-1, -1) + 1

  def handle_violation(self, node):
    pass

  def remove(self, data):
    if self.root.data == data:
      self.root = None
    else:
      self.remove_node(self.root, data)
  
  def remove_node(self, node, data):
    if node.data > data:
      self.remove_node(node.leftNode, data)
    elif node.data < data:
      self.remove_node(node.rightNode, data)
    elif node.data == data:
      parentNode = node.parent
      childLeftNode = node.leftNode
      childRightNode = node.rightNode
      #case-1 node has no children
      if childLeftNode is None and childRightNode is None:
        if node.parent.leftNode is node:
          parent.leftNode = None
          del node
          #check AVL violation
          self.handle_violation(node)
        elif node.parent.rightNode is node:
          parent.rightNode = None
          del node
          #check AVL violation
          self.handle_violation(node)
      #case-2 node has children
      #subcase-2.1 leftchild is empty rightchild has children
      if childLeftNode is None and childRightNode is not None:
        if node.parent.leftNode is node:
          node.parent.leftNode = childRightNode
          del node
          #check AVL violation
          self.handle_violation(node)
        elif node.parent.rightNode is node:
          node.parent.rightNode = childRightNode
          del node
          #check AVL violation
          self.handle_violation(node)
      #subcase-2.2 rightchild is empty leftchild has children
      elif childLeftNode is not None and childRightNode is None:
        if node.parent.leftNode is node:
          node.parent.leftNode = childLeftNode
          del node
          #check AVL violation
          self.handle_violation(node)
        elif node.parent.rightNode is node:
          node.parent.rightNode = childLeftNode
          del node
          #check AVL violation
          self.handle_violation(node)
      #subcase-2.3 rightchild and leftchild has children
      elif childLeftNode is not None and childRightNode is not None:
          predecessorNode = self.predecessor_node(node)
          node.data = predecessorNode.data
          del predecessorNode  
          
  def predecessor_node(self, node):
    node = node.rightNode
    while node.leftNode is not None:
      node = node.leftNode
    return node
    
#i = AVLTree()
#i.insert(50)

  