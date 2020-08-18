# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # # starting at the beginning of `a` and `b`
    # a_index = 0
    # b_index = 0

    # while a_index < len(arrA) or b_index < len(b_index):
    # # compare the next value of each
    #     if a_index >= len(arrA):
    #         # add smallest to `merged_arr`
    #         while b_index <= len(b_index) -1:
    #             merged_arr[len(arrA) + b_index]
    #             b_index += 1
    #         return merged_arr
    #     elif b_index >= len(arrB):
    #         while a_index <= len(arrA) -1:
    #             merged_arr[len(arrB) + a_index]
    #             a_index += 1
    #         return merged_arr
    #     else:
    #         if arrA[a_index] <= arrB[b_index]:
    #             merged_arr[a_index + b_index] = arrA[a_index]
    #             a_index += 1
    #         else:
    #             merged_arr[a_index + b_index] = arrB[b_index]
    #             b_index += 1

    # return merged_arr

    a_index = 0
    b_index = 0
    curr = 0

    while a_index < len(arrA) and b_index < len(arrB):
        if arrA[a_index] < arrB[b_index]:
            merged_arr[curr] = arrA[a_index]
            curr += 1
            a_index += 1
        else:
            merged_arr[curr] = arrB[b_index]
            curr += 1
            b_index += 1
    while a_index < len(arrA):
        merged_arr[curr] = arrA[a_index]
        curr += 1
        a_index += 1
    while b_index < len(arrB):
        merged_arr[curr] = arrB[b_index]
        curr += 1
        b_index += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # pass
    # Base Case
    if len(arr) <= 1:
        return arr

    else:
        stop = len(arr)
        pivot = round(len(arr) // 2)
        arrA = merge_sort(arr[0:pivot])
        arrB = merge_sort(arr[pivot:stop])
        arr = merge(arrA, arrB)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
