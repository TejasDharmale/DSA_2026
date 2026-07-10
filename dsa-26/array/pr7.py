class Solution:
    def rotateArray(self, nums, k: int) -> None:
        n = len(nums)
        k 

        for i in range(k):
            j= nums[0]
            for i in range(1,n):
                nums[i-1]=nums[i]
            nums[-1]=j 
        return nums      
