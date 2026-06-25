class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        popl={}
        nums.sort()
        for i in range(0,len(nums)):
            if nums[i] in popl:
                popl[nums[i]]+=1
            else:
                popl[nums[i]]=1
        nums.sort(key=lambda x: (popl[x], -x)) 
        return nums
        