'''
Implementation of Breadth-First-Search with forward relationship
Steps:
  0 - Create a node class with its attributes 
  1 - Start with a root_node
  2 - Visit all adjacent_list nodes 
  3 - Mark the visited the root_node as visited
  4 - Pop the root_node
  5 - Visit the adjacent_list nodes for their ajacent_list 
  6 - Make the visited adjacent_list nodes marked as visited
  7 - Pop the visited adjavent_list
  8 - Repeat step-5
'''
class Node():
  def __init__(self, name, visited=False, adjacent_list=[]):
    self.name = name
    self.adjacent_list = adjacent_list
    self.visited = visited

def breadth_first_search(start_node):
  queue = [start_node]
  
  while queue:
    queue = [node for node in queue[-1].adjacent_list if not node.visited] + queue
    if queue[-1].visited == False:
     print(queue[-1].name)
    queue[-1].visited = True
    queue.pop(-1)
    
    
    

  

  
#A--->B------>C
#|    |
#v    v
#E--->D

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')

A.adjacent_list = [B,E]
B.adjacent_list = [A,D,C]
C.adjacent_list = [B]
D.adjacent_list = [E,B]
E.adjacent_list = [A,D]

breadth_first_search(A)
