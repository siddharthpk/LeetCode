# Leetcode 605
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count: int = 0 # var to store how many flowers can be planted
        for x in range(len(flowerbed)):
            # Check if current plot is empty and either it's the first plot, or the previous plot is empty,
            # and either it's the last plot, or the next plot is empty
            if flowerbed[x] == 0 and (x==0 or flowerbed[x-1]== 0) and (x == len(flowerbed)-1 or flowerbed[x+1] == 0):
                flowerbed[x] = 1 # Plant a flower
                count += 1 # increment count
            if count >=n:
                return True
        return False
            