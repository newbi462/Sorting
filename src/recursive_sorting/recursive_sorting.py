# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    hold = []
    print(f"arrA:{arrA}")
    print(f"arrB:{arrB}")
    # TO-DO
    # print(elements)
    #hold = arrA
    kill = False
    for i in range(0, len(arrA)):
        #print(i)
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
        if i == len(arrA)-1:
            if len(arrB) > len(arrA):
                for foo in range(0, len(hold)):
                    if hold[foo] > arrB[i+1] and kill == False:
                        hold.insert(i, arrB[i+1])
                        kill = True
                    if foo == len(hold) - 1 and kill == False:
                        hold.append(arrB[i+1])

                #hold.append(arrB[i+1])
                #print("i ran")
        if len(hold) == len(merged_arr):
            run_loop = 0
            while run_loop < len(hold):
                for i in range(0, len(hold)-1):
                    #print(hold)
                    if hold[i+1] < hold[i]:
                        #print(f"move: {hold[i+1]}")
                        hold.insert(i, hold[i+1])
                        hold.pop(i+2)
                        run_loop = 0
                    else:
                        run_loop += 1


    print(f"Hold: {hold}")
    #return merged_arr
    #return sorted(hold)
    return hold


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) < 1:
        return arr
    else:
        if(len(arr) == 1):
            return arr

        else:
            find_middle = len(arr) // 2
            half1 = arr[:find_middle]
            half2 = arr[find_middle:]

            half1 = merge_sort(half1)
            half2 = merge_sort(half2)

            print(f"Merged: {merge( half1, half2 )}")
            return merge(half1, half2)

    #return arr


test = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort( test ))
print(sorted(test))

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
