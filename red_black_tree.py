# red black tree properties
# 1) always add a new node into the tree as red node
# 2) each red node must have two black nodes (black nodes can also be null pointers)
# 3) a null pointer is considered as a black node
# 4) root node will always be a black node
# 5) red node must have a black parent
# 6) every path from root to leaf has the same number of black nodes

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
      self.root = Node(data)
      print("Inserted ROOT", self.root.data)
      self.settle_violation(self.root)
    else:
      self.insert_node(self.root, data)

  def insert_node(self, node, data):
    if data < node.data:
      if node.left_node:
        self.insert_node(node.left_node, data)
      else:
        node.left_node = Node(data, parent=node)
        print("Inserted ", node.left_node.data)
        self.settle_violation(node.left_node)
    if data > node.data:
      if node.right_node:
        self.insert_node(node.right_node, data)
      else:
        node.right_node = Node(data, parent=node)
        print("Inserted ", node.right_node.data)
        self.settle_violation(node.right_node)
      
  def traverse(self):
    if self.root:
      self.inorder_traverse(self.root)
  
  def inorder_traverse(self, node):
    if node.left_node:
      self.inorder_traverse(node.left_node)
    print(node.data)
    if node.right_node:
      self.inorder_traverse(node.right_node)

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
    
    # define argument nodes as variables node = A
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
    
    # define argument nodes as variables node node = B
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

  def is_red(self, node) -> bool:
    if node is None:
      return False
    return node.colour == Colour.RED
    
  def settle_violation(self, node):
    '''
    After inserting a new node into red black tree we have check if tree properties have been violated and settle violations:
    1) Check the colours of family (parent, grandparent, uncle and sibling)
    2) Make necessary rotation(s) (if any)
    3) Recolour the node(s)

    CASES:
    To drive all cases you can find all combinations with Red and Black considering the tree was previously balanced (we will discard all combinations were the tree was previously not balanced):
      (visually check cases here https://ibb.co/TMxGcD6 https://ibb.co/w0sCH5v)
    -> The tree is empty 
       (depth = 0) [Total combinations =1 | valid combinations = (R)] (check case-1)
    -> The tree just has a root node 
       (depth = 1) [Total combinations = 12 | valid combinations = (R)-B-R, R-B-(R)] (check case-2) 
    -> The tree is a full tree 
       (depth >= 2) [Total combinations = 32 | valid combinations = R-B-B-(R), R-B-(R)-B, (R)-B-B-B, B-(R)-B-B, B-B-B-(R), B-B-(R)-B, (R)-B-R-B, B-(R)-R-B, B-R-B-(R), B-R-(R)-B, (R)-B-B-R, B-(R)-B-R] (check case-3, case-4, case-5)
    
    Ideal cases where little has to be done:
    1) If the new inserted node is a root node:
        => colour the root node to black
    2) If the new inserted node parent is the root node and if uncle is a null pointer or uncle is red:
        => do nothing
    3) If the new inserted node parent is not the root node and parent has colour black:
        => do nothing
    4) If the new inserted node parent is not the root node and parent has colour red check the uncle colour if RED then:
        => change the parent and uncle colour to black
        => change the grandparent colour to red (if grandparent is root node colour it black)
        => repeat the same step from grandparent considering it as the new node
    
    Case where more has to be done (uncle is black)
    5) If the new inserted node parent is not the root node and parent has colour red check the uncle colour if BLACK then there are four cases:
      5(a) Left-Left Rotation
      5(b) Left-Right Rotation
      5(c) Right-Right Rotation
      5(d) Right-Left Rotation
        
    KEY:
    G.P = Grand parent
    P = Parent
    S = Sibling
    U = Uncle
    Node = x
    B = Black
    R = Red
                                                
    a) Left-Left Rotation
  
                 (G.P-B)               ===> Rotate Right                         (P-B)                     
                /       \              ===> Swap Colours of G.P & P            /       \
            (P-R)       (U-B)                                              (N-R)      (G.P-R)
          /      \    /      \                                            /      \    /      \
        (N-R)    T3  T4       T5                                        T1       T2  T3     (U-B)
      /      \                                                                              /     \
     T1      T2                                                                            T4      T5
     
    b) Left-Right Rotation
    
             (G.P-B)         ===> Rotate R-R Rotation  (G.P-B)        ===> Apply same L-L rotation            (N-B) 
            /       \             on parent           /       \        (1) Rotate Right                     /       \
        (P-R)       (U-B)                         (N-R)       (U-B)    (2) Swap Colours of G.P & Node  (P-R)      (G.P-R)
      /      \    /      \                      /      \    /      \                                  /      \    /      \
     T1   (N-R)  T4       T5                 (P-R)     T3  T4       T5                              T1       T2  T3     (U-B)
         /     \                            /     \                                                                    /     \
       T2       T3                         T1     T2                                                                  T4      T5
     
    c) Right-Right Rotate
  
            (G.P-B)                  ===> Rotate Left                          (P-B) 
           /       \                 ===> Swap Colours of G.P & P           /        \
        (U-B)     (P-R)                                                 (G.P-R)      (N-R)
       /    \     /    \                                                /     \      /    \
     T1     T2   T3   (N-R)                                          (U-B)    T3    T4    T5
                     /     \                                        /    \
                    T4     T5                                      T1    T2

    d) Right-Left Rotate
            
            (G.P-B)           ===> Rotate Parent      (G.P-B)        ===> Apply same L-L rotation               (N-B)
           /       \               with node         /       \        (1) Rotate Left                         /       \
        (U-B)     (P-R)                           (U-B)     (N-R)     (2) Swap Colours of G.P & Node     (G.P-R)     (P-R)
       /    \     /    \                         /    \     /    \                                       /    \     /    \
     T1     T2  (N-R)   T5                     T1     T2   T3   (P-R)                                 (U-B)   T3   T4     T5
                /   \                                           /    \                               /    \
               T3   T4                                         T4    T5                             T1    T2
               
    '''
    # HANDLE ALL CASES
    # loop will break once the node is root node + node is black + and node parent is None
    while node != self.root and self.is_red(node) and self.is_red(node.parent):
      # get parent + grand parent + uncle
      parent_node = node.parent
      grand_parent_node = parent_node.parent
      if parent_node == grand_parent_node.left_node:
        uncle = grand_parent_node.right_node
        # uncle is RED CASE-4
        if uncle and self.is_red(uncle):
          print("Settling violation for", node.data)
          grand_parent_node.colour = Colour.RED
          parent_node.colour = Colour.BLACK
          uncle.colour = Colour.BLACK
          node = grand_parent_node
        # uncle is BLACK CASE-5
        elif uncle and not self.is_red(uncle):
          # L-R heavy situation CASE-5(b)
          if node == parent_node.right_node:
            # make rotations
            print("Settling violation for", node.data)
            self.rotate_left(parent_node)
            self.rotate_right(grand_parent_node)
            # change colour
            grand_parent_node.colour = Colour.RED
            node.colour = Colour.BLACK
            # reassign node for next iteration
            node = parent_node
          # L-L heavy situation CASE-5(a)
          elif node == parent_node.left_node:
            # make rotations
            print("Settling violation for", node.data)
            self.rotate_right(grand_parent_node)
            # change colour
            grand_parent_node.colour = Colour.RED
            parent_node.colour = Colour.BLACK
            # reassign node for next iteration
            node = parent_node
            
      elif parent_node == grand_parent_node.right_node:
        uncle = grand_parent_node.left_node
        # uncle is RED CASE-4
        if uncle and self.is_red(uncle):
          print("Settling violation for", node.data)
          grand_parent_node.colour = Colour.RED
          parent_node.colour = Colour.BLACK
          uncle.colour = Colour.BLACK
          node = grand_parent_node
        # uncle is BLACK CASE-5
        elif uncle and not self.is_red(uncle):
          # R-L heavy situation CASE-5(d)
          if node == parent_node.left_node:
            # make rotations
            print("Settling violation for", node.data)
            self.rotate_right(parent_node)
            self.rotate_left(grand_parent_node)
            # change colour
            grand_parent_node.colour = Colour.RED
            node.colour = Colour.BLACK
            # reassign node for next iteration
            node = parent_node
          # R-R heavy situation CASE-5(c)
          elif node == parent_node.right_node:
            # make rotations
            print("Settling violation for", node.data)
            self.rotate_left(grand_parent_node)
            # change colour
            grand_parent_node.colour = Colour.RED
            parent_node.colour = Colour.BLACK
            # reassign node for next iteration
            node = parent_node
    
    # node inserted is root node CASE-1      
    if self.is_red(self.root):
      print("Settling violation for ROOT", self.root.data)
      self.root.colour = Colour.BLACK
          
      




tree = RedBlackTree()
tree.insert(32)
tree.insert(10)
tree.insert(55)
tree.insert(1)
tree.insert(19)
tree.insert(79)
tree.insert(16)
tree.insert(23)
tree.insert(12)
tree.traverse()