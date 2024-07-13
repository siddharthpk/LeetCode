"""
LeetCode 2215 - Find the Difference of Two Arrays
Time Complexity - O(n1 + n2) : n1 & n2 are the lengths of the sets
Space Complexity - O(n1 + n2) : n1 & n2 are the lengths of the sets
"""

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        answer1 = set1 - set2
        answer2 = set2 - set1

        return[answer1,answer2]
    
    """
        set1 = set(nums1)
        set2 = set(nums2)
        answer1 = []
        answer2 = []

        for x in set1:
            if x not in set2:
                answer1.append(x)
        for y in set2:
            if y not in set1:
                answer2.append(y)
                

        return[answer1,answer2]
    """
        
   