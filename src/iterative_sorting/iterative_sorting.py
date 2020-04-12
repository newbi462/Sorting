# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    hold = [arr[0]]
    loops = 0
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        start_len = len(hold)
        print(f"hold:{hold}")
        #print(f"len:{len(hold)}")
        # TO-DO: find next smallest element
        #print(i)
        #print(len(hold))
        if hold[len(hold) - 1] > arr[cur_index]:
            hold.append(arr[cur_index])

        print(f"len 2:{len(hold)}")

        # (hint, can do in 3 loc)

        # TO-DO: swap
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



    #arr = hold
    return arr

test = [7,4,1,8,0,5,2,9,6,3]
print(selection_sort( test ))
if len(test) > 0:
    print(test[len(test) - 1])

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
