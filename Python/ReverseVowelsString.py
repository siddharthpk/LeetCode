# Leetcode 345
class Solution:
    def reverseVowels(self, s: str) -> str:
        #Convert string to list
        s_list = list(s)
        # Create a temp vowel holder list
        inStringVowels = []
        inStringVowelsIndex = []
        vowels: str = "aeiouAEIOU"

        # Iterate through the string to find the vowels and their indices
        for i in range(len(s)):
            if(s[i] in vowels):
                # Store this vowel and its index
                inStringVowels.append(s[i])
                inStringVowelsIndex.append(i)

        # Place vowels back into the string in reverse order
        for i in inStringVowelsIndex:
            s_list[i] = inStringVowels.pop() 

        # Convert the list to string and return
        return ''.join(s_list)
    
                
