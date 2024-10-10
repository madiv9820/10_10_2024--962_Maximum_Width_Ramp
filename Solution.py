from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # Initialize the maximum width to 0
        max_Width = 0
        n = len(nums)

        # Iterate through each pair of indices (i, j)
        for i in range(n - 1):
            for j in range(i + 1, n):
                # Check if the current pair satisfies the condition
                if nums[i] <= nums[j]:
                    # Update the maximum width if the current width is greater
                    max_Width = max(max_Width, j - i)

        return max_Width

# Time Complexity: O(n^2), where n is the length of the input list nums.
# Space Complexity: O(1), since we are using a fixed amount of extra space.