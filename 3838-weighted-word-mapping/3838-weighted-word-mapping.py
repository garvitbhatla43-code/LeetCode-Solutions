class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        res=""
        for i in words:
            ww=0
            for j in i:
                char_index= ord(j)-97
                ww+=weights[char_index]
            remainder=ww%26
            mappend_char=chr(122-remainder)
            res+=mappend_char
        return res


