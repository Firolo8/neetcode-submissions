class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # {freq : count}

        count = {} #dictionary
        freq = [[] for i in range(len(nums) + 1)] #empty array size of input

        # count # of times each value in nums occurs 
        for n in nums: 
            count[n] = 1 + count.get(n,0)
        
        #going through each val counted, returns key value pair
        for n, c in count.items(): 
            freq[c].append(n)

        res = [] #top k elemenets 
        #decending , start w/ most frequent #
        for i in range(len(freq) - 1, 0, -1):
            #going through every value, i is another list
            for n in freq[i]:
                res.append(n)
                # guaranteed same len at some point
                if len(res) == k:
                    return res