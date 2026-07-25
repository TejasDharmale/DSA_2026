arr = [38, 23, 16, 12, 8, 5, 2]
target = 8

def order_agnostic(arr, target):
    start = 0
    end = len(arr)-1
    
    is_asc = arr[start]<arr[end]
    
    while(start <=end):
        mid = start +(end-start)//2
        if target ==arr[mid]:
            return mid
            
        if is_asc:
            if target>arr[mid]:
                start = mid+1
            else:
                end = mid -1
        else:
            if target>arr[mid]:
                end = mid -1
            else:
                start = mid+1
    return -1
print(order_agnostic(arr, 8))    
            