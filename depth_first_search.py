"""
Implementation of Depth-First-Search
"""
#<================ RECURSIVE APPROCH ===============>
"""
Steps:
 1- Start with the root node in the stack
 2- If the latest added node in the stack has adjacent nodes check 1) if the nodes were already visited OR 2) the nodes are already in the list  
 3- if 2nd step conditions are False append the adjacent nodes to the stack
 4- maked the last visted node in stack to True and pop it out of the stack
 5- recursively check for adjacent nodes while maintaining a stack list for each recursion
"""
class Node:
  def __init__(self, name:str, adjacent_list:list = []):
    self.name = name
    self.visited = False
    self.adjacent_list = adjacent_list

def depth_first_search(stack=[]):
  adjacent_nodes = []
  if stack[-1].adjacent_list:
    for node in stack[-1].adjacent_list:
        # please add both these checks 
        if node not in stack and not node.visited:
          adjacent_nodes.append(node)

  if not stack[-1].visited:
    stack[-1].visited = True
    print(stack[-1].name)
  
  stack.pop(-1)

  stack = stack + adjacent_nodes
  adjacent_nodes = []

  if len(stack) > 0:
    depth_first_search(stack)
    

#<============= NON - RECURSIVE APPROCH ============>
"""
Steps:
  1- define a node class and its attributes
  2- define a depth-first-search method
  3- implement a stack DS and start from the root_node
  4- start the while loop
  5- for the last item in the stack check adjacent list and add it to the stack if 1) its not visited AND 2) if its not already in the stack
  6- remove the last item in the stack has adjacent list thats 1) visited OR 2) already in the stack
  7- repeat the loop at step-5
"""
"""
class Node:
  def __init__(self, name:str, adjacent_list:list = []):
    self.name = name
    self.visited = False
    self.adjacent_list = adjacent_list

def has_adjacent_list(node): 
  if node.adjacent_list == []:
    return False
  else:
    return True

def next_unvisited_node_and_not_in_stack(node, stack):
  if node.adjacent_list != []:
    for node in node.adjacent_list:
      if not node.visited and node not in stack:
        return node
  else:
    return None

def remove_and_visit(node, stack):
    node.visited = True
    print(node.name)
    stack.pop(-1)
  
def depth_first_search(start_node):
  stack = [start_node]

  while stack:
    top_node = stack[-1]
    
    if has_adjacent_list(top_node):
      next_node = next_unvisited_node_and_not_in_stack(top_node, stack)
      
      if next_node is not None:
        stack.append(next_node)
      else:
        remove_and_visit(top_node, stack)
    
    else:
      remove_and_visit(top_node, stack)
"""

# TREE
#  A --> B <---C --> D
#  |     |     ^
#  v     v     |
#  E     F --> G
#        |
#        v
#        H

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')
A.adjacent_list = [B,E]
B.adjacent_list = [F]
C.adjacent_list = [B,D]
F.adjacent_list = [H,G]
G.adjacent_list = [C]

depth_first_search([B])