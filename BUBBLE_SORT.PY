def bubblesort(arr):

    arr_len = len(arr)
    
    for i in range(arr_len - 0):

        checkVal = 1

        for j in range(0,arr_len - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                checkVal = 1 
                print(arr)

        if checkVal == 0:
            break

    return arr
    
unsorted = ["D", "S", "M", "R", "A", "E"]
sorted = bubblesort(unsorted)   
print(sorted)