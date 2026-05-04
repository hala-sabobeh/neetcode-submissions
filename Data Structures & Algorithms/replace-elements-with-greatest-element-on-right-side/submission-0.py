from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []  
        
       
        for i in range(len(arr)):
            
            if i == len(arr) - 1:
                result.append(-1)
            else:
                # from the right to end
                biggest = max(arr[i+1:])
                result.append(biggest)
        
        return result