class Solution:
    def linearSearch(self, nums, target):
        for i in range(len(nums)):
            if target == nums[i]:
                num = i
                return num
                break
    
        else:
            return -1            
