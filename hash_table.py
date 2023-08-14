"""
Task:
Write a basic HashTable(dictionary) class that can be used to insert, retrive and delete key:value pairs
"""

class HashTable:
  def __init__(self):
    # based on the load factor we may change the size of the HashTable
    # load factor = total keys stored in HashTable / size of Hashtable
    # in python when load factor > 0.66 python dynamically resizes the dictionary
    self.capacity = 10
    self.keys = [None] * self.capacity
    self.values = [None] * self.capacity

  def hash_function(self, key):
    hash_sum = 0
    for letter in key:
      # use ord() to calcualte ascii value for a letter
      hash_sum += ord(letter)
    return hash_sum % self.capacity

  def insert(self, key, value):
    index = self.hash_function(key)
    # update new key
    if self.keys[index] == key:
      self.values[index] = value
    # enter new key
    elif self.keys[index] is None:
      self.keys[index] = key
      self.values[index] = value
    # duplicate keys
    elif self.keys[index] is not None and self.keys[index] != key:
      # solutions 1)chaining 2)linear-probing
      # use linear probing (find the next index to store)
      while self.keys[index] is None:
        index = (index + 1) % self.capacity
      # enter new key
      self.keys[index] = key
      self.values[index] = value 
  
  def get(self, key):
    index = self.hash_function(key)
    # return key if found in index
    if self.keys[index] == key:
      return self.values[index]
    # key not inserted into the hashtable
    elif self.keys[index] is None:
      return None
    # collission issue find the key in the next index
    elif self.keys[index] != key:
      while self.keys[index] == key:
        index = (index + 1) % self.capacity
      if self.keys[index] == key:
        return self.values[index]
      else:
        return None
        

    
i = HashTable()
i.insert('adam', 23)
i.insert('kevin', 85)
i.insert('danny', 56)
i.insert('adam', 65)

print(i.get('Anna'))
print(i.get('adam'))


