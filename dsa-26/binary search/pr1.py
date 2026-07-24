arr = [2, 5, 8, 12, 16, 23, 38]
target = 23

def binary_search(arr, target):
    start = 0
    end = len(arr)-1
    
    
    
    while(start<=end):
        mid = start + (end-start)//2
        if(target<arr[mid]):
            end = mid -1
        elif(target>arr[mid]):
            start = mid+1
        else:
            return mid
    return -1
    
print(binary_search(arr, 23))  
    
    
        