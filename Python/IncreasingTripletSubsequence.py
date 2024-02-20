'''
Leetcode 334 - Increasing Triplet Subsequence
Time Complexity - O(n) : n is the length of the array
Space Complexity - O(1) : only maintains 2 vars
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Initialize two variables, first and second, with infinity.
        # These will hold the smallest and second smallest values found so far, respectively.
        first = second = float('inf')
        
        # Iterate through each number in the nums array.
        for num in nums:
            # If the current number is smaller than or equal to first,
            # it becomes the new smallest number (first).
            # This helps us track the lowest value seen so far.
            if num <= first:
                first = num
            # If the current number is greater than first but smaller than or equal to second,
            # it becomes the new second smallest number.
            # This step ensures that second is always greater than first
            # and tracks the second lowest value that forms a potential increasing pair.
            elif num <= second:
                second = num
            # If we find a number greater than both first and second,
            # it means we have found an increasing triplet (first < second < num),
            # so we return True.
            else:
                return True
        # If we finish iterating through the array without finding an increasing triplet, return False.
        
        return False