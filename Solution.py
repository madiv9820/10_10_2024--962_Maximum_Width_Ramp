from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        max_width = 0
        
        # Build a stack of indices based on the original array
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        # Iterate from the end of the array to find the maximum width
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                max_width = max(max_width, j - stack.pop())

        return max_width

# Time Complexity: O(n), where n is the length of the input list.
# Space Complexity: O(n) in the worst case for the stack.