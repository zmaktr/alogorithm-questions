def search(array, target_item):
  for i in range(len(array)):
    if array[i] == target_item:
      print(i)

search([54,63,67,23], 23)