def binary_itr(array, target):
  start_index = 0 
  end_index = len(array) - 1
  mid_index = (start_index + end_index) // 2
  
  while target != array[mid_index]:
    mid_index = (start_index + end_index) // 2
    
    if target > array[mid_index]:
      start_index = mid_index + 1
      
    elif target < array[mid_index]:
      end_index = mid_index - 1

  print(mid_index)
#[2,3,4,56,89,90,233,300,301],89

def binary_recur(array, start_index, end_index, target):
  mid_index = (start_index + end_index) // 2
  
  while target != array[mid_index]:
    mid_index = (start_index + end_index) // 2
    
    if target > array[mid_index]:
      return binary_recur(array, mid_index + 1, end_index, target)
      
    elif target < array[mid_index]:
      return binary_recur(array, start_index, mid_index - 1, target)

  print(mid_index)
