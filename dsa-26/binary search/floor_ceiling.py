class Solution:
    def getFloorAndCeil(self, nums, x):
        start = 0
        end = len(nums)-1
 
        ceil = -1
        floor = -1
    
        while(start <= end):
            mid = start +(end-start)//2
            if x == nums[mid]:
                return nums[mid], nums[mid]
            elif nums[mid]> x:
                ceil = nums[mid]
                end = mid -1
            else:
                floor = nums[mid]
                start = mid+1
        return floor,ceil      