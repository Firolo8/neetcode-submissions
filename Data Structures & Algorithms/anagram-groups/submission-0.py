class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list) #map charCount to list of anagrams. default value is list to not deal with edge case

        for string in strs: 
            count = [0] * 26 # a...z

            #how many of each char.
            for char in string:
                # a = 80 -> 0, 80 - 80 = 0... b = 81 - 80...
                count[ord(char) - ord("a")] += 1 #mapping a to 0 -> z to 25

            # in python lists can not be keys, change to tuple cuz immutable
            anagrams[tuple(count)].append(string) 

        return list(anagrams.values())

        #time complexity: O(m * n)