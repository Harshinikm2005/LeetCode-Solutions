# Problem: Best Time to Buy and Sell Stock
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
