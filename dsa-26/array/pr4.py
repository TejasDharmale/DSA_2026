class Solution:
    def unionArray(self, nums1, nums2):
        a = set(nums1)
        b = set(nums2)
        res  = a|b
        return list(res)