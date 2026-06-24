class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        ans=[]
        for w in words:
            Sum=sum( weights[ord(c)-97] for c in w)
            ans.append(chr(97+25-Sum%26))
        return "".join(ans)