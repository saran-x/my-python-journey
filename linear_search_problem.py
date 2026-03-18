# printing a target value previous and next value 

# function of the first and last index identify

def first_last(arr,target):
    
    first = -1
    last = -1

    for i in range(0,len(arr)):
    
        if target in arr:

            if arr[i] == target:
                if  i + 1 < len(arr):
                    last = i + 1
            
            if last == -1:
                first += 1
    
    print(first,last)       
                       




# testing function
def testing():
    
    print("case 1")
    arr1 = [1,2,3,5]
    first_last(arr1,1)

    print("case 2") 
    arr2 = [1, 2, 3, 4, 5]
    first_last(arr2, 6)

    print("case 3")
    arr3 = [1, 2, 3, 4, 5]
    first_last(arr3, 3) 
    
    print("case 4")
    arr4 = [5, 5, 5, 5, 5]
    first_last(arr4, 5) 
    
    print("case 5")
    arr5 = [1, 1, 2, 3, 4, 4]
    first_last(arr5, 1) 
    first_last(arr5, 4)

testing()
