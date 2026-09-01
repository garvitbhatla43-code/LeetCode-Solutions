class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l=0
        max_len=0
        for r in range(len(nums)):
            while nums[r]-nums[l] > 1:
                l+=1
            if nums[r] - nums[l] == 1:
                max_len = max( max_len , r-l+1)
        return max_len

       