'''
Leetcode 151 - Reverse Words in a String
Time Complexity - O(n) : n is the length of the string
Space Complexity - O(n) : n is the length of the string
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        # Result list, later to be converted to string
        result: list = []

        # Splitting string into words & removing spaces
        listString: list = s.split()

        # running for loop with list reversed
        for word in reversed(listString):
            result.append(word)

        # Returning the result list by converting to string with spaces
        return ' '.join(result)

        