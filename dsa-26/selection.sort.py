nums = [5,7,8,4,1,6,9,2]

def sel_sort(nums):
    n = len(nums)
    for i in range(0,n):
        mid_index = i
        for j in range(i+1,n):
            if nums[j]< nums[mid_index]:
                mid_index = j
            
        nums[i],nums[mid_index]=  nums[mid_index], nums[i]
    return nums

print(sel_sort(nums))
            

        #    Descinding order



def sel_sort(nums):
    n = len(nums)
    for i in range(0,n):
        mid_index = i
        for j in range(i+1,n):
            if nums[j]> nums[mid_index]:
                mid_index = j
            
        nums[i],nums[mid_index]=  nums[mid_index], nums[i]
    return nums

print(sel_sort(nums))
        
                        
           
           