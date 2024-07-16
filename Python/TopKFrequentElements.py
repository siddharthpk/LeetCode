"""
LeetCode 347 - Top K Frequent Elements
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_freq = {}
        answer = []

        for num in nums:
            if num in element_freq:
                element_freq[num] += 1
            else:
                element_freq[num] = 1
        
        print(element_freq)

        for i in range(0,k):
            max_key = max(element_freq, key=element_freq.get)
            answer.append(max_key)
            element_freq.pop(max_key)


        return answer