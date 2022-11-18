#The problem is that we want to reverse a T[] array in O(N) linear time complexity and we want the algorithm to be in-place as well - so no additional memory can be used!

#For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]


def reverse(array):
  start_index = 0  # O(1)
  end_index = len(array) - 1  # O(1)
  for i in range(len(array)):  # O(n)
    if start_index < end_index:  # O(n)
      array[start_index], array[end_index] = array[end_index], array[
        start_index]  # O(1)
      start_index += 1  # O(1)
      end_index -= 1  # O(1)
  print(array)

example_input_grid = [
    [" ", " ", "G", "W", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    ["W", "W", "W", " ", " "],
    [" ", " ", "G", " ", " "],
]