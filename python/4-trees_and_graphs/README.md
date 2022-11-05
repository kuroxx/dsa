# Trees

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


## Notes

- Recursive -> iterative
    - Push the parameters that usually go into a recursive function onto a stack
    - Note: if more than one recursive call inside and need to preserve the order of the calls, add them in the reverse order to the stack
    - Ref: [Stackoverflow](https://stackoverflow.com/questions/159590/way-to-go-from-recursion-to-iteration/159777#159777)