nums =  [1, 1, 1, 2, 1, 2]
m = nums.sort()
count = 1
n= len(nums)

for i in range(0,n-1):
    if nums[i]!=nums[i+1]:
        count =1
    else:
        count+=1
    
    if count>n/2:
        major = nums[i]
print(major)  
        
#time complexity: O(nlogn)
#space complexity: O(1)

#more efficient approach: moore's voting algorithm
class Solution:
    def majorityElement(self, nums):
        freq = 0
        ans = 0
        n= len(nums)

        for i in range(0,n):
            if freq ==0:
                ans = nums[i]
            if ans == nums[i]:
                freq+=1
            else:
                freq-=1
        return ans