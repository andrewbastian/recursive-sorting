# TO-DO: Implement a recursive implementation of binary search

"""
The binary search tree labeling uniquely identities where each key
is located. Start at the root. Unless it contains the query key`x`,
proceed either left or right dependingupon whetherxoccurs before or
after the root key. This algorithm works becauseboth the left and
right subtrees of a binary search tree are themselves binary searchtrees.
This recursive structure yields the recursive search algorithm below:
"""


def binary_search(arr, target, start, end):
    # if (1 == NULL) return(NULL);
    # if arr is None:
    #     return None
    if start <= end:
        pivot = (start + end) // 2
    # if (1->item == x) retrun(1);
        if arr[pivot] == target:
            return pivot
        elif arr[pivot] > target:
        # if (x < 1 ->item)
        #   retrun( binary_search(1->left, x))
            return binary_search(arr, target, start, pivot-1)
        # else
        #   retrun( binary_search(1->right, x))
        else:
            return binary_search(arr, target, pivot-1, end)

    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    pass
