from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # Pair each number with its index
        nums_with_index = [(num, index) for index, num in enumerate(nums)]
        
        # Sort based on the values (first element of the tuples)
        nums_with_index.sort()

        max_width = 0
        min_index = float('inf')  # Initialize to a very high value

        # Iterate through the sorted list
        for value, index in nums_with_index:
            # Update the minimum index encountered so far
            min_index = min(min_index, index)
            # Calculate width and update max_width
            max_width = max(max_width, index - min_index)

        return max_width

# Time Complexity: O(n log n) due to the sorting step, where n is the length of the input list.
# Space Complexity: O(n) for storing the paired list of numbers and indices.