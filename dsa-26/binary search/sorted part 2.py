class Solution:
    def search(self, nums, k):
        start = 0
        end = len(nums)-1
 
        while (start<=end):
            mid = start +(end-start)//2

            if k==nums[mid]:
                return True
            
            if nums[mid]==nums[start]==nums[end]:
                start +=1
                end -=1
                continue
            elif nums[start] <= nums[mid]:
                if nums[start] <= k < nums[mid]:
                    end = mid - 1
                else:
            
                    start = mid +1
        

            else:
                if nums[mid] < k <= nums[end]:
                    start = mid+1
                else:
                    end = mid-1
            
        return False