class Solution:
    
    # Do not return anything, modify s in-place instead.
    
    def reverseString(self, s: List[str]) -> None:
        
        # Using two pointer approach
        i=0
        j = len(s)-1

        while i<j:
            # Swapping
            s[i],s[j]= s[j],s[i]

            i+=1
            j-=1
        
