class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0 
        zeros = 0
        ones = 0
        count = 0
        for r in range(len(s)):
            if s[r] == "0":
                zeros+=1
            else:
                ones +=1
            while zeros>k and ones>k:
                if s[l] == "0":
                    zeros -=1
                else:
                    ones -=1
                l+=1
            count += (r-l+1)
        return count 
        


        