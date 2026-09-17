class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
       
        for j in range(0,k):
            last= nums[-1]
            for i in range(n-2,-1,-1):
                nums[i+1]=nums[i]
            nums[0]=last   
        return nums        

        