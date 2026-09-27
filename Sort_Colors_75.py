class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 
        current = 0
        right = len(nums)-1
        while current <= right:
            temp = 0
            if nums[current] == 0:
                temp = nums[left]
                nums[left] = nums[current]
                nums[current] = temp
                left += 1
                current += 1
            elif nums[current] == 1:
                current += 1
            else:
                temp = nums[right]
                nums[right] = nums[current]
                nums[current] = temp
                right -= 1





        
    
        