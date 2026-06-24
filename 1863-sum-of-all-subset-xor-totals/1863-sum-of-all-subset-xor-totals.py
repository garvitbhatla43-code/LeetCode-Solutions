class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bits = 0
        for num in nums:
            bits |= num
        return bits * (1 << (len(nums) - 1))