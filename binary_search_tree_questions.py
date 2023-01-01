"""
Question-1
Write an efficent algoritm thats able to compare two binary search trees. The method returns "True" if the tree are identical (same Topology with same Values in the nodes) otherwise it returns "False"
"""

# STEP-2 => Create comaprison method that takes in the root nodes and traverse both BST simultaneously
def compareBST(rootNode1, rootNode2):
  if rootNode1.data is rootNode2.data:
    if rootNode1.leftNode and rootNode2.leftNode:
      compareBST(rootNode1.leftNode, rootNode2.leftNode)
      if rootNode1.rightNode and rootNode2.rightNode:
        compareBST(rootNode1.rightNode, rootNode2.rightNode)
    return True
  else:
    return False
  
# STEP-1 => Create a BST with insert() and traverse() esential for comparision
# Binary Search Tree Implementation
#Node is composite class for BST
class Node:
  def __init__(self, data):
    self.data = data
    self.leftNode = None
    self.rightNode = None

#BST with insert() and traverse() methods
class BinarySearchTree:
  def __init__(self):
    self.root = None
  def insert(self, data):
    if not self.root:
      self.root = Node(data)
    else:
      node = self.root
      while True:
        if data < node.data and node.leftNode:
          node = node.leftNode
        elif data > node.data and node.rightNode:
          node = node.rightNode
        elif data < node.data and not node.leftNode:
          leafNode = Node(data)
          node.leftNode = leafNode
          break
        elif data > node.data and not node.rightNode:
          leafNode = Node(data)
          node.rightNode = leafNode
          break
  #we will traverse with postorder method
  def traverse_postorder(self):
    #<left> <right> <root> 
    if self.root:
      self.postorder(self.root)
  def postorder(self, node):
    if node.leftNode is not None:
      self.postorder(node.leftNode)
    if node.rightNode is not None:
      self.postorder(node.rightNode)
    print(node.data)  


    
#BST-1
BST1 = BinarySearchTree()
BST1.insert(50) 
BST1.insert(25) 
BST1.insert(10) 
BST1.insert(35)
BST1.insert(80)
BST1.insert(65)
BST1.insert(90)
BST1.insert(8)
BST1.insert(12)
BST1.insert(60)
BST1.insert(85)
BST1.insert(95)
#BST1.traverse_postorder()
#BST-2
BST2 = BinarySearchTree()
BST2.insert(50) 
BST2.insert(25) 
BST2.insert(10) 
BST2.insert(35)
BST2.insert(80)
BST2.insert(65)
BST2.insert(90)
BST2.insert(8)
BST2.insert(12)
BST2.insert(60)
BST2.insert(85)
BST2.insert(95)
#BST2.traverse_postorder()

print(compareBST(BST1.root, BST2.root))