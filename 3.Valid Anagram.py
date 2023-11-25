class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Using Hashmap
        first = {}
        second = {}

        # Add letters and their count as key and value
        for i in s:
            first[i] = first.get(i,0)+1

        for j in t:
            second[j]=second.get(j,0)+1

        # If the count of letters match, return true. Else, return false
        return first == second