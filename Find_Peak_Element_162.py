class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        #so the first approach in mind is that loop through the list and then check if its left and right are smaller than it if so return it
        """        
        for i, num in enumerate(nums):
            if i == 0:
                continue
            elif i == len(nums) - 1:
                left = nums[i-1]
                if num > left:
                    return i
            else:
                left = nums[i-1]
                right = nums[i+1]
                if num > left and num > right:
                    return i
                else:
                    continue
        return 0
        """        
        # ok now that the general approach is taken care of we will tackle the bianry search approach
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if (mid-1<0 or nums[mid-1] < nums[mid]) and (mid+1>len(nums)-1 or nums[mid+1] < nums[mid]):
                return mid
            if mid+1<=len(nums)-1 and nums[mid] <= nums[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
        return 0
            

