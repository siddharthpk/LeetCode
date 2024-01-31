class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # Run loops to merge strings characters to a result string
        result: str = ""

        # Iterate over the length of the longer string
        for x in range(max(len(word1), len(word2))) : 
            # Adding character from word1 if available
            if x < len(word1):
                result += word1[x]
            # Adding character from word2 if available
            if x < len(word2):
                result += word2[x]
        return result
        
        