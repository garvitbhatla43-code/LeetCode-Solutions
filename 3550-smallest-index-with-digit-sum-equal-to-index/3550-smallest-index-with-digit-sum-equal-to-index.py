class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0,len(nums)):
            digits=0
            while nums[i]>0:
                digits+=nums[i]%10
                nums[i]//=10
            if digits==i:
                return i
        return -1
                
    
            



        
        
            
            
        