# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    hold = []
    print(arrA)
    print(arrB)
    # TO-DO
    # print(elements)
    for i in range(0, len(arrA)):
        if arrA[i] < arrB[i]:
            hold.append(arrA[i])
            hold.append(arrB[i])
            #merged_arr.pop(i+2)
            #merged_arr.pop(i+3)
        if arrA[i] > arrB[i]:
            hold.append(arrB[i])
            hold.append(arrA[i])
            #merged_arr.pop(i+2)
            #merged_arr.pop(i+3)

    #return merged_arr
    return hold


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    print(arr)
    find_middle = len(arr) // 2 # // removes the float
    #print(find_middle)
    arrA = arr[:find_middle] # : slices left rightr
    arrB = arr[find_middle:]
    print(f"Merged: {merge( arrA, arrB )}")

    return arr


test = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort( test ))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
