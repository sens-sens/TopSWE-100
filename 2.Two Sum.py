class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Using Hashmap to store number as key : position(index) as value
        elements = {}

        for index,num in enumerate(nums):
            
            value = target-num
            
            if value in elements:
            
                # Get the position of the number
                return [index,elements[value]]
            
            # If not, add the position to the `elements` variable
            elements[num]=index