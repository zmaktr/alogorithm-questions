# red black tree properties
# 1) always add a new node into the tree as red node
# 2) each red node must have two black nodes
# 3) a null pointer is considered as a black node
# 4) root node will always be a black node
# 5) red node must have a black parent

class Colour:
  RED = 1
  BLACK = 2

class Node:
  def __init__(self, data, parent=None, colour=Colour.RED):
    self.data = data
    self.parent = parent
    self.colour = colour
    self.left_node = None
    self.right_node = None

class RedBlackTree:
  def __init__(self):
    self.root = None
    
  def insert(self, data):
    if not self.root:
      root = Node(data)
    else:
      self.insert_node(self.root, data)

  def insert_node(self, node, data):
    if data < node.data:
      if node.left_node:
        insert_node(node.left_node, data)
      else:
        left_node = Node(data, parent=node)
        self.settle_violation(left_node)
    if data > node.data:
      if node.right_node:
        insert_node(node.right_node, data)
      else:
        right_node = Node(data, parent=node)
        self.settle_violation(right_node)
      
  def traverse(self):
    if self.root:
      self.inorder_traverse(self.root)
  
  def inorder_traverse(self, node):
    if node.left_node:
      inorder_traverse(node.left_node)
    print(node.data)
    if node.right_node:
      inorder_traverse(node.right_node)

  def rotate_right(self, node):
    """
          (A)                ===>(ROTATE RIGHT)              (B)    
        /     \                                           /      \
     (B)      (E)                                      (C)        (A)
     /   \    /  \          (ROTATE LEFT)<===          /  \      /   \
   (C)  (D)  T5  T6                                   T1  T2  (D)    (E)
   / \   / \                                                  /  \  /  \
  T1 T2 T3 T4                                                T3  T4 T5  T6
    """
      
  print("rotating to the right on node", node.data)
  
  # define existing nodes as variables   # node = A
  temp_left_node = node.left_node        # (1)temp_left_node = B
  t = temp_left_node.right_node          # (2)t = D
  
  # change node references (only A + B require change)
  temp_left_node.right_node = node       # (1)temp_left_node.right_node(B's right_node) = A
  node.left_node = t                     # (2)node.left_node(A's left_node) = D
  
  # assiging parents to the rotated nodes (only A + B + D)
  if t:                                
    t.parent = node                      # (1) D's parent is now A
  if node.parent:
    temp_left_node.parent = node.parent  # (2) B's parent is now A's parent
    node.parent = temp_left_node         # (3) A's parent is now B
  # node is the root node with parent None
  else:
    temp_left_node.parent = None
    node.parent = temp_left_node
    # update root node
    self.root = temp_left_node

  def rotate_left(self, node):
    """
          (A)                ===>(ROTATE RIGHT)              (B)    
        /     \                                           /      \
     (B)      (E)                                      (C)        (A)
     /   \    /  \          (ROTATE LEFT)<===          /  \      /   \
   (C)  (D)  T5  T6                                   T1  T2  (D)    (E)
   / \   / \                                                  /  \  /  \
  T1 T2 T3 T4                                                T3  T4 T5  T6
    """
      
  print("rotating to the left on node", node.data)
  
  # define existing nodes as variables   # node = B
  temp_right_node = node.right_node      # (1)temp_right_node = A
  t = temp_right_node.left_node          # (2)t = D
  
  # change node references (only A + B require change)
  temp_right_node.left_node = node       # (1)temp_right_node.left_node(A's left_node) = B
  node.right_node = t                    # (2)node.right_node(B's right_node) = D
  
  # assiging parents to the rotated nodes (only A + B + D)
  if t:                                
    t.parent = node                      # (1) D's parent is now B
  if node.parent:
    temp_right_node.parent = node.parent # (2) A's parent is now B's parent
    node.parent = temp_right_node        # (3) B's parent is now A
  # node is the root node with parent None
  else:
    temp_right_node.parent = None
    node.parent = temp_right_node
    # update root node
    self.root = temp_right_node