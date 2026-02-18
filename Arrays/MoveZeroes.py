# Problem: Move Zeroes
# Difficulty: Easy
# Approach: Two Pointer Technique
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None
        """
        j = 0  # Pointer for placing next non-zero element
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
