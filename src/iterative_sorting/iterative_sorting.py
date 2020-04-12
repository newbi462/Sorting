# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)): # - 1 keeps this from compleeting loop
        cur_index = i
        smallest_index = cur_index
        print(arr)
        # TO-DO: find next smallest element
        print(f"testing: {arr[i]}")
        if arr[i] < arr[i-1]:
            print(f"next smallest element: {arr[i]}")

        # (hint, can do in 3 loc)

        # TO-DO: swap
            kill = 0
            if arr[i] < arr[0] or i == 0: # 0 to prevent duping the first
                print("would swap all the way down")
                arr.insert(0, arr[i])
                arr.pop(i+1)
            else:
                while kill < len(arr):
                    if arr[i] > arr[i - kill]:
                        print(f"lower match: {arr[i - kill]}")
                        arr.insert(i - kill + 1, arr[i])
                        arr.pop(i+1)
                        kill = len(arr) + 5
                    #kill = len(arr) + 5
                    kill += 1

            if i == len(arr):
                pass

        """
        kill = 0
        if len(hold) > start_len:
            print("would swap all the way down")
            if hold[len(hold) - 1] < hold[0]:
                hold.insert(0, hold[len(hold) - 1])
                hold.pop(len(hold) - 1)
            else:
                while len(hold) > start_len and kill < len(hold):
                    print("dance it down")
                    if hold[len(hold) - 1] < hold[len(hold) - 2 - kill]:
                        print("match me")
                        if hold[len(hold) - 3 - kill] < hold[len(hold) - 2 - kill]:
                            hold.insert(len(hold) - 2 - kill, hold[len(hold) - 1])
                            hold.pop(len(hold) - 1)
                        #hold.pop(len(hold) - 1)
#                        if hold[len(hold) - 1] > hold[len(hold) - 4 - kill]:
#                            hold.pop(len(hold) - 1)
#                            kill = len(hold) + 2
#                        else:
#                            hold.pop(len(hold) - 2 - kill)

                    kill += 1
            #hold.insert(len(hold) - 2, hold[len(hold) - 1])
            #hold.pop(len(hold) - 1)
            #if hold[len(hold) - 2] < hold[len(hold) - 3] and len(hold) > 2:
            #    print("move me down")
            """

    #arr = hold
    return arr
"""
test = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(selection_sort( test ))
if len(test) > 0:
    print(test[len(test) - 1])
"""
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    run_loop = 0
    while run_loop < len(arr):
        for i in range(0, len(arr)-1):
            print(arr)
            if arr[i+1] < arr[i]:
                print(f"move: {arr[i+1]}")
                arr.insert(i, arr[i+1])
                arr.pop(i+2)
                run_loop = 0
            else:
                run_loop += 1

    return arr

test = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(bubble_sort( test ))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
