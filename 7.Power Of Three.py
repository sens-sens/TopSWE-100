class Solution:

    def isPowerOfThree(self, n: int) -> bool:
        
        # Initialize Remainder and Quotient as n
        remainder = n
        quotient = n

        if n==0:
            return False

        # Loop until the quotient is 1 (3/3=1)
        while quotient!=1:
            
            # Calculate remainder
            remainder=quotient%3

            if remainder!=0:    
                # Remainder should be 0, inorder to be divisible by 3
                return False
            
            # Assign the new quotient value
            quotient=quotient//3

        return True