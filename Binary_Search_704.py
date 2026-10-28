class Solution:
    def search(self, nums: list[int], target: int) -> int:
        #so we make a while loop and have a left and right index tracker 
        #using the left and right we find the mid index 
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return -1
