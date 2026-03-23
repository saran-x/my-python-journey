# Insertion sort

def insertion_sort(arr):
   
    for i in range(len(arr)):

        key = arr[i]
        j = i - 1
        
        # swapping a value
        while j >= 0 and arr[j] > key:
            arr[j+1 ] = arr[j]
            j -= 1
        arr[j+1] = key
         
        
    return arr
           

        

def testing():
    # test case
    arr1 = [9,6,4,2,1]
    value = insertion_sort(arr1)
    print(value)


testing()
