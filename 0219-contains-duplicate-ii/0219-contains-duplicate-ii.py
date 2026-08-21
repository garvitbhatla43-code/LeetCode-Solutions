class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        check=set()
        for i in range(0,len(nums)):
            if nums[i] in check:
                return True
            check.add(nums[i])
            if len(check)> k:
                check.remove(nums[i-k])
        return False
            

        
        