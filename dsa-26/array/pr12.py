class Solution:
    def singleNumber(self, nums):
        #your code goes here
        res = sorted(nums)
        n = len(res)

        single = None
        if single is None:
            single = res[n-1]

        for i in range(0,n-1,2):
            if res[i]!=res[i+1]:
                single = res[i]
        return single          