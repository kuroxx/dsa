## heapq

- `heapq` > `queue.PriorityQueue` because it's more flexible
- https://docs.python.org/3/library/heapq.html
- `heapify` is in-place, `heapify(list)` will turn `list` into a heap
- `heapq` only supports min-heap (for max-heap, multiply all values by -1 before heapifying and multiply by -1 after popping)
- To create a heap for objects, add them as a tuple with `(priority, counter, object)`. 
  - `counter` is a unique number to break priority ties (otherwise you’ll get an error). Start counter at 0 and increment whenever pushing to heap
