class Solution:

    def isPalindrome(self, s: str) -> bool:

        obtained = [] 

        # Convert the given string into normal form by removing non-ascii characters
        for i in s:
            if i.isalnum():
                obtained.append(i.lower())
        
        formatted = ''.join(obtained)

        # Check whether the string is palindrome by reversing the formatted string
        return formatted==formatted[::-1]