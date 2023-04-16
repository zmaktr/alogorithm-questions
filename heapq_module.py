import heapq
# heapq is implementation of min heap using underlying list data structure

# methods
# heapq.heappush(heap, item)
# Push the value item onto the heap, maintaining the heap invariant.
# heapq.heappop(heap)
# Pop and return the smallest item from the heap
# heapq.heapify(x)
# Transform list x into a heap, in-place, in linear time

# example 1
h = []

# push items to heap
heapq.heappush(h, 5)
heapq.heappush(h, 6)
heapq.heappush(h, 8)
heapq.heappush(h, -2)
heapq.heappush(h, 3)
heapq.heappush(h, 5)

print('first example',h)

# example 2
h = [5, 6, 8, -2, 3, 5]
heapq.heapify(h)

print('second example', h)

# example 3
h = [5, 6, 8, -2, 3, 5]
heapq.heapify(h)

print('third example')
while h:
  print(heapq.heappop(h))