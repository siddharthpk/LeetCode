class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Creating our result array
        result: bool = []
        # Finding MaxCandies in candies list
        maxCandies: int = max(candies)

        # Using the greedy approach, we'll check for each kid if candies[i] + extraCandies >= maxCandies
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        
        return result

        