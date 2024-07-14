class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set1 = set(nums)
        numSum = sum(nums)
        setSum = sum(set1)

        return 2*setSum - numSum