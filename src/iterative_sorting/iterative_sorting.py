# TO-DO: Complete the selection_sort() function below

# TO-DO: find next smallest element
# (hint, can do in 3 loc)
# arr1 = [3, 2, 7, 8, 5, 9, 6]

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

       # compare i[0] with each i of array.
        for x in range(cur_index, len(arr)):
        # compare cur_index to i
            if arr[x] < arr[smallest_index]:
        # if any i in array is smaller than i[0], assign cur_index to smallest_index
                smallest_index = x
        # swap and make new_smallest = smallest
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # Make a flag to show if swaps have occured
    swaps_occurred = True
    # Run until you get through a loop without any swaps
    while swaps_occurred:
        swaps_occurred = False
        # For each element in the array...
        for i in range(len(arr) - 1):
        #check the index to the right
            if arr[i] > arr[i + 1]:
                # if the index on the right is smaller, swap
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                #if there was a swap, flagged true
                swaps_occurred = True


    return arr


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):
#
#     return arr





# My attempts

        # i += 1
        # repeat

        # if cur_index >= i:
        #     cur_index += 1
        #     print(f"current index: [{cur_index}] and current value {arr[cur_index]}")

        #     if arr[cur_index] < arr[smallest_index]:
        #         # print(f"current index value: {arr[cur_index]} and smallest value: {arr[smallest_index]}")

        #         new_smallest = cur_index
        #         # print(f"current value: {arr[cur_index]} and new smallest value: {arr[new_smallest]}")

        #         # print(f"Before swap: {arr[new_smallest]}, {i}")
        #         new_smallest, smallest_index = smallest_index, new_smallest
        #         # print(f"After swap: {arr[new_smallest]}, {i}")
        #         print(f"Array: {arr1}")

        #         cur_index += 1
        #         print(f"current: [{cur_index}]")
        #         print("ONE LOOP COMPLETE")
        # else:
        #     cur_index += 1
        #     print(f"current from else [{cur_index}]")
        # #     print(f"We hit else...{cur_index}")
        #     # TO-DO: swap

        
        # print(arr1)