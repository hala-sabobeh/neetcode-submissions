from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        for i in range(len(arr)-1, -1, -1):
            newmax = max(right_max, arr[i])
            arr[i] = right_max 
            right_max = newmax
        return arr