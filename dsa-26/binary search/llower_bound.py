class Solution:
    def lowerBound(self, nums, x):
        start = 0
        end = len(nums)-1
        ans = -1
    
    
    
        while(start<=end):
            mid = start + (end-start)//2
            

            if(x <= nums[mid]):
                ans = mid
                end = mid -1
            else:
            
                start = mid+1
            
        return ans