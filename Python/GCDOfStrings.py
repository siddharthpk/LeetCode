class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # helper func to find gcd of 2 numbers using Euclid's algorithm
        def gcd(a,b):
            # loop until b is 0
            while b:
                # update a to b and b to the remainder of a divided by b
                a,b = b, a%b

            #gcd is stored in a so return a
            return a

        x:str = ""
        # Checking if a GCD string exists for str1 & str2, start by checking if concat of str1 & str2 is the same as str2 & str1
        # helps identify if the 2 strings are made of the same repeated substring
        if str1 + str2 == str2 + str1:    
            x = str1[:gcd(len(str1), len(str2))]
        
        # if str1 & str2 are not composed of the same repeared substring, then no gcd possible so x is empty
        return x