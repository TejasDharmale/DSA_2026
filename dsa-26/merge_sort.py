class Solution:
    def merge_arr(self,left_half,right_half):    # merge two sorted arrays
        result =[]   # result array to store the merged array
        i,j=0,0 # initialize the pointers to the start of the arrays
        n,m = len(left_half), len(right_half)
        while i<n and j<m:  # while both arrays are not empty
            if left_half[i]<right_half[j]:
                result.append(left_half[i])  # append the smaller element to the result array
                i+=1 # increment the pointer of the left_half
            else:
                result.append(right_half[j])  # append the smaller element to the result array
                j+=1 # increment the pointer of the right_half
            if i<n:  # if left_half is not empty
                while i<n:
                    result.append(left_half[i])
                    i+=1
            else:
                while j<m: # if right_half is not empty 
                    result.append(right_half[j])
                    j+=1                
            return result            # return the merged array

    def mergeSort(self, nums):
        if len(nums)<=1:  # if the array is empty or has one element, return the array
            return nums
        mid = len(nums)//2  # find the middle index
        left_half = nums[:mid]  # split the array into two halves
        right_half = nums[mid:]  # split the array into two halves
        left_half = self.mergeSort(left_half)  # sort the left half
        right_half= self.mergeSort(right_half)  # sort the right half
        return self.merge_arr(left_half,right_half)  # merge the two sorted arrays

