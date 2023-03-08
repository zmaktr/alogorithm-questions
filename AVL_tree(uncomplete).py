#https://www.youtube.com/watch?v=lxHF-mVdwK8
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
    if node is None:
      return -1
    elif node.leftNode and node.rightNode:
      node.height = max(node.leftNode.height, node.rightNode.height) + 1
    elif node.leftNode and not node.rightNode:
      node.height = max(node.leftNode.height, -1) + 1
    elif not node.leftNode and node.rightNode:
      node.height = max(-1, node.rightNode.height) + 1
    elif not node.leftNode and not node.rightNode:
      node.height = max(-1, -1) + 1
    return node.height

  def balance_factor(self, node):
    balance = self.calculate_height(node.leftNode) - self.calculate_height(node.rightNode)
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
    
   parent-node                                  parent-node
        |                                            |  
     Node-1                                        Node-2
     /    \                                       /      \ 
   T1    Node-2                               Node1     Node-3
          /   \         (after rotation)     /    \      /   \
         T2   Node-3         ==>>          T1      T2  T3     T4
              /    \                                       
            T3      T4                                    
            
    3) Left-Right Heavy Situation
     
     parent-node                                     parent-node                                       parent-node 
         |                                                |                                                 |
       Node-1                                           Node-1                                            Node-3
       /    \             (1st rotation)                /    \             (2nd rotation)                /      \ 
   Node-2    T1   (right-right heavy situation)    Node-3     T1   (left-left heavy situation)       Node-2    Node-1
    /    \                 (at Node2)               /    \                  (at Node1)               /    \    /    \
   T2   Node-3               ==>>               Node-2    T3                   ==>>                T2     T4  T3     T1
        /    \                                  /    \                                           
      T4      T3                              T2     T4                                        
      
    4) Right-Left Heavy Situation

   parent-node                                        parent-node                                       parent-node
       |                                                  |                                                  |
     Node-1                                             Node-1                                             Node-3
     /    \                (1st rotation)               /    \               (2nd rotation)               /      \     
   T1    Node-2     (left-left heavy situation)       T1    Node-3    (right-right heavy situation)  Node-1      Node-2
          /   \              (at Node2)                      /    \           (at Node1)              /   \       /   \
      Node-3   T2               ==>>                       T3    Node-2          ==>>               T1     T3    T4    T2
      /    \                                                     /    \                                             
    T3      T4                                                  T4     T2                                         
    
    """
    #there can be four situations
    if self.balance_factor(node) > 1:
      #CASE-1 => left-left heavy situation
      if node.leftNode and self.balance_factor(node.leftNode) > 0:
        self.left_left_heavy(node)
      #CASE-2 => left-right heavy situation  
      elif node.leftNode and self.balance_factor(node.leftNode) < 0:
        self.right_right_heavy(node.leftNode)
        self.left_left_heavy(node)
    elif self.balance_factor(node) < -1:
      #CASE-3 => right-right heavy situation
      if node.rightNode and self.balance_factor(node.rightNode) < 0:
        self.right_right_heavy(node)
      #CASE-4 => right-left heavy situation
      elif node.rightNode and self.balance_factor(node.rightNode) > 0:
        self.left_left_heavy(node.rightNode)
        self.right_right_heavy(node)
    return node
    
  def left_left_heavy(self, node):
   #declare initial nodes to be rotated
    node1 = node
    node2 = node1.leftNode
    if node1.parent is not None:
      parentNode = node1.parent
    else:
      parentNode = None
    if node1.leftNode.rightNode is not None:
      t2 = node1.leftNode.rightNode
    else:
      t2 = None
    
    #making rotations
    node1.parent, node1.leftNode = node2, t2
    node2.parent, node2.rightNode = parentNode, node1
    if t2 is not None:
      t2.parent = node1
    
    #update root node after rotation (only if the node is a root node)
    if node2.parent is None:
      self.root = node2
    
    return node1

  def right_right_heavy(self, node):
    #declare initial nodes to be rotated
    node1 = node
    node2 = node1.rightNode
    if node1.parent is not None:
      parentNode = node1.parent
    else:
      parentNode = None
    if node1.rightNode.leftNode is not None:
      t2 = node1.rightNode.leftNode
    else:
      t2 = None
    
    #making rotations
    node1.parent, node1.rightNode = node2, t2
    node2.parent, node2.leftNode = parentNode, node1
    if t2 is not None:
      t2.parent = node1
      
    #update root node after rotation (only if the node is a root node)
    if node2.parent is None:
      self.root = node2
    
    return node1
    
  def handle_violation(self, node):
    while node is not None:
      self.calculate_height(node)
      if self.balance_factor(node) < -1 or self.balance_factor(node) > 1:
        self.make_rotations(node)
      node = node.parent

  def remove(self, data):
    if self.root.data == data:
      predecessorNode = self.predecessor_node(self.root)
      predecessorParent = predecessorNode.parent
      self.root.data = predecessorNode.data
      del predecessorNode
      self.handle_violation(predecessorParent)
    else:
      self.remove_node(self.root, data)
  
  def remove_node(self, node, data):
    #STEP-1 => iterate to left/right node to find the exact node to be deleted
    if node.data > data and node.leftNode is not None:
      self.remove_node(node.leftNode, data)
    elif node.data < data and node.rightNode is not None:
      self.remove_node(node.rightNode, data)
    #STEP-2 => once you find the node check the possibilities to delete the node 
    elif node.data == data:
      parentNode = node.parent
      childLeftNode = node.leftNode
      childRightNode = node.rightNode
      #case-1 node is a leaf node
      if childLeftNode is None and childRightNode is None:
        if node.parent.leftNode is node:
          node.parent.leftNode = None
          print(f"line 215 {node.data}")
          del node
        elif node.parent.rightNode is node:
          node.parent.rightNode = None
          print(f"line 219 {node.data}")
          del node
        #check AVL violation
        self.handle_violation(parentNode)
      #case-2 node has children
      #subcase-2.1 leftchild is empty rightchild has children
      if childLeftNode is None and childRightNode is not None:
        if node.parent.leftNode is node:
          node.parent.leftNode = childRightNode
          print(f"line 228 {node.data}")
          del node
        elif node.parent.rightNode is node:
          node.parent.rightNode = childRightNode
          print(f"line 232 {node.data}")
          del node
        #check AVL violation
        self.handle_violation(parentNode)
      #subcase-2.2 rightchild is empty leftchild has children
      elif childLeftNode is not None and childRightNode is None:
        if node.parent.leftNode is node:
          node.parent.leftNode = childLeftNode
          print(f"line 240 {node.data}")
          del node
        elif node.parent.rightNode is node:
          node.parent.rightNode = childLeftNode
          print(f"line 244 {node.data}")
          del node
        #check AVL violation
        self.handle_violation(parentNode)
      #subcase-2.3 rightchild and leftchild has children
      elif childLeftNode is not None and childRightNode is not None:
        predecessorNode = self.predecessor_node(node)
        node.data = predecessorNode.data
        predecessorNodeParent = predecessorNode.parent
        print(f"predecessor {node.data}")
        del predecessorNode  
        #check AVL violation
        self.handle_violation(predecessorNodeParent)
          
  def predecessor_node(self, node):
    node = node.leftNode
    while node.rightNode is not None:
      node = node.leftNode
    return node
    
  def traverse_in_order(self):
    if self.root is not None:
      self.traverse_tree(self.root)
    else:
      print("the tree is empty")
  
  def traverse_tree(self, node):  
    #<leftNode> <rootNode> <rightNode>
    if node.leftNode is not None:
      self.traverse_tree(node.leftNode)
    print(node.data)
    if node.rightNode is not None:
      self.traverse_tree(node.rightNode)


i = AVLTree()
i.insert(50)
i.insert(40)
i.insert(30)
i.insert(35)
i.insert(60)
i.insert(70)
i.insert(65)
#i.remove(70)
#i.remove(30)
#i.remove(35)
i.traverse_in_order()