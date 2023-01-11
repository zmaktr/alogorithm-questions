def sort_array(array):
  max_index = len(array) - 1
  
  while max_index >= 0:
    for i in range(max_index):
      if array[i] > array[i + 1] and i < max_index:
        array[i], array[i + 1] = array[i + 1], array[i]
      else:
        pass
    
    max_index -= 1
  return print(array)

sort_array([4,6,3,4,7,9,25,36])