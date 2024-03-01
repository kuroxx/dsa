# String

## String builder

- String is immutable
- Linear: ```string += c```
- Constant: ```stringBuilder.append(c)```
- StringBuilder: O(n) (Java, C#, etc.)
- String.join(): O(n) (Python)

# Coding patterns

## Sliding window O(n)

Aims to reduce the use of nested loop and replace it with a single loop, thereby reducing the time complexity.

The general use of Sliding window technique can be demonstrated as following:

1. Find the size of window required 
2. Compute the result for 1st window, i.e. from start of data structure
3. Then use a loop to slide the window by 1, and keep computing the result window by window.

We can use this technique to find max/min k-subarray, XOR, product, sum, etc. 