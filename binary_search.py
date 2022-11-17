def binary_itr(array, target):
  start_index = 0 
  end_index = len(array) - 1
  mid_index = (start_index + end_index) // 2
  if target >= array[mid_index]:
    while target != array[mid_index]:
      start_index = mid_index + 1
      mid_index = (start_index + end_index) // 2
    print(mid_index)
  elif target <= array[mid_index]:
    while target != array[mid_index]:
      end_index = mid_index - 1
      mid_index = (start_index + end_index) // 2
    print(mid_index)