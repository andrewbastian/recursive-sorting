# Day 2

## Space Complexity - Defined by the shape of the output

## Space = Memory

- As input size increases, how much *more* space do we take up?

    > not counting the original memory taken up.

- Aka, as the function runs, does it put more stuff into memory?

```python
arr = [1, 2, 3, 4, 5]

second_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def counter(arr):  # `second_arr` will take twice as long
    total = 0

    for thing in arr:
        total += 1

    return total
```

- Time Complexity: Linear

    > Double input, double steps

    > O(n)

- Space Complexity:

    > DOUBLE INPUT, NO EXTRA Space

    > Constant

    > O(1)

```python
arr = [1, 2, 3, 4, 5]


def dupliate(arr):
    copy_arr = []

    for thing in arr:
        copy_arr.append(thing)

    return copy_arr
```

- Time Complexity

    > 1 + len(n)

    > O(n)

- Space Complexity

    > Linear - O(n)

```python
def times_table(n):
    times_table = []

    for i in range(n):
        row = []

        for j in range(n):
            row.append(i * j)

        times_table.append(row)

    return times_table


table = times_table(5)  # 5x5 matrix = 25
table = times_table(10)  # 10x10 matrix = 100
```

- Time Complexity

    > O(n^2)

- Space Complexity

    > O(n^2)


- Often time and space complexity are the same

- We oftern trade space for time


### Matrix:

_Pandas_ - python library

```
matrix =    [[1, 2, 3, 4, 5],
             [2, 3, 4, 5, 6]]
```

## Recursive Sorting:

- What do we need?

    > Base Case

    > Function that calls itself

    > Progress toward base case

- Used because:

    > Elegant, terse, few lines of code

- Divide and conquer:

    > Divide into subproblems that have the same 'shape' as the parent problem

    > Solve subproblems

    > Combine your solutions, the overall problem is solved

Post master example:

- If finding most efficent route to deliver all mail at once?

- Divide into subreagions

- Find most efficent route in each supregion

- Delivered all the mail!


sorting:

- Break up the array

- Sort each piece

- Put them back together again

```python
arr = [5, 7, 3, 1, 2, 9, 0, 8, 4, 6]

pivot = arr[0]

#           [3, 1, 2, 0, 4] [5] [7, 9, 8, 6]
#   [3, 1, 2, 0, 4]
#   pivot = arr[0]
#          [0,1,2] [3] [4]


def partition(arr):
    # chose Piviot
    pivot = arr[0]
    left = []
    right = []
    # partion around the piviot
    for num in arr:
        if num < pivot:
            left.append(num)
        if num > pivot:
            right.append(num)
    # mult returns are wrapped in tuple
    return left, pivot, right


# Quick Sort
def quicksort(arr):
    if len(arr) == 0:
        return arr

    # recure on left and right side
    left, right, piviot = partition(arr)

    return quicksort(left) + [piviot] + quicksort(right)


print(quicksort([1, 4, 5, 6]))
```

- `RecursionError: maximum recursion depth exceeded in comparison`

    > Python has run out of memory