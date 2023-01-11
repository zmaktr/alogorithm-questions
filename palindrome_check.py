def string_check(string):
  
  first_index = 0
  last_index = len(string) - 1

  while first_index <= last_index:
    if string[first_index] == string[last_index]:
      first_index += 1
      last_index -= 1
    else:
      return print("this is not a palindrome word")
  
  return print("this is a palindrome word")

# quick solution
# if string == string[::-1]:
#  return print("this is a palindrome word")
# else:
#  return print("this is not a palindrome word")

string_check('radar')
  