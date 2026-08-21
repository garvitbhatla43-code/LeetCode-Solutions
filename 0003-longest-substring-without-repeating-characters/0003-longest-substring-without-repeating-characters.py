class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charS=set()
        l=0
        res=0
        for i in range(0,len(s)):
            while s[i] in charS:
                charS.remove(s[l])
                l+=1
            charS.add(s[i])
            res=max(res ,i-l+1)
        return res
            

        