class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        max_len = 0
        hash_m = [0] * 26

        for r in range(0, len(s)):
            hash_m[ord(s[r]) - ord("a")] += 1

            while hash_m[ord(s[r]) - ord("a")] > 2:
                hash_m[ord(s[l]) - ord("a")] -= 1  # Changed 1 to l here
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len