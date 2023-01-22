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
      return node.height = max(node.leftNode.height, node.rightNode.height) + 1
    elif node.leftNode and not node.rightNode:
      return node.height = max(node.leftNode.height, -1) + 1
    elif not node.leftNode and node.rightNode:
      return node.height = max(-1, node.rightNode.height) + 1
    elif not node.leftNode and not node.rightNode:
      return node.height = max(-1, -1) + 1
    elif node = None:
      return -1

  def balance_factor(self, node):
    balance = node.leftNode.height - node.rightNode.height
    return balance
    
  def make_rotations(self, node):
    """
    There are four situations we need to handle here if the tree is unbalanced
    1) Left-Left Heavy Situations
    
      parent-node                          parent-node
           |                                    |  
         Node-1                              Node-2
         /    \                              /     \
     Node-2    T1    (after rotation)    Node-3   Node-1
      /    \              ==>>           /    \   /    \
   Node-3   T2                         T4     T3 T2      T1
    /    \                          
  T4      T3                     
  
    2) Right-Right Heavy Situation
     Node-1
     /    \
   T1    Node-2
          /   \   
         T2   Node-3   
              /    \
            T3      T4
    3) Left-Right Heavy Situation
        Node
       /    \
     Node    T1
    /    \
   T2    Node
        /    \
      T4      T3 
    4) Right-Left Heavy Situation
      Node
     /    \
   T1      Node
          /   \   
       Node    T2   
      /    \
    T3      T4
    """
    #there can be four situations
    if self.balance_factor(node) > 1:
      #CASE-1 => left-left heavy situation
      if node.leftNode and self.balance_factor(node.leftNode) > 0:
        #declare initial nodes to be rotated
        parentNode = node.parent
        node1 = node
        node2 = node.leftNode
        t2 = node2.rightNode
        #rotations
        node1.parent, node1.leftNode = node2, t2
        t2.parent = node1
        node2.parent, node2.rightNode = parentNode, node1
      #CASE-2 => left-right heavy situation  
      elif node.leftNode and self.balance_factor(node.leftNode) < 0:
        pass
    elif balance_factor(node) < -1:
      #CASE-3 => right-right heavy situation
      if node.rightNode and self.balance_factor(node.rightNode) < 0:
        pass
      #CASE-4 => right-left heavy situation
      elif node.rightNode and self.balance_factor(node.rightNode) > 0:
        pass
      
  def handle_violation(self, node):
    while node != None
      self.calculate_height(node)
        if self.balance_factor(node) < -1 or self.balance_factor(node) > 1:
          self.make_rotations(node)
      node = node.parent

  def remove(self, data):
    if self.root.data == data:
      self.root = None
    else:
      self.remove_node(self.root, data)
  
  def remove_node(self, node, data):
    #STEP-1 => iterate to left/right node to find the exact node to be deleted
    if node.data > data:
      self.remove_node(node.leftNode, data)
    elif node.data < data:
      self.remove_node(node.rightNode, data)
    #STEP-2 => once you find the node check the possibilities to delete the node 
    elif node.data == data:
      parentNode = node.parent
      childLeftNode = node.leftNode
      childRightNode = node.rightNode
      #case-1 node has no children
      if childLeftNode is None and childRightNode is None:
        if node.parent.leftNode is node:
          parent.leftNode = None
          del node
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
        elif node.parent.rightNode is node:
          node.parent.rightNode = childRightNode
          del node
        #check AVL violation
        self.handle_violation(node.parent)
      #subcase-2.2 rightchild is empty leftchild has children
      elif childLeftNode is not None and childRightNode is None:
        if node.parent.leftNode is node:
          node.parent.leftNode = childLeftNode
          del node
        elif node.parent.rightNode is node:
          node.parent.rightNode = childLeftNode
          del node
        #check AVL violation
        self.handle_violation(node.parent)
      #subcase-2.3 rightchild and leftchild has children
      elif childLeftNode is not None and childRightNode is not None:
        predecessorNode = self.predecessor_node(node)
        node.data = predecessorNode.data
        predecessorNodeParent = predecessorNode.parent
        del predecessorNode  
        #check AVL violation
        self.handle_violation(predecessorNodeParent)
          
  def predecessor_node(self, node):
    node = node.rightNode
    while node.leftNode is not None:
      node = node.leftNode
    return node
    
#i = AVLTree()
#i.insert(50)

  