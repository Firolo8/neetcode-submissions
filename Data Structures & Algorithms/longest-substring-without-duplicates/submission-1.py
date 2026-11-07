class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in charSet: #while dupe remains in set
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r]) #after remove dupes
            result = max(result, r - l + 1) #potentially making it bigger if window size is greater than what it is now. 
        return result