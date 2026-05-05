from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        
        # First half:copy nums to positions 0 to n-1
        i = 0
        while i < n:  
            ans[i] = nums[i]  
            i = i + 1
        
        # Second half:copy nums to positions n to 2n-1
        i = 0
        while i < n:
            ans[i + n] = nums[i]  
            i = i + 1
        
        return ans