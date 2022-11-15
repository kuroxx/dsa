# Python

## Syntax patterns

### Lists

1. Sorting
   - ```sorted(list)``` - return sorted in ascending and leave original list unchanged
   - ```list.sort()``` - sorts and mutates list in-place
   - ```sorted()``` - uses Timsort, O(n log n) average & worst-case complexity, O(n) space
2. List slicing
    - ```iterable[start:stop:step]``` - generic syntax
    - ```list[i:j]``` - return from index i, up to but not including index j
    - ```list[i:]``` - return from index i, up to end
    - ```list[:j]``` - return from start, up to index j
    - ```list[::2]``` - returns every other element from the list (indices: 0,2,4...)
    - ```list[::-1]``` - reverses the list (although built-in `list.reversed()` is faster, [it returns an iterator object whereas slicing creates an entirely new list via copying each element from original list](https://www.geeksforgeeks.org/python-reversed-vs-1-which-one-is-faster/)).   
3. List comprehension (i.e. Pythonic map and filter)
   - ```expression for member in iterable [if conditon]``` - generic syntax
   - i.e. ```[i * 2 for i in list if i % 2 == 0]``` - returns new list with every even element doubled from original list
   - Use this instead of `map` and `filter` for better readability
4. Range()
   - ```range(start, stop, step)``` - generic syntax
   - ```range(n)``` - for an iterable from 0 to n-1
   - ```range(i,j)``` - for an iterable from i up to but not including j
   - ```range(0, 10, 2)``` - [need to specify start and stop if you want to use step](https://stackoverflow.com/questions/15875188/the-strange-arguments-of-range)
5. Creating lists of size N
   - ```list(range(N))``` or ```[*range(N)]``` - use range and convert to list
   - ```[element] * N ``` i.e. ```[0] * 5``` - list of 5 zeroes
   - ```[[0 for i in range(5)] for j in range(10)]``` - for 2 or more dimensions. 
   - ```[[0] * 5] * 10``` - DONT DO THIS! (10 rows will just be references to the one row with 5 values so editing 1 row will change the other 9).


## Study resources

- [https://towardsdatascience.com/19-helpful-python-syntax-patterns-for-coding-interviews-3704c15b758f](https://towardsdatascience.com/19-helpful-python-syntax-patterns-for-coding-interviews-3704c15b758f)
- [https://medium.com/@ratulsaha/preparing-for-programming-interview-as-a-phd-student-with-python-5f8af8b40d5f](https://medium.com/@ratulsaha/preparing-for-programming-interview-as-a-phd-student-with-python-5f8af8b40d5f)