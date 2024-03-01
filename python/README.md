# Python

## Syntax patterns

### Lists

1. Sorting
   - `sorted(list)` - return sorted in ascending and leave original list unchanged
   - `list.sort()` - sorts and mutates list in-place
   - `sorted()` - uses Timsort, O(n log n) average & worst-case complexity, O(n) space
2. List slicing
    - `iterable[start:stop:step]` - generic syntax
    - `list[i:j]` - return from index i, up to but not including index j
    - `list[i:]` - return from index i, up to end
    - `list[:j]` - return from start, up to index j
    - `list[::2]` - returns every other element from the list (indices: 0,2,4...)
    - `list[::-1]` - reverses the list (although built-in `list.reversed()` is faster, [it returns an iterator object whereas slicing creates an entirely new list via copying each element from original list](https://www.geeksforgeeks.org/python-reversed-vs-1-which-one-is-faster/)).   
3. List comprehension (i.e. Pythonic map and filter)
   - `expression for member in iterable [if conditon]` - generic syntax
   - i.e. `[i * 2 for i in list if i % 2 == 0]` - returns new list with every even element doubled from original list
   - Use this instead of `map` and `filter` for better readability
4. Range()
   - `range(start, stop, step)` - generic syntax
   - `range(n)` - for an iterable from 0 to n-1
   - `range(i,j)` - for an iterable from i up to but not including j
   - `range(0, 10, 2)` - [need to specify start and stop if you want to use step](https://stackoverflow.com/questions/15875188/the-strange-arguments-of-range)
5. Creating lists of size N
   - `list(range(N))` or `[*range(N)]` - use range and convert to list
   - `[element] * N ` i.e. `[0] * 5` - list of 5 zeroes
   - `[[0 for i in range(5)] for j in range(10)]` - for 2 or more dimensions
   - `[[0] * 5] * 10` - DONT DO THIS! (10 rows will just be references to the one row with 5 values so editing 1 row will change the other 9)

### Iteration

6. Enumerate
   - `for idx, ele in enumerate(list)` - to get index and element from an iterable
7. `do while` in Python
    - in other languages:
    ```
        do {
            # Write code here
        } while (condition)
    ```
    - in python:
    ```
        while True:
            # Write code here
            if condition:
                break
    ```
8. Generators
   - useful when looking up neighbors for a DFS or BFS problem with any graph-type structure
   - we can create a getNeighbors helper function that returns a generator
    ```
        def numIslands(grid) -> int:
            def getNeighbours(i, j):
                for di, dj in [(1,0), (-1,0), (0,1), (0, -1)]:
                    ni, nj = i + di, j +dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[i]):
                        yield ni, nj
            def dfs(i, j):
                grid[i][j] = "-1"
                for new_i, new_j in getNeighbour(i, j):
                    if grid[new_i][new_j] == "1":
                        dfs(new_i, new_j)
            islands = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == "1":
                        islands += 1
                        dfs(i, j)
            return islands
    ```

### Higher-order functions

9. List comprehension > `map` or `filter`
    ```
    list = list(range(10)) # [0, 1, ..., 9]

    # Not very pythonic
    evens = filter(lambda x : x % 2 == 0, list) # [0, 2, ..., 8]
    evens_doubled = map(lambda x : x*2, evens) # [0, 4, ..., 16]

    # Use list comprehensions
    evens_doubled = [x*2 for x in list if x % 2 == 0]
    ```
10. Use reduce with caution
    - `functools.reduce(function, iterable[, initializer])` - syntax
    - `sum` , `math.prod`, `all`, and `any` are more readable
    ```
    from functools import reduce
    nums = [1, 2, 3, 4, 5]
    bools = [True, False, True, False, True]

    # sum 
    reduce(lambda a, b: a + b, nums, 0) # 15

    # math.prod
    reduce(lambda a, b: a * b, nums, 1) # 120

    # min
    reduce(lambda a, b: a if a < b else b, nums) # 1

    # max 
    reduce(lambda a, b: a if a > b else b, nums) # 5

    # any 
    reduce(lambda a, b: a or b, bools) # true

    # all 
    reduce(lambda a, b: a and b, bools) # false
    ```
11. Using `zip`, `zip_longest`, and `zip_shortest`
    - ```zip``` - iterates through lists simultaneously (lists of unequal length truncates the output to shortest list)
    ```
    list_a = [1, 2, 3, 4]
    list_b = [10, 20, 30, 40]

    list_sum = [a + b for a, b in zip(list_a, list_b)]

    # OR 
    list_sum = []
    for a, b in zip(list_a, list_b):
        list_sum.append(a + b)

    print(list_sum) # [11, 22, 33, 44]
    ```
    - `zip_longest` from `itertools` library lets allows padding smaller list with a `fill_value` to `zip` as if they are equal lengths
    ```
    from itertools import zip_longest, zip_shortest

    short = [1, 2]
    long = [10, 20, 30, 40]

    zip_short = [a + b for a, b in zip(short, long)]
    print(zip_short) # [11, 22]

    zip_long = [a + b for a, b in zip_longest(short, long, fill_value=0)]
    print(zip_long) # [11, 22, 30, 40]
    ```

### Data structures

12. Python dictionary methods
    - `key in my_dict` - check if key is in dict
    - `my_dict[key]` - access item in dict and returns `keyError` if key isn't in dict
      - `my_dict.get(key, default_value=None)` - to avoid error and return default val instead
    - `del my_dict[key]` - remove key from dict if you know key exists
      - `my_dict.pop(key, None)` - returns None if key is not in my_dict
    - `my_dict.setdefault(key, default_value)` - returns current val for key if exists in my_dict else default val
      - `setdefault` - very useful for counting elements i.e. `counts[element] = counts.setfeault(element, 0) + 1`
    - `my_dict.keys()`, `my_dict.values()`, and `my_dict.items()` - returns a list of keys, values and tuples of (key, value) from my_dict respectively
    - create new dict using dictionary comprehensions:
    ```
    my_baskset = {'apple': 2, 'banana': 3, 'starfruit': 1}
    double_my_basket = {k:v*2 for (k, v) in my_basket.items()}
    print(double_my_basket) # {'apple': 4, 'banana': 6, 'starfruit': 2}
    ```
    - `|` and `|=` - operators to merge or update keys and values in sets or dictionaries (only available for dict as of Python 3.9)
    ```
    a = {1, 2, 3} # New set
    a += {4} # Returns a 'TypeError'
    a |= {4} # {1, 2, 3, 4}
    ```
13. Using OrderedDict
    - `OrderedDict` - not used frequently but makes implementing LRU Cache almost trivial
      - effectively a dictionary combined with a doubly linked-list for ordering
    - `.popItem()` - remove items in LIFO order 
      - `.popItem(last=False)` - remove items in FIFO order
    - `.move_to_end(item_key)` - moves item to end of dict
      - `.move_to_end(item_key, last=False)` - move item to beginning
14. Using collections.Counter
    - `collections.Counter` - is a subclass of `dict` (frequently used in interview questions involving adding counts to a hashmap)
    ```
    things = ['a', 'a', 'b', 'c', 'b', 'b']
    counts = collections.Counter(things)
    print(counts) # Counter({'b': 3, 'a': 2, 'c': 1})
    ```


## Study resources

- [https://towardsdatascience.com/19-helpful-python-syntax-patterns-for-coding-interviews-3704c15b758f](https://towardsdatascience.com/19-helpful-python-syntax-patterns-for-coding-interviews-3704c15b758f)
- [https://medium.com/@ratulsaha/preparing-for-programming-interview-as-a-phd-student-with-python-5f8af8b40d5f](https://medium.com/@ratulsaha/preparing-for-programming-interview-as-a-phd-student-with-python-5f8af8b40d5f)