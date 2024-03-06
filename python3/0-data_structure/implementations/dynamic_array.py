# https://neetcode.io/problems/dynamicArray

# Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

# Dynamic Array implementation
# Note: Python lists are dynamic arrays by default,
# but this is an example of what's going on under the hood.

import unittest

class DynamicArray:
    
    # O(n) - n = capcity
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * capacity

    # O(1)
    # Get value at i-th index 
    def get(self, i: int) -> int:
        if i >= self.length:
            return -1
        return self.arr[i]

    # O(1) 
    # Set n at i-th index
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    # O(1) Avg case / Amortized
    # O(n) Worst case
    # Insert n in the last position of the array
    def pushback(self, n: int) -> None:
        if self.length == self.capacity: 
            self.resize()

        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1

    # O(1)
    # Remove the last element in the array
    def popback(self) -> int:
        if self.length > 0: 
            # soft delete last element
            self.length -= 1
        # return popped element
        return self.arr[self.length]

    # O(n)
    def resize(self) -> None:
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        # copy elements to new_arr
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    # O(1)
    def getSize(self) -> int:
        return self.length
    
    # O(1)
    def getCapacity(self) -> int:
        return self.capacity


# Example 1
#    Input:
#    ["Array", 1, "getSize", "getCapacity"]
#    Output:
#    [null, 0, 1]

# Example 2
#   Input:
#   ["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]
#   Output:
#   [null, null, 1, null, 2]

# Example 3 
#   Input:
#   ["Array", 1, "getSize", "getCapacity", "pushback", 1, "getSize", "getCapacity", "pushback", 2, "getSize", "getCapacity", "get", 1, "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"]
#   Output:
#   [null, 0, 1, null, 1, 1, null, 2, 2, 2, null, 3, 3, 1, 2]


class TestDynamicArray(unittest.TestCase):
    def setUp(self):
        self.dyn_array = DynamicArray(5)

    def test_initialization(self):
        self.assertEqual(self.dyn_array.getSize(), 0)
        self.assertEqual(self.dyn_array.getCapacity(), 5)

    def test_pushback_and_get(self):
        self.dyn_array.pushback(1)
        self.assertEqual(self.dyn_array.get(0), 1)
        self.assertEqual(self.dyn_array.getSize(), 1)

    def test_set(self):
        self.dyn_array.pushback(1)
        self.dyn_array.set(0, 5)
        self.assertEqual(self.dyn_array.get(0), 5)

    def test_popback(self):
        self.dyn_array.pushback(1)
        popped = self.dyn_array.popback()
        self.assertEqual(popped, 1)
        self.assertEqual(self.dyn_array.getSize(), 0)

    def test_resize(self):
        for i in range(6):
            self.dyn_array.pushback(i)
        self.assertGreaterEqual(self.dyn_array.getCapacity(), 6)

    def test_boundary_conditions(self):
        out_of_bounds_index = 100
        self.assertEqual(self.dyn_array.get(out_of_bounds_index), -1)

if __name__ == '__main__':
    unittest.main()
