def sort_insertion(array):
  # i1 = current iteration idex of list 1 (sorted)
  # i2 = current iteration idex of list 2 (un-sorted)
  i1 = 0
  for i2 in range(1,len(array)):
    i1 = i2 - 1
    while array[i1] > array[i2] and i1 >= 0:
      array[i1], array[i2] = array[i2], array[i1]
      i1 -= 1
      i2 -= 1
    
  return print(array)