class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        repeated = set()
        for i in range(0,len(s)-9):
            sub = s[i:i+10]
            if sub in seen:
                repeated.add(sub)
            else:
                seen.add(sub)
        return list(repeated)
       