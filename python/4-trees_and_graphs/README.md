# Trees

## Implementing a Tree

- No helpful Tree data structure in Python's standard library, implement your own.
- For a binary tree, create a Node class with left and right Node attributes. Make sure to keep track of the “head” Node in your code.
- For a non-binary tree, use an array or a dictionary for the children. If you don’t expect children with duplicate values and want O(1) lookup, a dictionary might be better.

```
# Binary Tree Node
class Node:
  def __init__(value):
    self.value = value
    self.left = None
    self.right = None

# Non-Binary Tree Node
class Node:
  def __init__(value):
    self.value = value
    self.children = [] # or self.children = {} for dict
```

## Tree Traversal

| Depth first | Breadth first |
|---|---|
| 1. Pre-order  | 1. Level-order | 
| 2. In-order   | | 
| 3. Post-order | | 

### Depth first

1. Pre-order O(n) / Top-down
    - Visit node
    - Traverse left
    - Traverse right

2. In-order O(n)
    - Traverse left
    - Vivist node
    - Traverse right

3. Post-order O(n) / Bottom-up
    - Traverse left
    - Traverse right
    - Visit node

### Breadth first

1. Level-order O(n)
    -  Traverse level by level, left to right

## DFS vs BFS

| Parameters | DFS | BFS |
|---|---|---|
| Data structure  | Stack (FIFO) |  Queue (LIFO) | 
| Backtracking  | Recursive algo that uses the idea of backtracking |  No such concept | 
| Memory  | Less memory |  More memory |
| Applications  | Acylic graphs, topological order, etc. | Bipartite graphs, shorted path, etc. |
| When to use?  | Target is far from source |  Targer is close to source | 

## Notes

- Recursive -> iterative
    - Push the parameters that usually go into a recursive function onto a stack
    - Note: if more than one recursive call inside and need to preserve the order of the calls, add them in the reverse order to the stack
    - Ref: [Stackoverflow](https://stackoverflow.com/questions/159590/way-to-go-from-recursion-to-iteration/159777#159777)