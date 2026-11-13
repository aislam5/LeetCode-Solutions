class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        
        left = 0 
        prod = 1
        count = 0 

        for right, num in enumerate(nums):
            prod = prod * num
            while prod >= k:
                prod = prod // nums[left]
                left += 1
            count = count + (right - left + 1)
        return count

# first adds 1 for [10]
# second adds 2 for [10,5] and [5]
# third adds 3 for [10,5,2], [5,2], and [2]
# and so on the cycle continues
