"""
LeetCode 53 - Maximum Subarray
"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = max_global = nums[0]
        for num in nums[1:]: # Since first index is used in initialization, calc will start from index 1
            max_current = max(num + max_current, num)
            if max_current > max_global:
                max_global = max_current
        
        return max_global