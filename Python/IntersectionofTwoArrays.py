class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(set(nums2))
        """
        Alternative        
        set1 = set(nums1)
        set2 = set(nums2)
        intersect = set1.intersection(set2)
        return list(intersect)
        """