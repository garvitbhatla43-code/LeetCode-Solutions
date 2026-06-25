class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        a=nums[0]
        p=nums[1:n]
        p.sort()
        return a+p[0]+p[1]
       
        