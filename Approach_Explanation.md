# Maximum Width Ramp: Three Approaches

- ## Approach 1: Brute Force Approach

    - ### Intuition
        - The problem requires us to find the maximum width of a ramp formed by two indices (i) and (j) in the list such that (i < j) and (nums[i] <= nums[j]). The width is defined as (j - i). By examining all possible pairs of indices, we can determine the maximum width of the ramp.

    - ### Approach
        1. Initialize `max_Width` to store the maximum width found, starting at 0.
        2. Iterate through each possible pair of indices ((i, j)) in the list:
            - The outer loop runs from the first index to the second last index.
            - The inner loop runs from the next index to the last index.
        3. For each pair, check if (nums[i] leq nums[j]):
            - If true, calculate the width (j - i) and update `max_Width` if this width is greater than the current `max_Width`.
        4. After checking all pairs, return the maximum width found.
    
    - ### Time Complexity
        - ___O(n<sup>2</sup>)___, where n is the length of the input list nums.
    
    - ### Space Complexity
        - ___O(1)___, since we are using a fixed amount of extra space.

    - ### Code
        ```python3 []
        from typing import List

        class Solution:
            def maxWidthRamp(self, nums: List[int]) -> int:
                max_Width = 0
                n = len(nums)

                for i in range(n - 1):
                    for j in range(i + 1, n):
                        if nums[i] <= nums[j]:
                            max_Width = max(max_Width, j - i)

                return max_Width

        # Time Complexity: O(n^2), where n is the length of the input list nums.
        # Space Complexity: O(1), since we are using a fixed amount of extra space.
        ```

- ## Approach 2: Sorting

    - ### Intuition
        - To find the maximum width of a ramp in the array, we can leverage sorting. By pairing each element with its index and sorting them based on the values, we can efficiently compute the maximum width without needing to check all pairs explicitly.

    - ### Approach

        1. **Pairing and Sorting**:
            - Create a list of tuples where each tuple consists of the number and its original index: (num, index).
            - Sort this list based on the number values. This allows us to process the elements in increasing order.

        2. **Calculating Maximum Width**:
            - Initialize `max_width` to zero and `min_index` to infinity. `min_index` keeps track of the smallest index encountered as we iterate through the sorted list.
            - As we iterate through the sorted list:
                - Update `min_index` to the minimum index seen so far.
                - Calculate the width as the difference between the current index and `min_index`. Update `max_width` if this width is greater than the previously recorded maximum.

        3. **Return the Result**:
            - After processing all elements, return the `max_width`.

    - ### Time Complexity: 
        - ___O(nlogn)___ due to the sorting step, where n is the length of the input list.
    - ### Space Complexity: 
        - ___O(n)___ for storing the paired list of numbers and indices. 

    - ### Code
        ```python3 []
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
        ```

- ## Approach 3:- Using Stacks

    - ### Intuition
        - The goal is to find the maximum width of a ramp in an array defined by indices (j) and (i) such that (j>i) and (nums[i] <= nums[j]). By using a stack to keep track of indices, we can efficiently find potential candidates for the minimum index (i) while iterating from the end of the list to find suitable (j).

    - ### Approach
        1. **Building the Stack**:
            - We first iterate through the array to create a stack that holds the indices of elements in a way that maintains their increasing order. This is achieved by pushing the index (i) onto the stack only if the current number is less than the number at the index at the top of the stack. This ensures that the stack will only contain indices of local minima.

        2. **Calculating Maximum Width**:
            - We then iterate through the array from the end to the start (reverse order). For each index ( j ):
            - While the stack is not empty and the current number is greater than or equal to the number at the index represented by the top of the stack, we pop the index from the stack and calculate the width ( j - text{index} ). We update `max_width` if this width is greater than the previously recorded maximum.

        3. **Return the Result**:
            - After processing all elements, return the `max_width`.

    - ### Time Complexity: 
        - ___O(n)___, where n is the length of the input list.
    - ### Space Complexity: 
        - ___O(n)___ in the worst case for the stack.    

    - ### Code
        ```python3 []
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
        ```