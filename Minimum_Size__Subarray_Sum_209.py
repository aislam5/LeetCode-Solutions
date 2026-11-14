from collections import defaultdict
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0 
        currSum = 0
        size = float('inf')

        for right, num in enumerate(nums):
            currSum += num
            while currSum >= target:
                size = min(size, right - left + 1) 
                currSum -= nums[left]
                left += 1

        if size != float('inf'):
            return size
        else:
            return 0
