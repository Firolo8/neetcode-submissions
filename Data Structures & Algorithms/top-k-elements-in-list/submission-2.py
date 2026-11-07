class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #hash to count occurance
        freq = [[]for i in range(len(nums) + 1)] #index is freq
        for n in nums: #count how many times val occures
            count[n] = 1 + count.get(n, 0) #default 0 if no exist
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k: #guarnteed run 
                    return res
