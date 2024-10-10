# 962. Maximum Width Ramp

__Type:__ Medium <br>
__Topics:__ Array, Stack, Monotonic Stack <br>
__Companies:__ Google, Amazon, Bloomberg, Accenture, Microsoft, Adobe <br>
__Leetcode Link:__ [Maximum Width Ramp](https://leetcode.com/problems/maximum-width-ramp/description/)
<hr>

A __ramp__ in an integer array `nums` is a pair `(i, j)` for which `i < j` and `nums[i] <= nums[j]`. The width of such a ramp is `j - i`.

Given an integer array `nums`, _return the maximum width of a __ramp__ in_ `nums`. If there is no __ramp__ in `nums`, return `0`.
<hr>

### Examples:

__Example 1:__ <br>
__Input:__ nums = [6,0,8,2,1,5] <br>
__Output:__ 4 <br>
__Explanation:__ The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.

__Example 2:__ <br>
__Input:__ nums = [9,8,1,0,1,9,4,0,4,1] <br>
__Output:__ 7 <br>
__Explanation:__ The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
<hr>

### Constraints:

- <code>2 <= nums.length <= 5 * 10<sup>4</sup></code>
- <code>0 <= nums[i] <= 5 * 10<sup>4</sup></code>
