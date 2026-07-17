from turtle import right


nums = [2,0,2,1,1,0]

def dutch_nation_flag_algo(nums):
    low, mid, high = 0, 0, len(nums)-1
    while mid <= high:
        if nums[mid]==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    print(nums)


## overwriting apporach 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        """
        Do not return anything, modify nums in-place instead.
        """

        count_of_zero = 0
        count_of_one=0
        count_of_two=0

        for i in nums:
            if i==0:
                count_of_zero+=1
            elif i==1:
                count_of_one+=1
            else:
                count_of_two+=1

#started overwriting in array        
        
        for j in range(0,count_of_zero):
            nums[j]=0
            j+=1
        for j in range(count_of_zero,count_of_zero+count_of_one):
            nums[j]=1
            j+=1
        for j in range(count_of_zero+count_of_one,len(nums)):
            nums[j]=2
            j+=1    
              
        return nums        
