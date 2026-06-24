class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        p=sum(nums)
        for i in range(1,len(nums)):
            left_sum=sum(nums[:i])
            right_sum=p-left_sum
            if (left_sum-right_sum)%2==0:
                count+=1
        return count
