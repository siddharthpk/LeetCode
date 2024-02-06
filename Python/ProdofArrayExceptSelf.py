'''
LeetCode 238 - Product of Array Except Self
Time Complexity - O(n) : n is the length of the List
Space Complexity - O(n) : n is the length of the List
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left, right, answer = [0]*length, [0]*length, [0]*length
        
        # left[i] contains the product of all elements to the left of i. For left[0], there are no elements to the left, so left[0] is 1.
        left[0] = 1
        for i in range(1, length):
            left[i] = nums[i - 1] * left[i - 1]
        
        # right[i] contains the product of all elements to the right of i. For right[-1], there are no elements to the right, so right[-1] is 1.
        right[length - 1] = 1
        for i in reversed(range(length - 1)):
            right[i] = nums[i + 1] * right[i + 1]
        
        # Construct the answer array
        for i in range(length):
            answer[i] = left[i] * right[i]
        
        return answer