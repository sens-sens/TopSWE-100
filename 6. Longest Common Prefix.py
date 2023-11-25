class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Find the minimum string's length, so that index out of range will not occur
        end = len(min(strs))

        ans = []

        for i in range(end):

            # Choose any one of the string `strs[0]` and get the i th letter
            current_letter = strs[0][i]

            for string in strs:
                if string[i]!=current_letter:

                    # If the letter mismatch, terminate the program and return the previously matched values

                    if len(ans)>0:
                        return ''.join(ans)                
                    return ""
            
            # Add the letter if all strings contain the same letter
            ans.append(current_letter)
        
        return ''.join(ans)