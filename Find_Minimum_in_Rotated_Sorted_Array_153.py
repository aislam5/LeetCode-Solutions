class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0 
        right = len(nums) - 1

        while left <= right:
            #calculate mid
            mid = (left + right) //2

            if nums[right] <= nums[mid]:
                left = mid + 1
            else:
                right = mid #otherwise mid element gets skipped 

        return nums[mid]
                
            
            

            